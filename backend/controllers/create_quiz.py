from db.create_quiz import create_quiz
from db.quiz_list import add_quiz_to_list, get_quiz_list

def create_quiz_controller(sio, data):
    quiz_data = data["quiz_data"]

    quiz = create_quiz(quiz_data)
    add_quiz_to_list(quiz["name"], quiz["uuid"])

    return {
        "name": quiz["name"],
        "uuid": quiz["uuid"]
    }