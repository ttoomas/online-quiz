import tkinter as tk
from tkinter import messagebox
from ui_elements import on_link_click
from create_quiz import create_quiz




def main_page(root, quizes):
    # Hlavní stránka
    for widget in root.winfo_children():
        widget.grid_forget()

    # Hlavní titul
    title_label = tk.Label(root, text="Výběr kvízu", font=("Arial", 32, "bold"))
    title_label.grid(row=0, column=0, columnspan=5, pady=20)

    quiz_button = tk.Button(root, text="Vytvořit kvíz", command=lambda: create_quiz(root), bg="black", fg="white", font=("Arial", 12, "bold"))
    quiz_button.grid(row=0, column=5, padx=10, pady=20)

    for index, quiz in enumerate(quizes):
        row = 1 + (index // 2)
        column = 1 if index % 2 == 0 else 3

        # Rámeček pro kvíz
        frame = tk.Frame(root, bd=2, relief="solid", padx=10, pady=10)
        frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

        label_title = tk.Label(frame, text=quiz["title"], font=("Arial", 14, "bold"))
        label_title.pack(anchor="center")

        link_button = tk.Button(frame, text=f"Klikněte na odkaz {index + 1}", fg="white", bg="black", bd=0, font=("Arial", 12),
                                command=lambda q=quiz: on_link_click(root, q["id"]))  # Opraveno volání funkce
        link_button.pack(side="bottom", anchor="center", pady=10)

        # Nastavení rozvržení pro lepší přizpůsobení velikosti obrazovky
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)
    root.grid_columnconfigure(2, weight=1)
    root.grid_columnconfigure(3, weight=3)
    root.grid_columnconfigure(4, weight=1)
    root.grid_columnconfigure(5, weight=1)