import eventlet
from helpers.socketio import sio, app
from helpers.rooms import rooms
from controllers.room import joinRoom, getRoomPlayers, create_room
from controllers.load import check_jwt_token, init_client
from controllers.questions import start_questions_loop, send_answer


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

# RUN THE SERVER
if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5100)), app)