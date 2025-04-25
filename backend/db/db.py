import mysql.connector
import uuid
import json

def import_quiz(file_path):
    with open(file_path, 'r') as file:
        quiz_data = json.load(file)

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kviz"
    )

    cursor = db.cursor()

    quiz_uid = str(uuid.uuid4())

    cursor.execute(
        "INSERT INTO quizzes (quiz_name, uid) VALUES (%s, %s)", 
        (quiz_data["quizName"], quiz_uid)
    )
    db.commit()
    quiz_id = cursor.lastrowid

    for question in quiz_data["questions"]:
        question_uid = str(uuid.uuid4())

        cursor.execute(
            "INSERT INTO questions (question, quiz_id, uid) VALUES (%s, %s, %s)",
            (question["question"], quiz_id, question_uid)
        )
        db.commit()
        question_id = cursor.lastrowid

        for answer in question["answers"]:
            answer_uid = str(uuid.uuid4())

            cursor.execute(
                "INSERT INTO answers (answer, correct, question_id, uid) VALUES (%s, %s, %s, %s)",
                (answer["answer"], answer["correct"], question_id, answer_uid)
            )
            db.commit()


def convert_to_serializable(data):
    if isinstance(data, (bytearray, bytes)):
        return data.decode("utf-8")
    return data

def export_everything_by_uid(uid, db_config, output_file):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT id, quiz_name FROM quizzes WHERE uid = %s", (uid,))
    quiz = cursor.fetchone()
    if not quiz:
        print("Quiz not found")
        return
    
    quiz_id = quiz['id']
    result = {
        "quizName": convert_to_serializable(quiz['quiz_name']),
        "uid": convert_to_serializable(uid),
        "questions": []
    }
    
    cursor.execute("SELECT id, question, uid FROM questions WHERE quiz_id = %s", (quiz_id,))
    questions = cursor.fetchall()
    
    for q in questions:
        question_data = {
            "question": convert_to_serializable(q['question']),
            "uid": convert_to_serializable(q['uid']),
            "answers": []
        }
        
        cursor.execute("SELECT answer, correct, uid FROM answers WHERE question_id = %s", (q['id'],))
        answers = cursor.fetchall()
        
        for a in answers:
            question_data["answers"].append({
                "answer": convert_to_serializable(a['answer']),
                "correct": bool(a['correct']),
                "uid": convert_to_serializable(a['uid'])
            })
        
        result["questions"].append(question_data)
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    
    cursor.close()
    conn.close()


def export_quiz_names_and_uids(db_config, file_name):
    conn = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )
    cursor = conn.cursor()

    
    cursor.execute("SELECT quiz_name, uid FROM quizzes")
    quizzes = cursor.fetchall()

    
    quiz_data = []
    for quiz in quizzes:
        quiz_name = quiz[0]
        uid = quiz[1]

 
        if isinstance(quiz_name, bytearray):
            quiz_name = quiz_name.decode('utf-8')

        quiz_data.append({
            "quizName": quiz_name,  
            "uid": uid              
        })

    conn.close()

    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(quiz_data, json_file, indent=4, ensure_ascii=False)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'kviz'
}


#import_quiz("quiz_data.json")
#export_quiz_names_and_uids(db_config, 'quiz_names_and_uids.json')
#export_everything_by_uid("40b83b65-ff96-496e-9f58-86a8e81d8672", db_config, "export_everything_by_uid.json")