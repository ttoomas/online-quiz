import socketio
import threading
from frames.waiting_room import update_waiting_players
from frames.home_frame import update_quiz_list
from frames.guessing_room import update_guessing_players, update_guessing_title, start_guessing_time


SIO = None

def init():
    sio = socketio.Client()

    @sio.event
    def connect():
        sio.emit('initClient', {
            "role": "admin"
        }, callback=on_connect)
        print('connection established')
    
    @sio.event
    def disconnect():
        print('disconnected from server')
    
    @sio.on('updateRoomPlayers')
    def update_room_players(data):
        print(data)
        update_waiting_players(data["playerNames"])

    @sio.on('showQuestion')
    def show_question(data):
        title = data["title"]
        time = data["time"]
        
        update_guessing_title(title)
        start_guessing_time(time)


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

# On connect
def on_connect(data):
    quiz_list = data["quiz_list"]

    update_quiz_list(quiz_list)