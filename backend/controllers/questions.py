import asyncio
import threading
import eventlet
import time
from db.get_questions import get_quiz_questions
from helpers.socketio import sio
from helpers.rooms import rooms, get_room_id_by_sid, find_answer_by_id, update_player_score, get_player_by_sid, update_non_guessed_players

def start_questions_loop(sid):
    room_id = get_room_id_by_sid(sid)
    if room_id is None:
        print("Room not found")
        return
    
    rooms[room_id]["status"] = "answering"
    
    # Get questions
    questions = get_quiz_questions()
    number_of_questions = len(questions)
    current_question_index = rooms[room_id]["current_question"]["index"] + 1
    current_question_id = questions[current_question_index]["question_id"]
    time_limit = 5

    question1 = {
        "question": questions[current_question_index]["question"],
        "answers": questions[current_question_index]["answers"]
    }

    show_question(room_id, question1["question"], question1["answers"], number_of_questions, current_question_index, current_question_id, time_limit)
    
    # Start limit timer
    print("Started task timer")
    rooms[room_id]["question_timer"] = True
    sio.start_background_task(start_timer, time_limit, room_id)

def start_timer(time_limit, room_id):
    eventlet.sleep(time_limit)
    if rooms[room_id]["question_timer"] == True:
        show_answer(room_id)
    

def show_question(room_id, title, answers_list, number_of_questions, current_question_index, current_question_id, time):
    rooms[room_id]["status"] = "answering"
    rooms[room_id]["current_player_guessed"] = []
    rooms[room_id]["current_question"]["index"] = current_question_index
    rooms[room_id]["current_question"]["question_id"] = current_question_id
    
    sio.emit("showQuestion", {
        "title": title,
        "answers_list": answers_list,
        "number_of_questions": number_of_questions,
        "current_question": current_question_index + 1,
        "time": time
    }, room=room_id)

def show_answer(room_id):
    if rooms[room_id]["status"] != "answering":
        return

    # Cancel the timer
    if rooms[room_id]["question_timer"] is True:
        rooms[room_id]["question_timer"] = False

    # Update questions of each player who not guessed
    update_non_guessed_players(room_id)

    # Show answer
    rooms[room_id]["status"] = "showing_answer"

    # Emit the answer to each player
    print("Sending show answer")
    for player in rooms[room_id]["players"]:
        sio.emit("showAnswer", {
            "sid": player["sid"]
        }, room=player["sid"])

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

    # Update guessed players
    current_user = get_player_by_sid(sid)

    if current_user is not None:
        rooms[room_id]["current_player_guessed"].append(current_user["username"])
    
    # If all players guessed, show answer
    # Else emit the guessed players
    if len(rooms[room_id]["current_player_guessed"]) == len(rooms[room_id]["players"]):
        show_answer(room_id)
    else:
        sio.emit("updateGuessedPlayers", {
            "guessed_players": rooms[room_id]["current_player_guessed"],
        }, room=room_id)