import socketio
import threading

SIO = None

def init():
    sio = socketio.Client()

    @sio.event
    def connect():
        sio.emit('adminInit')
        print('connection established')


    @sio.event
    def disconnect():
        print('disconnected from server')
    
    @sio.on('quizCreated')
    def on_quiz_created():
        print('Quiz room created')


    sio.connect('http://localhost:5100')
    
    wait_thread = threading.Thread(target=sio.wait)
    wait_thread.start()

    return sio

def get_sio():
    global SIO

    if SIO is None:
        SIO = init()

    return SIO

def default_connect():
    get_sio()

def close_connection():
    sio = get_sio()
    sio.disconnect()

# Join room
def create_room_request(quizId):
    sio = get_sio()
    sio.emit('createRoom', {"quizId": quizId})