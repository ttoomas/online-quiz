from db.connect_db import get_cursor

QUIZ_LIST = None

def get_quiz_list():
    global QUIZ_LIST

    if QUIZ_LIST is None:
        QUIZ_LIST = get_quiz_list_db()

    return QUIZ_LIST

def get_quiz_list_db():
    cursor = get_cursor()

    cursor.execute("SELECT quiz_name, uid FROM quizzes")
    quizzes = cursor.fetchall()

    quiz_data = []
    for quiz in quizzes:
        quiz_name = quiz[0]
        uid = quiz[1]
 
        if isinstance(quiz_name, bytearray):
            quiz_name = quiz_name.decode('utf-8')

        quiz_data.append({
            "name": quiz_name,  
            "uuid": uid              
        })

    return quiz_data

def add_quiz_to_list(name, uuid):
    global QUIZ_LIST

    if QUIZ_LIST is None:
        QUIZ_LIST = get_quiz_list_db()

    QUIZ_LIST.append({
        "name": name,
        "uuid": uuid
    })


# EXAMPLE DATA
test_quiz_list = [
    {
        "name": "Kvíz 1",
        "uuid": "1020",
    },
    {
        
        "name": "Kvíz 2",
        "uuid": "3040",
    }
]