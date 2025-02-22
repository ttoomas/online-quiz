import tkinter as tk
from frames.create_quiz import create_quiz
from frames.show_quiz import show_quiz
from frames.waiting import waiting_screen

root = tk.Tk()
# root.geometry("1920x1080")

quiz_list = [
    { "id": 1, "title": "Kvíz 1" },
]
user_list = ["pepa", "karel"]

# HANDLERS
def create_quiz_handler():
    show_quiz_actions["hide"]()
    create_quiz_actions["show"]()

def show_waiting_handler(quiz_id):
    show_quiz_actions["hide"]()
    waiting_actions["show"](user_list)

def start_quiz_handler():
    waiting_actions["hide"]()
    print("Starting quiz")

# FRAME ACTIONS
show_quiz_actions = show_quiz(root, create_quiz_handler, show_waiting_handler)
create_quiz_actions = create_quiz(root)
waiting_actions = waiting_screen(root, start_quiz_handler)


# Default page
show_quiz_actions["show"](quiz_list)

root.mainloop()