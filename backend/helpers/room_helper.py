from helpers.socketio import sio

"""
rooms dictionary structure:
{
    "room_id": {
        "status": "waiting" / "answering" / "showing_answer",
        "current_question": {
            "index": -1,
            "question_id": "question_id",
        },
        "round_results": [{
            "username": "player_username",
            "score": 0,
            "is_correct": true / false
        }],
        "question_timer": None,
        "admin": "admin_sid",
        "time_limit": int in seconds,
        "players": [
            {
                "sid": "player_sid",
                "username": "player_username",
                "uuid": "player_uuid",
                "score": 0,
                "correct_answers": 0,
                "questions": [
                    {
                        "question_id": "question_id",
                        "answer_id": "answer_id",
                        "correct": true / false
                    }
                ]
            }
        ]
    }
}
"""

rooms = {}


# ROOM HELPERS
def create_room_var(room_uuid, admin_sid):
    rooms[room_uuid] = {
        "status": "waiting",
        "current_question": {
            "index": -1,
            "question_id": None
        },
        "round_results": [],
        "admin": admin_sid,
        "time_limit": 10,
        "players": []
    }

def add_player_to_room(room_id, sid, user_name, user_uuid):
    rooms[room_id]["players"].append({
        "sid": sid,
        "username": user_name,
        "uuid": user_uuid,
        "score": 0,
        "questions": []
    })

def get_room_id_by_sid(sid):
    # Get all rooms
    user_rooms = sio.rooms(sid)

    # Compare room list with user rooms
    for room_key in user_rooms:
        if room_key in rooms:
            return room_key
        
    return None

def find_answer_by_id(answers_list, answer_id):
    for answer in answers_list:
        if answer["answer_id"] == answer_id:
            return answer
    return None

def update_player_score(room_id, player_sid, question_id, answer_id, is_correct):
    for player in rooms[room_id]["players"]:
        if player["sid"] == player_sid:
            print(player)
            
            player["score"] += 1 if is_correct else 0
            player["correct_answers"] += 1 if is_correct else 0
            player["questions"].append({
                "question_id": question_id,
                "answer_id": answer_id,
                "correct": is_correct
            })

            # Update round results
            rooms[room_id]["round_results"].append({
                "username": player["username"],
                "score": player["score"],
                "is_correct": is_correct
            })
            
            break

def get_player_by_sid(sid):
    for room in rooms.values():
        for player in room["players"]:
            if player["sid"] == sid:
                return player
    return None

def update_non_guessed_players(room_id):
    current_question_id = rooms[room_id]["current_question"]["question_id"]
    
    for player in rooms[room_id]["players"]:
        has_guessed = False
        
        for question in player["questions"]:
            if question["question_id"] == current_question_id:
                has_guessed = True
                break
        
        if not has_guessed:
            player["questions"].append({
                "question_id": current_question_id,
                "answer_id": None,
                "correct": False
            })

            rooms[room_id]["round_results"].append({
                "username": player["username"],
                "score": player["score"],
                "is_correct": False
            })