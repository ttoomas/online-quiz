import tkinter as tk
from helpers import create_frame


frame = None

def waiting_screen(root, start_quiz_handler):
    global frame
    
    # Frame
    frame_data = create_frame(root, "")
    frame = frame_data["frame"]

    enable_waiting_screen(start_quiz_handler, [])

    def show_frame(quiz_id):
        update_waiting_quiz_id(quiz_id)
        frame_data["show"]()

    return {
        "frame": frame,
        "show": show_frame,
        "hide": frame_data["hide"]
    }

def enable_waiting_screen(start_quiz_handler, user_list):
    global frame
    root = frame

    # Funkce pro zobrazení čekací obrazovky
    for widget in root.winfo_children():
        widget.grid_forget()

    # Zobrazí nadpis pro čekání
    tk.Label(root, text="Čekání na uživatele", font=("Arial", 16, "bold")).grid(row=0, column=0, pady=10)

    # Zobrazení id kvízu
    tk.Label(root, text="ID kvízu: 1234-5678-1234-5678", font=("Arial", 12)).grid(row=1, column=0, pady=20)

    # Vypsání seznamu uživatelů
    users_listbox = tk.Listbox(root, height=10, width=40)
    for user in user_list:
        users_listbox.insert(tk.END, user)
    users_listbox.grid(row=2, column=0, pady=10)

    # Tlačítko pro start kvízu
    tk.Button(root, text="Start", command=start_quiz_handler, font=("Arial", 14), bg="green", fg="white").grid(row=3, column=0, pady=20)

def update_waiting_quiz_id(quiz_id):
    global frame
    root = frame

    # Update quiz id
    quiz_id_label = root.winfo_children()[1]
    quiz_id_label["text"] = f"ID kvízu: {quiz_id}"
    root.update()

def update_waiting_players(user_list):
    global frame
    root = frame

    # Update user list
    users_listbox = root.winfo_children()[2]
    users_listbox.delete(0, tk.END)
    for user in user_list:
        users_listbox.insert(tk.END, user)
    root.update()