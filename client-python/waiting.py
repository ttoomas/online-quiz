# waiting.py

import tkinter as tk
from tkinter import messagebox


def on_link_click(root, link_name):
    # Funkce pro zobrazení čekací obrazovky
    for widget in root.winfo_children():
        widget.grid_forget()

    # Zobrazí nadpis pro čekání
    tk.Label(root, text="Čekání na uživatele", font=("Arial", 16, "bold")).grid(row=0, column=0, pady=20)

    # Seznam uživatelů
    users = ["pepa", "pavel", "pepik"]
    
    # Vypsání seznamu uživatelů
    users_listbox = tk.Listbox(root, height=10, width=40)
    for user in users:
        users_listbox.insert(tk.END, user)
    users_listbox.grid(row=1, column=0, pady=10)

    # Tlačítko pro start kvízu
    def start_quiz():
        messagebox.showinfo("Start kvízu", "Kvíz začíná!")

    tk.Button(root, text="Start", command=start_quiz, font=("Arial", 14), bg="green", fg="white").grid(row=2, column=0, pady=20)

    # Tlačítko pro návrat na hlavní stránku
    tk.Button(root, text="Zpět na hlavní stránku", command=lambda: main_page(root)).grid(row=3, column=0, pady=20)
