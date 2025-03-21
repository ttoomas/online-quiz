import tkinter as tk
from helpers import create_frame


def round_results(root):
    # Frame
    frame_data = create_frame(root, "")
    frame = frame_data["frame"]
    show_frame = frame_data["show"]
    hide_frame = frame_data["hide"]

    def show(results):
        show_frame()  # Show the frame when results are ready
        activate_round_results(frame, results)  # Update the frame with results

    return {
        "frame": frame,
        "show": show,
        "hide": hide_frame
    }

def activate_round_results(frame, results):
    """
    This function is responsible for displaying the round results.
    It takes the results (a list of dictionaries with user names and their points) 
    and displays them in the frame.
    """
    # Clear any existing widgets before updating the frame with new results
    for widget in frame.winfo_children():
        widget.destroy()

    # Label for displaying the round result title
    title_label = tk.Label(frame, text="Round Results", font=("Helvetica", 16))
    title_label.pack(pady=10)

    # Create a listbox or labels to show players and their points
    results_label = tk.Label(frame, text="Results: ", font=("Helvetica", 12))
    results_label.pack(pady=5)

    # Create a Listbox to display the results
    results_listbox = tk.Listbox(frame)
    for result in results:
        # Insert player and points as a formatted string
        results_listbox.insert(tk.END, f"{result['user']}: {result['points']} points")
    results_listbox.pack(pady=10)

    # Button to go to the next round
    next_round_button = tk.Button(frame, text="Start Next Round", command=start_next_round)
    next_round_button.pack(pady=20)

def start_next_round():
    """
    This function will handle the logic to move to the next round.
    For now, it just prints a message.
    You can extend this function to reset the game state or transition to a new screen.
    """
    print("Starting the next round!")
    # You can add logic here to transition to the next round, reset states, etc.
