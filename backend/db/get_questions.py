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
    {
        "question": "Who painted the Mona Lisa?",
        "question_id": "3",
        "answers": [
            {
                "answer": "Leonardo da Vinci",
                "answer_id": "9",
                "correct": True
            },
            {
                "answer": "Pablo Picasso",
                "answer_id": "10",
                "correct": False
            },
            {
                "answer": "Vincent van Gogh",
                "answer_id": "11",
                "correct": False
            },
            {
                "answer": "Michelangelo",
                "answer_id": "12",
                "correct": False
            }
        ]
    }
]


def get_quiz_questions():
    # TODO - Get questions from DB
    # TODO - Also save it into dict, so we can use it in the show_answer function
    return quiz_questions