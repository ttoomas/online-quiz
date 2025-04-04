import tkinter as tk
from helpers import create_frame


frame = None
frame_data = None

def guessing_room(root):
    global frame
    global frame_data
    
    # Frame
    frame_data = create_frame(root, "")
    frame = frame_data["frame"]
    show_frame = frame_data["show"]
    hide_frame = frame_data["hide"]

    activate_guessing_room()

    return {
        "frame": frame,
        "show": show_frame,
        "hide": hide_frame,
    }

def show_guessing_room():
    global frame_data

    frame_data["show"]()

def activate_guessing_room():
    global frame

    title = tk.Label(frame, text="", font=("Helvetica", 12))
    title.pack(pady=10)

    timer_label = tk.Label(frame, text="Time remaining: 60 seconds", font=("Helvetica", 12))
    timer_label.pack(pady=10)

    listbox = tk.Listbox(frame)
    listbox.pack()


def update_guessing_players(players):
    global frame

    # Remove the listbox
    users_listbox = frame.winfo_children()[2]
    users_listbox.destroy()
    
    # Listbox for players
    listbox = tk.Listbox(frame)
    for player in players:
        listbox.insert(tk.END, player)
    listbox.pack()

def update_guessing_title(title):
    global frame

    # Update the title content
    title_label = frame.winfo_children()[0]
    title_label.config(text=title)

def start_guessing_time(time):
    global frame

    # Update time label
    timer_label = frame.winfo_children()[1]
    timer_label.config(text=f"Time remaining: {time} seconds")

    # Update the timer every second
    current_time = time
    
    def update_timer():
        nonlocal current_time
        if current_time > 0:
            current_time -= 1
            timer_label.config(text=f"Time remaining: {current_time + 1} seconds")
            frame.after(1000, update_timer)
        else:
            timer_label.config(text="Time's up!")
    
    update_timer()