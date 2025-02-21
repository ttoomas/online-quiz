import tkinter as tk
from tkinter import messagebox
from show_quiz import main_page
from hide_page import empty_page
from hide_page import hide_main_page

# pro testování, potom to čapneš z db
quizes = [
    {"title": "Kvíz jedna", "desc": "popis", "id": "ksdljflūkajkfsd"},
    {"title": "Kvíz asdf", "desc": "asdf", "id": "asdf"},
    {"title": "Kvíz tři", "desc": "nový popis", "id": "novy_id"},
    
    {"title": "Kvíz tři", "desc": "nový popis", "id": "novy_id"},
]

root = tk.Tk()
root.title("Moje aplikace")
root.geometry("1920x1080")

#empty_page(root)
main_page(root, quizes)
#hide_main_page(root)
root.mainloop()