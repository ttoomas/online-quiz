from tkinter import LabelFrame

def create_frame(root, title):
    frame = LabelFrame(
        root,
        text=title,
        padx=15,
        pady=15
    )

    frame.grid(row=0, column=1)

    hide_labelframe(frame)

    return {
        "frame": frame,
        "hide": lambda: hide_labelframe(frame),
        "show": lambda: show_labelframe(frame)
    }

def destroy_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


# UTILS
def hide_labelframe(frame):
    frame.grid_remove()

def show_labelframe(frame):
    frame.grid()