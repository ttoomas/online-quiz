import tkinter as tk
from helpers import create_frame


frame = None
hide_guessing_room = None

def round_results(root, next_round_handler, hide_guessing_room_handler):
    global frame
    global hide_guessing_room

    hide_guessing_room = hide_guessing_room_handler
    
    # Frame
    frame_data = create_frame(root, "")
    frame = frame_data["frame"]
    show_frame = frame_data["show"]
    hide_frame = frame_data["hide"]

    activate_round_results(next_round_handler)

    return {
        "frame": frame,
        "show": show_frame,
        "hide": hide_frame
    }

def activate_round_results(next_round_handler):
    global frame
    
    for widget in frame.winfo_children():
        widget.destroy()

    title_label = tk.Label(frame, text="Round Results", font=("Helvetica", 16))
    title_label.pack(pady=10)

    results_label = tk.Label(frame, text="Results: ", font=("Helvetica", 12))
    results_label.pack(pady=5)

    results_listbox = tk.Listbox(frame)
    results_listbox.pack(pady=10)

    next_round_button = tk.Button(frame, text="Start Next Round", command=next_round_handler)
    next_round_button.pack(pady=20)

def show_round_results(results):
    global frame
    global hide_guessing_room

    hide_guessing_room()

    # Show the frame
    frame.grid()
    
    # Remove the results listbox
    results_listbox = frame.winfo_children()[2]
    results_listbox.delete(0, tk.END)

    # Add the new results
    for result in results:
        results_listbox.insert(tk.END, f"{result['username']} - {result['score']} points")