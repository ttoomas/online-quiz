import tkinter as tk
from tkinter import messagebox
from socketConnect import defaultConnect, closeConnection, createQuiz

defaultConnect()

# Data o kvízech
quizes = [
    {"title": "Kvíz jedna", "desc": "popis", "id": "id-123"},
]
 
# Funkce, která se spustí při kliknutí na tlačítko ve formě odkazu
def on_link_click(link_name):
    messagebox.showinfo("Odkaz kliknut", f"Klikli jste na odkaz: {link_name}")
 
# Funkce pro vytvoření kvízu (pro testovací účely)
def create_quiz():
    messagebox.showinfo("Vytvoření kvízu", "Kvíz byl vytvořen!")
 
# Vytvoření hlavního okna
root = tk.Tk()
root.title("Moje aplikace")
root.geometry("500x500")  # Nastavení velikosti okna
 
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
                            command=lambda q=quiz: createQuiz(q["id"]))
    link_button.pack(side="bottom", anchor="center", pady=10)
 
# Nastavení flexibilní šířky sloupců
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=3)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)
 
 
# Uzavření spojení
def closeWindow():
    closeConnection()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", closeWindow)

# Spuštění hlavní smyčky aplikace
root.mainloop()