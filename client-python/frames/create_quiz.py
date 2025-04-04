import tkinter as tk
from tkinter import messagebox
from helpers import create_frame
from controllers.default_connect import get_sio

def create_quiz(root, hide_create_quiz_handler):
    # Frame
    frame_data = create_frame(root, "")
    frame = frame_data["frame"]

    activate_create_quiz(frame, hide_create_quiz_handler)

    return frame_data

def activate_create_quiz(root, hide_create_quiz_handler):
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

    questions = []

    def create_question_section():
        # Vytvoření sekce pro otázky
        question_index = len(questions) + 1
        question_label = tk.Label(scroll_frame, text=f"Otázka {question_index}", font=("Arial", 14))
        question_label.pack(pady=10)
        question_entry = tk.Entry(scroll_frame, font=("Arial", 12), width=40)
        question_entry.pack(pady=10)

        answer_frame = tk.Frame(scroll_frame)
        answer_frame.pack(pady=5)

        answers = []

        def add_answer():
            # Funkce pro přidání odpovědí
            answer_index = len(answers) + 1
            frame = tk.Frame(answer_frame)
            frame.pack(pady=2)

            tk.Label(frame, text=f"Odpověď {answer_index}").pack(side="left")
            answer_entry = tk.Entry(frame, width=30)
            answer_entry.pack(side="left", padx=5)

            def mark_correct():
                answer_entry.config(bg="lightgreen")
                answers.append((answer_entry, True))
            def mark_incorrect():
                answer_entry.config(bg="lightcoral")
                answers.append((answer_entry, False))

            # Tlačítka pro označení správnosti odpovědi
            tk.Button(frame, text="Správná", bg="green", fg="white", command=mark_correct).pack(side="left", padx=2)
            tk.Button(frame, text="Špatná", bg="red", fg="white", command=mark_incorrect).pack(side="left", padx=2)

            # Přidání odpovědi do seznamu odpovědí
            answers.append((answer_entry, False))

        # Předdefinované odpovědi
        for _ in range(2):
            add_answer()

        # Tlačítko pro přidání další odpovědi
        tk.Button(scroll_frame, text="Přidat odpověď", command=add_answer).pack(pady=(10, 100))

        questions.append((question_entry, answers))

    # Tlačítko pro přidání nové otázky
    tk.Button(scroll_frame, text="Vytvořit novou otázku", command=create_question_section).pack(pady=20)

    def create_quiz():
        quiz_title = quiz_title_entry.get()
        quiz_data = {"title": quiz_title, "questions": []}

        for question_entry, answers in questions:
            question_text = question_entry.get()
            question_data = {"question": question_text, "answers": []}
            for answer_entry, is_correct in answers:
                answer_text = answer_entry.get()
                question_data["answers"].append({"answer": answer_text, "correct": is_correct})
            quiz_data["questions"].append(question_data)

        emit_create_quiz(quiz_data)
        hide_create_quiz_handler()

    # Tlačítko pro vytvoření kvízu
    tk.Button(scroll_frame, text="Vytvořit kvíz", command=create_quiz).pack(side="bottom", pady=75)


def emit_create_quiz(quiz_data):
    sio = get_sio()
    
    sio.emit("createQuiz", {
        "quiz_data": quiz_data
    }, callback=update_quiz_list)

def update_quiz_list(data):
    new_quiz_name = data["name"]
    new_quiz_uuid = data["uuid"]