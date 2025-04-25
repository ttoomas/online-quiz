import eventlet
from helpers.socketio import sio, app
from helpers.room_helper import rooms
from controllers.room import joinRoom, getRoomPlayers, create_room
from controllers.load import check_jwt_token, init_client
from controllers.questions import start_questions_loop, send_answer
from controllers.create_quiz import create_quiz_controller


# SOCKET.IO EVENTS
# GENERAL
@sio.event
def connect(sid, environ):
    print('connect server')
    print(rooms)

@sio.event
def disconnect(sid):
    print('disconnect ')
    sio.leave_room(sid, 'chat_users')

# Init client (player/admin)
sio.on('initClient', init_client)

# PLAYER
sio.on('checkJwtToken', check_jwt_token)

sio.on('joinRoom', joinRoom)
sio.on('getRoomPlayers', getRoomPlayers)

sio.on('sendAnswer', send_answer)

# ADMIN
sio.on("createRoom", create_room)
sio.on("startQuiz", start_questions_loop)

sio.on("createQuiz", create_quiz_controller)

# RUN THE SERVER
if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5100)), app)


# from db.get_questions import get_quiz_questions
# from db.quiz_list import get_quiz_list
# from db.create_quiz import create_quiz