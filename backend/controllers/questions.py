import threading
from db.get_questions import get_quiz_questions
from helpers.socketio import sio, rooms

def start_questions_loop(sid, data):
    room_id = data["room_id"]
    rooms[room_id]["status"] = "answering"
    
    # Get questions
    questions = get_quiz_questions()
    number_of_questions = len(questions)
    current_question = rooms[room_id]["current_question"] + 1
    time = 5

    question1 = {
        "question": questions[current_question]["question"],
        "answers": questions[current_question]["answers"]
    }

    show_question(room_id, question1["question"], question1["answers"], number_of_questions, current_question, time)
    
    t = threading.Timer(10, show_answer, args=[room_id])
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
    rooms[room_id]["status"] = "showing_answer"

    sio.emit("showAnswer", room=room_id)