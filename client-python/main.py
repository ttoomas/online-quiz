import tkinter as tk

from frames.home_frame import home_frame
from frames.create_quiz import create_quiz
from frames.waiting_room import waiting_screen
from frames.guessing_room import guessing_room
from frames.round_results import round_results
from frames.round_results import activate_round_results



root = tk.Tk()
root.geometry("1920x1080")

quiz_list = [
    { "id": 1, "title": "Kvíz 1" },
]
user_list = ["pepa", "karel"]

# HANDLERS
def create_quiz_handler():
    home_frame_actions["hide"]()
    create_quiz_actions["show"]()

def show_waiting_handler(quiz_id):
    home_frame_actions["hide"]()
    waiting_actions["show"](user_list)

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

# Add a button or other way to trigger results after the guessing room is complete
# For the sake of this example, we can simulate the transition after some time
root.after(60000, show_results_handler)  # After 3 seconds, show the results

#Default page
home_frame_actions["show"](quiz_list)

# Simulate showing the guessing room and updating players
#guessing_actions["show"]()
#guessing_actions["update"](["player1", "player2", "player3"])

root.mainloop()

