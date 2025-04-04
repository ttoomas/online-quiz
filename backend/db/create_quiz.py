import uuid
from db.connect_db import get_cursor, get_db

def create_quiz(quiz_data):
    db = get_db()
    cursor = get_cursor()

    quiz_uid = str(uuid.uuid4())

    cursor.execute(
        "INSERT INTO quizzes (quiz_name, uid) VALUES (%s, %s)", 
        (quiz_data["title"], quiz_uid)
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

    return {
        "name": quiz_data["title"],
        "uuid": quiz_uid,
    }