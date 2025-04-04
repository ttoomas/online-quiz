from db.connect_db import get_cursor

QUIZ_QUESTION_DICT = {}

def get_quiz_questions(uuid):
    if uuid not in QUIZ_QUESTION_DICT:
        QUIZ_QUESTION_DICT[uuid] = get_quiz_questions_from_db(uuid)
    
    return QUIZ_QUESTION_DICT[uuid]

def get_quiz_questions_from_db(uid):
    cursor = get_cursor()
    
    cursor.execute("SELECT id, quiz_name FROM quizzes WHERE uid = %s", (uid,))
    quiz = cursor.fetchone()
    if not quiz:
        print("Quiz not found")
        return
    
    quiz_id = quiz[0]
    result = []
    
    cursor.execute("SELECT id, question, quiz_id, uid FROM questions WHERE quiz_id = %s", (quiz_id,))
    questions = cursor.fetchall()
    
    for q in questions:
        question_data = {
            "question": convert_to_serializable(q[1]),
            "question_id": convert_to_serializable(q[3]),
            "answers": []
        }
        
        cursor.execute("SELECT answer, correct, uid FROM answers WHERE question_id = %s", (q[2],))
        answers = cursor.fetchall()
        
        for a in answers:
            question_data["answers"].append({
                "answer": convert_to_serializable(a[0]),
                "correct": bool(a[1]),
                "answer_id": convert_to_serializable(a[2])
            })
        
        result.append(question_data)
    
    return result

def convert_to_serializable(data):
    if isinstance(data, (bytearray, bytes)):
        return data.decode("utf-8")
    return data

# EXAMPLE DATA
test_quiz_questions = [
    {
        "question": "What is the capital of France?",
        "question_id": "1",
        "answers": [
            {
                "answer": "Paris",
                "answer_id": "1",
                "correct": True
            },
            {
                "answer": "London",
                "answer_id": "2",
                "correct": False
            },
            {
                "answer": "New York",
                "answer_id": "3",
                "correct": False
            },
            {
                "answer": "Berlin",
                "answer_id": "4",
                "correct": False
            }
        ]
    },
    {
        "question": "What is the largest planet in our solar system?",
        "question_id": "2",
        "answers": [
            {
                "answer": "Jupiter",
                "answer_id": "5",
                "correct": True
            },
            {
                "answer": "Mars",
                "answer_id": "6",
                "correct": False
            },
            {
                "answer": "Saturn",
                "answer_id": "7",
                "correct": False
            },
            {
                "answer": "Venus",
                "answer_id": "8",
                "correct": False
            }
        ]
    },
    # {
    #     "question": "Who painted the Mona Lisa?",
    #     "question_id": "3",
    #     "answers": [
    #         {
    #             "answer": "Leonardo da Vinci",
    #             "answer_id": "9",
    #             "correct": True
    #         },
    #         {
    #             "answer": "Pablo Picasso",
    #             "answer_id": "10",
    #             "correct": False
    #         },
    #         {
    #             "answer": "Vincent van Gogh",
    #             "answer_id": "11",
    #             "correct": False
    #         },
    #         {
    #             "answer": "Michelangelo",
    #             "answer_id": "12",
    #             "correct": False
    #         }
    #     ]
    # }
]
