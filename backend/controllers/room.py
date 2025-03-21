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
    user_uuid = uuid.uuid4().hex
    jwt_token = jwt.encode({
        "uuid": user_uuid,
        "room_id": room_id,
        "username": user_name
    }, JWT_SECRET, algorithm="HS256")

    # Update user name    
    rooms[room_id]["players"].append({
        "sid": sid,
        "username": user_name,
        "uuid": user_uuid,
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
    room_id = None

    for room_key in user_rooms:
        if room_key in rooms:
            room_id = room_key
            break
        
    if not room_id:
        return []
    
    # Get room player names and return
    playerNames = filterPlayerNames(room_id)

    return {
        "playerNames": playerNames
    }
    

def filterPlayerNames(id):
    room = rooms[id]["players"]
    playerNames = []

    for player in room:
        playerNames.append(player["username"])

    return playerNames

def create_room(sid, data):
    room_uuid = data.