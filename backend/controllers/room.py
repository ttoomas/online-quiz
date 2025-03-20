import uuid
import jwt
from env import JWT_SECRET
from helpers.socketio import sio, rooms

def joinRoom(sid, data):
    room_id = data["roomId"]
    user_name = data["username"]

    # Check if room exists
    if room_id not in rooms:
        print("Room does not exist")
        sio.emit("roomError", {"message": "Room does not exist"})

        return { 'success': False }
    else:
        print("Player connected to room: " + room_id)
        sio.enter_room(sid, room_id)

    # Generate jwt
    uuid = uuid.uuid4().hex
    jwt_token = jwt.encode({
        "uuid": uuid,
        "room_id": room_id,
        "username": user_name
    }, JWT_SECRET, algorithm="HS256")

    # Update user name    
    rooms[room_id].append({
        "sid": sid,
        "username": user_name,
        "uuid": uuid
    })
    
    # Send waiting room to user
    playerNames = filterPlayerNames(room_id)
    data = {
        "playerNames": playerNames
    }

    sio.emit("updateRoomPlayers", data, room=room_id, skip_sid=sid)

    return {
        'success': True,
        'jwt': jwt_token
    }

def getRoomPlayers(sid):
    # Get room id
    user_rooms = sio.rooms(sid)
    room_id = user_rooms[1]

    # Get room player names and return
    playerNames = filterPlayerNames(room_id)

    return {
        "playerNames": playerNames
    }
    

def filterPlayerNames(id):
    room = rooms[id]
    playerNames = []

    for player in room:
        playerNames.append(player["username"])

    return playerNames