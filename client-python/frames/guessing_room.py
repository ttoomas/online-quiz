import tkinter as tk
from helpers import create_frame

def guessing_room(root):
    # Frame
    frame_data = create_frame(root, "")
    frame = frame_data["frame"]
    show_frame = frame_data["show"]
    hide_frame = frame_data["hide"]

    activate_guessing_room(frame)

    def update_frame(players):
        update_quessing_players(root, players)

    return {
        "frame": frame,
        "show": show_frame,
        "hide": hide_frame,
        "update": update_frame
    }

def update_quessing_players(root, players):
    # DEV ONLY
    players = ["pepa", "karel"]

    # pokud se zavola tato funkce, upravi se seznam hracu, kteri se zobrazuji (vybrali nejakou odpoved)

def activate_guessing_room(root):
    pass

    # bude tam nadpis, seznam hracu kteri uz hadali a cas, ktery se bude sam odcitat (napr. 1 minutu)