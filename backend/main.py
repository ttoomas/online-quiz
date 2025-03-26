import eventlet
from helpers.socketio import sio, app, rooms
from controllers.room import joinRoom, getRoomPlayers, create_room
from controllers.load import check_jwt_token, init_client

tempRoomId = "karel"
rooms[tempRoomId] = {
    "status": "waiting",
    "players": []
}

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

# ADMIN
sio.on("createRoom", create_room)

# TESTING

# @sio.on("createRoom")
# def createRoom(sid, data):
#     rooms[data["key"]] = {
#         "status": "waiting",
#         "players": []
#     }

# # PLAYER
# @sio.on("playerInit")
# def playerInit(sid):
#     print("Player connected")
#     sio.save_session(sid, {"role": "player"})

# @sio.on("connectToRoom")
# def connectToRoom(sid, data):
#     roomId = data["roomId"]
#     userName = data["userName"]
    
#     # Check if room exists
#     if roomId not in sio.manager.rooms.get("/"):
#         print("Room does not exist")
#         sio.emit("roomError", {"message": "Room does not exist"})

#         return

#     sio.enter_room(sid, roomId)

#     # Update user name
#     sio.save_session(sid, {"userName": userName})

#     # Send waiting room to user
#     print("Player connected to room: " + roomId)
#     sio.emit("playerWaitingRoom")

# # ADMIN
# @sio.on("adminInit")
# def adminInit(sid):
#     print("Admin connected")
#     sio.save_session(sid, {"role": "admin"})

# @sio.on("createQuiz")
# def createQuiz(sid, data):
#     quizId = data["quizId"]

#     # Check if quiz exists
#     # TODO!: DB CHECK

#     # Create room
#     sio.enter_room(sid, quizId)
    
#     sio.emit("quizCreated")

#     print("Quiz created with id: " + quizId)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5100)), app)