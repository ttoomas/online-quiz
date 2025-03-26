import socketio
import threading
# from main import update_waiting_room
from frames.waiting_room import update_waiting_players

SIO = None

def init():
    sio = socketio.Client()

    @sio.event
    def connect():
        sio.emit('initClient', {
            "role": "admin"
        })
        print('connection established')

    @sio.event
    def disconnect():
        print('disconnected from server')
    
    @sio.on('updateRoomPlayers')
    def update_room_players(data):
        print(data)
        update_waiting_players(data["playerNames"])
        # update_waiting_room(data["playerNames"])


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