import tkinter as tk
from tkinter import messagebox

# Data o kvízech
quizes = [
    {"title": "Kvíz jedna", "desc": "popis", "id": "ksdljflūkajkfsd"},
    {"title": "Kvíz asdf", "desc": "asdf", "id": "asdf"},
    {"title": "Kvíz tři", "desc": "nový popis", "id": "novy_id"},
]

# Funkce, která se spustí při kliknutí na tlačítko ve formě odkazu
def on_link_click(link_name):
    messagebox.showinfo("Odkaz kliknut", f"Klikli jste na odkaz: {link_name}")

# Funkce pro vytvoření kvízu (zobrazení formuláře pro zadání otázky a odpovědí)
def create_quiz():
    # Smazání stávajícího obsahu
    for widget in root.winfo_children():
        widget.grid_forget()

    # Zobrazení formuláře pro zadání otázky
    question_label = tk.Label(root, text="Zadejte otázku", font=("Arial", 14))
    question_label.grid(row=1, column=0, columnspan=2, pady=10)

    question_entry = tk.Entry(root, font=("Arial", 12), width=40)
    question_entry.grid(row=2, column=0, columnspan=2, pady=10)

    # Rámečky pro zadání odpovědí (na začátku pouze 2 odpovědi)
    answer_labels = ["Odpověď 1", "Odpověď 2"]
    answer_entries = []
    answer_buttons = []

    answers_frame = tk.Frame(root)
    answers_frame.grid(row=3, column=0, columnspan=2, pady=20)

    def create_answer_widgets(i):
        answer_label = tk.Label(answers_frame, text=answer_labels[i], font=("Arial", 12))
        answer_label.grid(row=i, column=0, pady=5, padx=10)

        answer_entry = tk.Entry(answers_frame, font=("Arial", 12), width=40)
        answer_entry.grid(row=i, column=1, pady=5, padx=10)
        answer_entries.append(answer_entry)

        # Tlačítka pro označení správnosti odpovědi
        def mark_correct(entry):
            entry.config(bg="lightgreen")

        def mark_incorrect(entry):
            entry.config(bg="lightcoral")

        correct_button = tk.Button(answers_frame, text="Správná", command=lambda: mark_correct(answer_entry), font=("Arial", 10), bg="green", fg="white")
        correct_button.grid(row=i, column=2, padx=10)

        incorrect_button = tk.Button(answers_frame, text="Špatná", command=lambda: mark_incorrect(answer_entry), font=("Arial", 10), bg="red", fg="white")
        incorrect_button.grid(row=i, column=3, padx=10)

        answer_buttons.append((correct_button, incorrect_button))

    # Vytvoření prvních dvou odpovědí
    for i in range(2):
        create_answer_widgets(i)

    # Tlačítko pro přidání další odpovědi
    def add_answer():
        new_answer_index = len(answer_entries) + 1
        new_answer_label = tk.Label(answers_frame, text=f"Odpověď {new_answer_index}", font=("Arial", 12))
        new_answer_label.grid(row=new_answer_index, column=0, pady=5, padx=10)

        new_answer_entry = tk.Entry(answers_frame, font=("Arial", 12), width=40)
        new_answer_entry.grid(row=new_answer_index, column=1, pady=5, padx=10)
        answer_entries.append(new_answer_entry)

        # Tlačítka pro označení správnosti odpovědi
        def mark_correct(entry):
            entry.config(bg="lightgreen")

        def mark_incorrect(entry):
            entry.config(bg="lightcoral")

        correct_button = tk.Button(answers_frame, text="Správná", command=lambda: mark_correct(new_answer_entry), font=("Arial", 10), bg="green", fg="white")
        correct_button.grid(row=new_answer_index, column=2, padx=10)

        incorrect_button = tk.Button(answers_frame, text="Špatná", command=lambda: mark_incorrect(new_answer_entry), font=("Arial", 10), bg="red", fg="white")
        incorrect_button.grid(row=new_answer_index, column=3, padx=10)

    add_button = tk.Button(root, text="Přidat odpověď", command=add_answer, font=("Arial", 12))
    add_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Tlačítko pro potvrzení kvízu
    submit_button = tk.Button(root, text="Vytvořit kvíz", font=("Arial", 12), command=lambda: submit_quiz(question_entry.get(), [entry.get() for entry in answer_entries]))
    submit_button.grid(row=5, column=0, columnspan=2, pady=20)

# Funkce pro zpracování a odeslání kvízu
def submit_quiz(question, answers):
    if not question or any(not answer for answer in answers):
        messagebox.showwarning("Chyba", "Všechna pole musí být vyplněná!")
    else:
        messagebox.showinfo("Kvíz vytvořen", f"Otázka: {question}\nOdpovědi: {', '.join(answers)}")

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Moje aplikace")
root.geometry("1920x1080")  # Nastavení velikosti okna

# Nadpis "Text"
title_label = tk.Label(root, text="Výběr kvízu", font=("Arial", 32, "bold"))
title_label.grid(row=0, column=0, columnspan=5, pady=20)

# Tlačítko pro vytvoření kvízu
quiz_button = tk.Button(root, text="Vytvořit kvíz", command=create_quiz, bg="black", fg="white", font=("Arial", 12, "bold"))
quiz_button.grid(row=0, column=5, padx=10, pady=20)

# Vykreslení dynamických rámečků pro každý kvíz
for index, quiz in enumerate(quizes):
    row = 1 + (index // 2)
    column = 1 if index % 2 == 0 else 3

    frame = tk.Frame(root, bd=2, relief="solid", padx=10, pady=10)
    frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

    label_title = tk.Label(frame, text=quiz["title"], font=("Arial", 14, "bold"))
    label_title.pack(anchor="center")

    label_desc = tk.Label(frame, text=quiz["desc"], wraplength=380, justify="center")
    label_desc.pack(anchor="center", pady=5)

    link_button = tk.Button(frame, text=f"Klikněte na odkaz {index + 1}", fg="white", bg="black", bd=0, font=("Arial", 12),
                            command=lambda q=quiz: on_link_click(q["id"]))
    link_button.pack(side="bottom", anchor="center", pady=10)

# Nastavení flexibilní šířky sloupců
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=3)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)

# Spuštění hlavní smyčky aplikace
root.mainloop()
