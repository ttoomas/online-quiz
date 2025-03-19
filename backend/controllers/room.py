from helpers.socketio import sio

def joinRoom(sid, data):
    roomId = data["roomId"]
    userName = data["username"]
    
    # Check if room exists
    print(sio.rooms(sid))
    if roomId not in sio.rooms(sid):
        print("Room does not exist")
        sio.emit("roomError", {"message": "Room does not exist"})

        return { 'success': False }
    else:
        print("Player connected to room: " + roomId)
        sio.enter_room(sid, roomId)

    # Update user name
    sio.save_session(sid, {"userName": userName})

    return { 'success': True }