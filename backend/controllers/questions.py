import threading
from db.get_questions import get_quiz_questions
from helpers.socketio import sio
from helpers.rooms import rooms, get_room_id_by_sid, find_answer_by_id, update_player_score

def start_questions_loop(sid):
    room_id = get_room_id_by_sid(sid)
    if room_id is None:
        print("Room not found")
        return
    
    rooms[room_id]["status"] = "answering"
    
    # Get questions
    questions = get_quiz_questions()
    number_of_questions = len(questions)
    current_question = rooms[room_id]["current_question"] + 1
    time = 10

    question1 = {
        "question": questions[current_question]["question"],
        "answers": questions[current_question]["answers"]
    }

    show_question(room_id, question1["question"], question1["answers"], number_of_questions, current_question, time)
    
    t = threading.Timer(time, show_answer, args=[room_id])
    t.start()
    print("Timer started")

def show_question(room_id, title, answers_list, number_of_questions, current_question, time):
    rooms[room_id]["status"] = "answering"
    rooms[room_id]["current_question"] = current_question
    
    sio.emit("showQuestion", {
        "title": title,
        "answers_list": answers_list,
        "number_of_questions": number_of_questions,
        "current_question": current_question + 1,
        "time": time
    }, room=room_id)

def show_answer(room_id):
    # rooms[room_id]["status"] = "showing_answer"

    # sio.emit("showAnswer", room=room_id)
    print("show answer - ", room_id)

def send_answer(sid, data):
    print("Received answer")
    
    room_id = get_room_id_by_sid(sid)
    answer_id = data["answer_id"]

    if room_id is None:
        print("Room not found")
        return
    
    # Check, if the answer is correct
    current_question_index = rooms[room_id]["current_question"]
    question_list = get_quiz_questions()
    current_question = question_list[current_question_index]
    current_answer = find_answer_by_id(current_question["answers"], answer_id)

    if current_answer is None:
        print("Answer not found")
        return
    
    is_answer_correct = current_answer["correct"]

    update_player_score(room_id, sid, answer_id, is_answer_correct)

    print(is_answer_correct)
    print(rooms)