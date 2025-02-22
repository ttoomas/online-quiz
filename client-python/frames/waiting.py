import tkinter as tk
from helpers import create_frame

def waiting_screen(root, start_quiz_handler):
    # Frame
    frame_data = create_frame(root, "")
    frame = frame_data["frame"]
    show_frame = frame_data["show"]
    hide_frame = frame_data["hide"]

    def show(user_list):
        show_frame()
        activate_waiting_screen(frame, start_quiz_handler, user_list)

    return {
        "frame": frame,
        "show": show,
        "hide": hide_frame
    }

def activate_waiting_screen(root, start_quiz_handler, user_list):
    # Clear existing widgets
    # IMPORTANT, DO NOT REMOVE (DŮLEŽITÉ, NEODSTRAŇUJTE)
    for widget in root.winfo_children():
        widget.grid_forget()
    
    # Funkce pro zobrazení čekací obrazovky
    for widget in root.winfo_children():
        widget.grid_forget()

    # Zobrazí nadpis pro čekání
    tk.Label(root, text="Čekání na uživatele", font=("Arial", 16, "bold")).grid(row=0, column=0, pady=20)

    # Vypsání seznamu uživatelů
    users_listbox = tk.Listbox(root, height=10, width=40)
    for user in user_list:
        users_listbox.insert(tk.END, user)
    users_listbox.grid(row=1, column=0, pady=10)

    # Tlačítko pro start kvízu
    tk.Button(root, text="Start", command=start_quiz_handler, font=("Arial", 14), bg="green", fg="white").grid(row=2, column=0, pady=20)