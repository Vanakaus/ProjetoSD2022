import tkinter as tk

def players(window, bg_quadro):
    quadro2 = tk.Frame(window, width=200, height=280, bg=bg_quadro)
    quadro2.place(x=20, y=200)

    lbl_players = tk.Label(quadro2, text="Jogadores", bg=bg_quadro, font=("arial", 22))
    lbl_players.place(x=20, y=0)

    global lbl_listplayers
    lbl_listPlayers = tk.Label(quadro2, text="João Vitor: 8 \nVinicius: 5", bg=bg_quadro, font=("arial", 18), justify="left")
    lbl_listPlayers.place(x=5, y=50)