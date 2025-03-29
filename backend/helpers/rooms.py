from helpers.socketio import sio

"""
rooms dictionary structure:
{
    "room_id": {
        "status": "waiting" / "answering" / "showing_answer",
        "current_question": 0,
        "admin": "admin_sid",
        "players": [
            {
                "sid": "player_sid",
                "username": "player_username",
                "uuid": "player_uuid",
                "score": 0,
                "questions": [
                    {
                        "question_id": "question_id",
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
        if answer["id_question"] == answer_id:
            return answer
    return None

def update_player_score(room_id, player_sid, answer_id, is_correct):
    for player in rooms[room_id]["players"]:
        if player["sid"] == player_sid:
            player["score"] += 1 if is_correct else 0
            player["questions"].append({
                "question_id": answer_id,
                "correct": is_correct
            })
            
            break