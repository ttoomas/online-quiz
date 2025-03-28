import tkinter as tk
from helpers import create_frame

def guessing_room(root):
    # Frame
    frame_data = create_frame(root, "")
    frame = frame_data["frame"]
    show_frame = frame_data["show"]
    hide_frame = frame_data["hide"]

    # Activate the guessing room, which includes the UI components like players and countdown
    activate_guessing_room(frame)

    # Function to update the list of players in the guessing room
    def update_frame(players):
        update_guessing_players(frame, players)

    return {
        "frame": frame,
        "show": show_frame,
        "hide": hide_frame,
        "update": update_frame
    }

def update_guessing_players(frame, players):
    # Clearing any previous widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a label showing the players who guessed
    player_label = tk.Label(frame, text="Players who have guessed: " + ", ".join(players))
    player_label.pack(pady=10)

    # Example of how the list might appear (in a Listbox for example)
    listbox = tk.Listbox(frame)
    for player in players:
        listbox.insert(tk.END, player)
    listbox.pack()

def activate_guessing_room(frame):
    # Header Label (room title)
    header_label = tk.Label(frame, text="Guessing Room", font=("Helvetica", 16))
    header_label.pack(pady=10)

    # Players who have already guessed (initially empty list)
    initial_players = []
    update_guessing_players(frame, initial_players)

    # Timer label
    timer_label = tk.Label(frame, text="Time remaining: 60 seconds", font=("Helvetica", 12))
    timer_label.pack(pady=10)

    # Simulate a countdown
    countdown_time = 60  # 1 minute countdown
    def update_timer():
        nonlocal countdown_time
        if countdown_time > 0:
            countdown_time -= 1
            timer_label.config(text=f"Time remaining: {countdown_time} seconds")
            frame.after(1000, update_timer)  # Call every 1000ms (1 second)
        else:
            timer_label.config(text="Time's up!")

    # Start the countdown
    update_timer()
