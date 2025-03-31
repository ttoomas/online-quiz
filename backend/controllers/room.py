import uuid
import jwt
from env import JWT_SECRET
from helpers.role_check import only_admin, only_player
from helpers.socketio import sio
from helpers.rooms import rooms, get_room_id_by_sid, create_room_var, add_player_to_room

# @only_player
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

    print("Generating jwt")
    # Generate jwt
    user_uuid = uuid.uuid4().hex
    jwt_token = jwt.encode({
        "uuid": user_uuid,
        "room_id": room_id,
        "username": user_name
    }, JWT_SECRET, algorithm="HS256")

    print("updating room")
    # Update user name    
    add_player_to_room(room_id, sid, user_name, user_uuid)

    print("sending waiting room")
    # Send waiting room to user and admin to update players
    playerNames = filterPlayerNames(room_id)
    data = {
        "playerNames": playerNames
    }

    sio.emit("updateRoomPlayers", data, room=room_id, skip_sid=sid)

    print("returned")
    return {
        'success': True,
        'jwt': jwt_token
    }

def getRoomPlayers(sid):
    room_id = get_room_id_by_sid(sid)

    if room_id is None:
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

# @only_admin
def create_room(sid, data):
    room_uuid = data["quizId"]
    create_room_var(room_uuid, sid)

    # Put admin inside of the room
    sio.enter_room(sid, room_uuid)

    print(rooms)

    return {
        'success': True
    }