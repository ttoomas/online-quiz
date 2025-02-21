import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    # Create room (will be created from the py frontend)
    # tempRoomId = "kareljaromir123"
    # sio.enter_room(sid, tempRoomId)
    
    print('connect server')

@sio.event
def my_message(sid, data):
    print('message ')

@sio.event
def disconnect(sid):
    print('disconnect ')
    
    # sio.leave_room(sid, 'chat_users')

@sio.on("connectToRoom")
def roomConnect(sid, data):
    roomId = data["roomId"]
    userName = data["userName"]
    
    # Check if room exists
    if not sio.rooms(sid).get(roomId):
        sio.emit("roomError", {"message": "Room does not exist"})

        return
    else:
        sio.enter_room(sid, roomId)

    # Update user name
    sio.save_session(sid, {"userName": userName})

    # Send success message to user

# PLAYER
@sio.on("playerInit")
def playerInit(sid):
    print("Player connected")
    sio.save_session(sid, {"role": "player"})

@sio.on("connectToRoom")
def connectToRoom(sid, data):
    roomId = data["roomId"]
    userName = data["userName"]
    
    # Check if room exists
    if roomId not in sio.manager.rooms.get("/"):
        print("Room does not exist")
        sio.emit("roomError", {"message": "Room does not exist"})

        return

    sio.enter_room(sid, roomId)

    # Update user name
    sio.save_session(sid, {"userName": userName})

    # Send waiting room to user
    print("Player connected to room: " + roomId)
    sio.emit("playerWaitingRoom")

# ADMIN
@sio.on("adminInit")
def adminInit(sid):
    print("Admin connected")
    sio.save_session(sid, {"role": "admin"})

@sio.on("createQuiz")
def createQuiz(sid, data):
    quizId = data["quizId"]

    # Check if quiz exists
    # TODO!: DB CHECK

    # Create room
    sio.enter_room(sid, quizId)
    
    sio.emit("quizCreated")

    print("Quiz created with id: " + quizId)



if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)