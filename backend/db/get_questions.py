quiz_questions = [
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
    }
]


def get_quiz_questions():
    # TODO - Get questions from DB
    # TODO - Also save it into dict, so we can use it in the show_answer function
    return quiz_questions