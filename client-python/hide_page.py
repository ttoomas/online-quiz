def empty_page(root):
    # Čistíme všechny widgety
    for widget in root.winfo_children():
        widget.grid_forget()

    # Nastavíme pozadí na bílou
    root.configure(bg="white")


def hide_main_page(root):
    # Čistíme všechny widgety
    for widget in root.winfo_children():
        widget.grid_forget()

    # Nastavíme pozadí na bílou
    root.configure(bg="white")

