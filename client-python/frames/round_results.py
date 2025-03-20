import tkinter as tk
from helpers import create_frame


def round_results(root):
    # Frame
    frame_data = create_frame(root, "")
    frame = frame_data["frame"]
    show_frame = frame_data["show"]
    hide_frame = frame_data["hide"]

    def show(results):
        show_frame()
        activate_round_results(frame, results)


    return {
        "frame": frame,
        "show": show,
        "hide": hide_frame
    }

def activate_round_results(root, results):
    # DEV ONLY
    results = [
        {
            "user": "pepa",
            "points": 10
        },
        {
            "user": "karel",
            "points": 5
        }
    ]

    # vysledky jednoho kola
    # zobrazi se vysledky + button pro zapnuti dalsiho kola