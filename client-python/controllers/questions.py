# import random
from controllers.default_connect import get_sio


# def start_questions(questions, room_id):
#     for question in questions:
#         title = question["question"]
#         answers = question["answers"]

#         # Randomize the order of answers
#         answers_list = []
#         for answer in answers:
#             answers_list.append({
#                 "answer": answer["answer"],
#                 "id_question": answer["id_question"],
#             })
#         random.shuffle(answers_list)

#         # Send the question and answers to the client
#         show_question(room_id, title, answers_list)
        

# def show_question(room_id, title, answers_list):
#     sio = get_sio()
#     sid = sio.sid

#     sio.emit('showQuestion', {
#         title,
#         answers_list
#     }, room=room_id, skip_sid=sid)

# def show_answer():
#     pass


def start_questions(room_id):
    sio = get_sio()

    sio.emit('startQuiz', {
        "room_id": room_id
    })