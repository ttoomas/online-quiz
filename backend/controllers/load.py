import jwt
from env import JWT_SECRET
from helpers.socketio import sio
from helpers.room_helper import rooms
from helpers.role_check import only_player
from db.quiz_list import get_quiz_list

# @only_player
def check_jwt_token(sid, data):
    jwt_token = data["jwtToken"]

    token_data = jwt.decode(jwt_token, JWT_SECRET, algorithms=["HS256"])

    if (
        token_data is None or
        "uuid" not in token_data or
        "room_id" not in token_data or
        "username" not in token_data
    ):
        return { 'success': False }

    # Get room id
    player_uuid = token_data["uuid"]
    room_id = token_data["room_id"]

    if room_id not in rooms:
        return { 'success': False }

    room = rooms[room_id]

    # Get player
    player = find_player_uuid(room, player_uuid)

    if not player:
        return { 'success': False }

    # SUCCESS
    # Connect to the room
    print("entered room")
    sio.enter_room(sid, room_id)
    
    # Send status
    return {
        'success': True,
        'status': room["status"]
    }

def find_player_uuid(room, player_uuid):
    for player in room["players"]:
        if player["uuid"] == player_uuid:
            return player

    return None


def init_client(sid, data):
    role = data["role"]

    if role == "player":
        print("Init player")
        sio.save_session(sid, {
            "role": "player"
        })

        return {
            'success': True
        }
    elif role == "admin":
        print("Init admin")
        sio.save_session(sid, {
            "role": "admin"
        })


        quiz_list = get_quiz_list()
        print("quiz list: ")
        print(quiz_list)

        return {
            'success': True,
            'quiz_list': quiz_list
        }

    return { 'success': False }