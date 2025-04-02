from helpers.room_helper import rooms, get_player_by_sid
from db.get_questions import get_quiz_questions

def get_questions_data(room_id):
    questions = get_quiz_questions()
    number_of_questions = len(questions)
    current_question_index = rooms[room_id]["current_question"]["index"]
    current_question_id = questions[current_question_index]["question_id"]
    time_limit = rooms[room_id]["time_limit"]
    
    data = {
        "title": questions[current_question_index]["question"],
        "answers_list": questions[current_question_index]["answers"],
        "number_of_questions": number_of_questions,
        "current_question": current_question_index + 1,
        "question_id": current_question_id,
        "time": time_limit,
        "questions": questions
    }
    
    return data

def get_round_result_usernames(room_id):
    player_usernames = []
    
    for player in rooms[room_id]["round_results"]:
        player_usernames.append(player["username"])
    
    return player_usernames

def question_answers_result(room_id, player_sid):
    player = get_player_by_sid(player_sid)
    questions_data = get_questions_data(room_id)
    result = []

    # Find player answer
    player_answer = None
    for answer in player["questions"]:
        if answer["question_id"] == questions_data["question_id"]:
            player_answer = answer
            break

    # Check
    for answer in questions_data["answers_list"]:
        is_correct = None
        if answer["correct"]:
            is_correct = True
        elif player_answer["answer_id"] == answer["answer_id"]:
            is_correct = False
        
        result.append({
            "answer": answer["answer"],
            "is_correct": is_correct
        })
        
    return result

def get_total_quiz_results(room_id):
    results = []

    # Check
    for player in rooms[room_id]["players"]:
        results.append({
            "position": -1,
            "username": player["username"],
            "score": player["score"],
        })
    
    # Update positions
    results.sort(key=lambda x: x["score"], reverse=True)
    for i, player in enumerate(results):
        player["position"] = i + 1
    
    return results