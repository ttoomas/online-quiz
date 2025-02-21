import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    # Create room (will be created from the py frontend)
    tempRoomId = "kareljaromir123"
    sio.enter_room(sid, tempRoomId)
    
    print('connect ')

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


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)