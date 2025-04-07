import tkinter as tk
from helpers import create_frame


frame = None
hide_guessing_room = None

def quiz_results(root, hide_guessing_room_handler):
    global frame
    global hide_guessing_room

    hide_guessing_room = hide_guessing_room_handler
    
    # Frame
    frame_data = create_frame(root, "")
    frame = frame_data["frame"]
    show_frame = frame_data["show"]
    hide_frame = frame_data["hide"]

    activate_quiz_results()

    return {
        "frame": frame,
        "show": show_frame,
        "hide": hide_frame
    }

def activate_quiz_results():
    global frame
    
    for widget in frame.winfo_children():
        widget.destroy()

    
    title_label = tk.Label(frame, text="Quiz finished!", font=("Helvetica", 16))
    title_label.pack(pady=10)

    results_label = tk.Label(frame, text="Results: ", font=("Helvetica", 12))
    results_label.pack(pady=5)

    results_listbox = tk.Listbox(frame)
    results_listbox.pack(pady=10)

def show_quiz_results(results):
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
        results_listbox.insert(tk.END, f"Position {result['position']}. - {result['username']} - {result['score']} points")
    
    
    # Dynamically adjust the Listbox size
    max_width = max((len(f"Position {result['position']}. - {result['username']} - {result['score']} points") for result in results), default=0)
    results_listbox.config(width=max_width, height=len(results))