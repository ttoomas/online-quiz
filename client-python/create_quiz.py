import tkinter as tk
from tkinter import messagebox


def create_quiz(root):
    for widget in root.winfo_children():
        widget.grid_forget()

    # Vytvoření canvasu pro scrollování
    canvas = tk.Canvas(root)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas)

    # Bindování pro scrollování
    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    window = canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Umístění canvasu na pravou stranu a scrollbar také na pravou stranu
    canvas.grid(row=0, column=1, sticky="nsew", padx=(800, 20))
    scrollbar.grid(row=0, column=2, sticky="ns")

    # Nastavení rozvržení pro správné přizpůsobení
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=0)
    root.grid_columnconfigure(1, weight=3)
    root.grid_columnconfigure(2, weight=0)

    # Hlavní nadpis pro zadání názvu kvízu
    tk.Label(scroll_frame, text="Zadejte název kvízu", font=("Arial", 14)).pack(pady=10)
    quiz_title_entry = tk.Entry(scroll_frame, font=("Arial", 12), width=40)
    quiz_title_entry.pack(pady=10)

    def create_question_section():
        # Vytvoření sekce pro otázky
        question_index = len(scroll_frame.winfo_children()) // 2
        question_label = tk.Label(scroll_frame, text=f"Otázka {question_index}", font=("Arial", 14))
        question_label.pack(pady=10)
        question_entry = tk.Entry(scroll_frame, font=("Arial", 12), width=40)
        question_entry.pack(pady=10)

        answer_frame = tk.Frame(scroll_frame)
        answer_frame.pack(pady=5)

        def add_answer():
            # Funkce pro přidání odpovědí
            answer_index = len(answer_frame.winfo_children()) + 1
            frame = tk.Frame(answer_frame)
            frame.pack(pady=2)

            tk.Label(frame, text=f"Odpověď {answer_index}").pack(side="left")
            answer_entry = tk.Entry(frame, width=30)
            answer_entry.pack(side="left", padx=5)

            def mark_correct():
                answer_entry.config(bg="lightgreen")
            def mark_incorrect():
                answer_entry.config(bg="lightcoral")

            # Tlačítka pro označení správnosti odpovědi
            tk.Button(frame, text="Správná", bg="green", fg="white", command=mark_correct).pack(side="left", padx=2)
            tk.Button(frame, text="Špatná", bg="red", fg="white", command=mark_incorrect).pack(side="left", padx=2)

        # Předdefinované odpovědi
        for _ in range(2):
            add_answer()

        # Tlačítko pro přidání další odpovědi
        tk.Button(scroll_frame, text="Přidat odpověď", command=add_answer).pack(pady=(10, 100))

    # Tlačítko pro přidání nové otázky
    tk.Button(scroll_frame, text="Vytvořit novou otázku", command=create_question_section).pack(pady=20)

    # Tlačítko pro vytvoření kvízu
    tk.Button(scroll_frame, text="Vytvořit kvíz", command=lambda: messagebox.showinfo("Info", "Kvíz vytvořen")).pack(side="bottom", pady=75)
