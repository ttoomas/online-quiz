import tkinter as tk
from controllers.default_connect import default_connect, close_connection, create_room_request

from frames.home_frame import home_frame
from frames.create_quiz import create_quiz
from frames.waiting_room import waiting_screen
from frames.guessing_room import guessing_room
from frames.round_results import round_results
from frames.round_results import activate_round_results


default_connect()

root = tk.Tk()
# root.geometry("1920x1080")

user_list = ["pepa", "karel"]


quiz_list = [
    {
        "name": "Kvíz 1",
        "uuid": "1234-5678-1234-5678",
    },
    {
        
        "name": "Kvíz 2",
        "uuid": "1234-5678-56456-5678",
    }
]

# HANDLERS
def create_quiz_handler():
    home_frame_actions["hide"]()
    create_quiz_actions["show"]()

def show_waiting_handler(quiz_id):
    create_room_request(quiz_id)
    home_frame_actions["hide"]()
    waiting_actions["show"]()

def start_quiz_handler():
    waiting_actions["hide"]()
    guessing_actions["show"]()

def show_results_handler():
    # After the guessing round, show the results
    guessing_actions["hide"]()  # Hide the guessing room
    results_actions["show"]([
        { "user": "pepa", "points": 10 },
        { "user": "karel", "points": 5 }
    ])  # Pass the results to show them

# FRAME ACTIONS
home_frame_actions = home_frame(root, create_quiz_handler, show_waiting_handler)
create_quiz_actions = create_quiz(root)
waiting_actions = waiting_screen(root, start_quiz_handler)
guessing_actions = guessing_room(root)
results_actions = round_results(root)

# Uzavření spojení
def closeWindow():
    close_connection()
    root.destroy()


# Default page
home_frame_actions["show"](quiz_list)
root.protocol("WM_DELETE_WINDOW", closeWindow)

# Spuštění hlavní smyčky aplikace
root.mainloop()