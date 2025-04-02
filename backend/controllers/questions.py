import asyncio
import threading
import eventlet
import time
from db.get_questions import get_quiz_questions
from helpers.socketio import sio
from helpers.room_helper import rooms, get_room_id_by_sid, find_answer_by_id, update_player_score, get_player_by_sid, update_non_guessed_players
from helpers.question_helper import get_questions_data, get_round_result_usernames, question_answers_result, get_total_quiz_results

def start_questions_loop(sid):
    room_id = get_room_id_by_sid(sid)
    if room_id is None:
        print("Room not found")
        return
    
    rooms[room_id]["status"] = "answering"
    
    # Get questions
    show_question(room_id)
    
    # Start limit timer
    print("Started task timer")
    rooms[room_id]["question_timer"] = True
    sio.start_background_task(start_timer, room_id)

def start_timer(room_id):
    time_limit = rooms[room_id]["time_limit"]

    eventlet.sleep(time_limit)
    if rooms[room_id]["question_timer"] == True:
        print("called show_answer via timer")
        show_answer(room_id)
    

def show_question(room_id):
    # Update question index to previous index plus one to work with the new question
    rooms[room_id]["current_question"]["index"] = rooms[room_id]["current_question"]["index"] + 1    

    # Get data
    question_data = get_questions_data(room_id)
    # TODO! sending with true/false if its correct
    
    # Update room data
    rooms[room_id]["status"] = "answering"
    rooms[room_id]["round_results"] = []
    rooms[room_id]["current_question"]["question_id"] = question_data["question_id"]
    
    sio.emit("showQuestion", {
        "title": question_data["title"],
        "answers_list": question_data["answers_list"],
        "number_of_questions": question_data["number_of_questions"],
        "current_question": question_data["current_question"] + 1,
        "time": question_data["time"]
    }, room=room_id)

def show_answer(room_id):
    if rooms[room_id]["status"] != "answering":
        return

    # Cancel the timer
    if rooms[room_id]["question_timer"] is True:
        rooms[room_id]["question_timer"] = False

    # Update questions of each player who not guessed
    update_non_guessed_players(room_id)

    # Check if the game is over
    questions_length = len(get_quiz_questions())
    
    if rooms[room_id]["current_question"]["index"] >= questions_length:
        # End the game
        # Show quiz results
        show_quiz_results(room_id)
    else:
        # Show the round answers
        show_round_results(room_id)

def show_quiz_results(room_id):
    rooms[room_id]["status"] = "showing_results"

    # Emit the answer to each player
    total_player_results = get_total_quiz_results(room_id)
    questions_length = len(get_quiz_questions())

    data = {
        "number_of_questions": questions_length,
        "total_players": len(rooms[room_id]["players"]),
    }
    
    for player in rooms[room_id]["players"]:
        # current_player_data = player_data.copy()
        # current_player_data["round_answers"] = 


def show_round_results(room_id):
    # Show answer
    rooms[room_id]["status"] = "showing_answer"

    # Emit the answer to each player
    question_data = get_questions_data(room_id)
    player_data = {
        "title": question_data["title"],
        "current_question": question_data["current_question"],
        "number_of_questions": question_data["number_of_questions"],
        "round_results": rooms[room_id]["round_results"],
        "round_answers": None
    }
    
    # Send the answer to each player
    for player in rooms[room_id]["players"]:
        current_player_data = player_data.copy()
        current_player_data["round_answers"] = question_answers_result(room_id, player["sid"])
        
        sio.emit("showRoundResults", current_player_data, room=player["sid"])
    
    # Send answer to admin
    sio.emit("showRoundResults", {
        "round_results": player_data["round_results"]
    }, room=rooms[room_id]["admin"])

def send_answer(sid, data):
    print("Received answer")
    
    room_id = get_room_id_by_sid(sid)
    answer_id = data["answer_id"]
    question_id = rooms[room_id]["current_question"]["question_id"]

    if room_id is None:
        print("Room not found")
        return
    
    # Check, if the answer is correct
    current_question_index = rooms[room_id]["current_question"]["index"]
    question_list = get_quiz_questions()
    current_question = question_list[current_question_index]
    current_answer = find_answer_by_id(current_question["answers"], answer_id)

    if current_answer is None:
        print("Answer not found")
        return
    
    is_answer_correct = current_answer["correct"]

    update_player_score(room_id, sid, question_id, answer_id, is_answer_correct)

    # If all players guessed, show answer
    # Else emit the guessed players
    if len(rooms[room_id]["round_results"]) == len(rooms[room_id]["players"]):
        show_answer(room_id)
    else:
        round_usernames = get_round_result_usernames(room_id)
        
        sio.emit("updateGuessedPlayers", {
            "guessed_players": round_usernames,
        }, room=room_id)