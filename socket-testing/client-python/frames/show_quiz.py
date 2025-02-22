import tkinter as tk
from helpers import create_frame


def show_quiz(root, create_quiz_handler, show_waiting_handler):
    # Frame
    frame_data = create_frame(root, "")
    frame = frame_data["frame"]
    show_frame = frame_data["show"]
    hide_frame = frame_data["hide"]

    def show(quiz_list):
        show_frame()
        activate_show_quiz(frame, create_quiz_handler, show_waiting_handler, quiz_list)


    return {
        "frame": frame,
        "show": show,
        "hide": hide_frame
    }

def activate_show_quiz(root, create_quiz_handler, show_waiting_handler, quiz_list):
    # Clear existing widgets
    # IMPORTANT, DO NOT REMOVE (DŮLEŽITÉ, NEODSTRAŇUJTE)
    for widget in root.winfo_children():
        widget.grid_forget()
    
    # Hlavní stránka
    for widget in root.winfo_children():
        widget.grid_forget()

    # Hlavní titul
    title_label = tk.Label(root, text="Výběr kvízu", font=("Arial", 32, "bold"))
    title_label.grid(row=0, column=0, columnspan=5, pady=20)

    quiz_button = tk.Button(root, text="Vytvořit kvíz", command=lambda: create_quiz_handler(), bg="black", fg="white", font=("Arial", 12, "bold"))
    quiz_button.grid(row=0, column=5, padx=10, pady=20)

    for index, quiz in enumerate(quiz_list):
        row = 1 + (index // 2)
        column = 1 if index % 2 == 0 else 3

        # Rámeček pro kvíz
        frame = tk.Frame(root, bd=2, relief="solid", padx=10, pady=10)
        frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

        label_title = tk.Label(frame, text=quiz["title"], font=("Arial", 14, "bold"))
        label_title.pack(anchor="center")

        link_button = tk.Button(frame, text=f"Klikněte na odkaz {index + 1}", fg="white", bg="black", bd=0, font=("Arial", 12),
                                command=lambda q=quiz: show_waiting_handler(q["id"]))  # Opraveno volání funkce
        link_button.pack(side="bottom", anchor="center", pady=10)

        # Nastavení rozvržení pro lepší přizpůsobení velikosti obrazovky
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)
    root.grid_columnconfigure(2, weight=1)
    root.grid_columnconfigure(3, weight=3)
    root.grid_columnconfigure(4, weight=1)
    root.grid_columnconfigure(5, weight=1)