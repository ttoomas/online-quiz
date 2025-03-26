import tkinter as tk
from helpers import create_frame


frame = None

def waiting_screen(root, start_quiz_handler):
    global frame
    
    # Frame
    frame_data = create_frame(root, "")
    frame = frame_data["frame"]

    enable_waiting_screen(start_quiz_handler, [])

    return {
        "frame": frame,
        "show": frame_data["show"],
        "hide": frame_data["hide"]
    }

def enable_waiting_screen(start_quiz_handler, user_list):
    global frame
    root = frame

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

def update_waiting_players(user_list):
    global frame
    root = frame

    # Update user list
    users_listbox = root.winfo_children()[1]
    users_listbox.delete(0, tk.END)
    for user in user_list:
        users_listbox.insert(tk.END, user)
    
    root.update()