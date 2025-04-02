from controllers.default_connect import get_sio

def start_questions():
    sio = get_sio()

    sio.emit('startQuiz')