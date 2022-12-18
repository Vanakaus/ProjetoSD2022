
import comunicacao as com
import tkinter as tk
from random import shuffle

window = tk.Tk()
bg_janela = "#00c8ff"
bg_quadro = "#fefefe"
bg_carta = "#e8c999"
pontos = 0
listPlayers = ''
lbl_pontuacao2 = tk.Label()
lbl_listPlayers = tk.Label()
cartas = [[0 for x in range(6)] for x in range(6)]
controleCartas = [0 for x in range(36)]


def janela():
    window.title("Jogo da Memória")
    window.geometry("800x500")
    window.configure(bg=bg_janela)
    window.resizable(False, False)
    window.iconbitmap("src/icons/play.ico")

    lbl_titulo = tk.Label(window, text="Jogo da Memoria", bg=bg_janela, font=("Arial", 32))
    lbl_titulo.place(x=220, y = 30)

def pontuacao():
    quadro = tk.Frame(window, width=200, height=80, bg=bg_quadro)
    quadro.place(x=20, y=100)

    lbl_pontuacao = tk.Label(quadro, text="Sua Pontuação:", bg=bg_quadro, font=("arial", 20))
    lbl_pontuacao.place(x=0, y=0)
    global lbl_pontuacao2
    lbl_pontuacao2 = tk.Label(quadro, text=pontos, bg=bg_quadro, font=("arial", 20))
    lbl_pontuacao2.place(x=5, y=30)

def players():
    quadro2 = tk.Frame(window, width=200, height=280, bg=bg_quadro)
    quadro2.place(x=20, y=200)

    lbl_players = tk.Label(quadro2, text="Jogadores", bg=bg_quadro, font=("arial", 22))
    lbl_players.place(x=20, y=0)

    global lbl_listplayers
    lbl_listPlayers = tk.Label(quadro2, text="João Vitor: 8 \nVinicius: 5", bg=bg_quadro, font=("arial", 18), justify="left")
    lbl_listPlayers.place(x=5, y=50)

def mesa():
    mesa = tk.Frame(window, width=500, height=380, bg=bg_quadro)
    mesa.place(x=250, y=100)
    mesa2 = tk.Frame(mesa, bg=bg_quadro, width=500, height=380)
    mesa2.place(x=75, y=7)
    for i in range(6):
        for j in range(6):
            cartas[i][j] = tk.Button(mesa2, width=4, height=2, cursor="hand2", bg=bg_carta, activebackground=bg_carta, command=lambda x1=i, y1=j: Escolher(x1,y1))
            cartas[i][j].grid(column=j, row=i, padx=12, pady=10)

def Escolher(y, x):
    print("Carta [{}][{}] escolhida".format(x, y))

    com.canal.basic_publish(exchange='', routing_key='com_jogador', body="carta {} {}".format(x, y))


def main():
    janela()
    pontuacao()
    players()
    mesa()

    window.mainloop()