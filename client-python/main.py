import tkinter as tk
from controllers.default_connect import default_connect, close_connection, create_room_request
from controllers.questions import start_questions

from frames.home_frame import home_frame
from frames.create_quiz import create_quiz
from frames.waiting_room import waiting_screen
from frames.guessing_room import guessing_room
from frames.round_results import round_results
from frames.round_results import activate_round_results



root = tk.Tk()
# root.geometry("1920x1080")


# HANDLERS
def create_quiz_handler():
    home_frame_actions["hide"]()
    create_quiz_actions["show"]()

def show_waiting_handler(quiz_id):
    create_room_request(quiz_id)
    home_frame_actions["hide"]()
    waiting_actions["show"](quiz_id)

def start_quiz_handler():
    start_questions()
    waiting_actions["hide"]()
    guessing_actions["show"]()

# def show_results_handler():
#     guessing_actions["hide"]()
#     results_actions["show"]([
#         { "user": "pepa", "points": 10 },
#         { "user": "karel", "points": 5 }
#     ])

# FRAME ACTIONS
home_frame_actions = home_frame(root, create_quiz_handler, show_waiting_handler)
create_quiz_actions = create_quiz(root)
waiting_actions = waiting_screen(root, start_quiz_handler)
guessing_actions = guessing_room(root)
results_actions = round_results(root)

# Close window and connection
def closeWindow():
    close_connection()
    root.destroy()


# Default page
home_frame_actions["show"]()
root.protocol("WM_DELETE_WINDOW", closeWindow)

default_connect()


root.mainloop()