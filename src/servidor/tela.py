
import comunicacao as com
import tkinter as tk
from random import shuffle

window = tk.Tk()
bg_janela = "#00c8ff"
bg_quadro = "#fefefe"
bg_carta = "#e8c999"
listPlayers = ['vinicius', 'maria', 'joao']
listPontos = [0, 0, 0]
lbl_listPlayers = tk.Label()

cartas = [[0 for x in range(6)] for x in range(6)]
carta1 = [-1, -1]
carta2 = [-1, -1]
cores = [""] * 18
seq_cores = [""] * 36

cores[0] = "#DD0000"
cores[1] = "#FFA500"
cores[2] = "#FFC0CB"
cores[3] = "#A020F0"
cores[4] = "#3030FF"
cores[5] = "#00FFFF"
cores[6] = "#ADD8E6"
cores[7] = "#FFFF00"
cores[8] = "#00FF00"
cores[9] = "#00AA00"
cores[10] = "#964B00"
cores[11] = "#FFDB58"
cores[12] = "#03bb85"
cores[13] = "#C4A484"
cores[14] = "#FFFFFF"
cores[15] = "#D3D3D3"
cores[16] = "#808080"
cores[17] = "#000000"


def janela():
    window.title("Servidor")
    window.geometry("800x500")
    window.configure(bg=bg_janela)
    window.resizable(False, False)
    window.iconbitmap("src/icons/cartas.ico")

    lbl_titulo = tk.Label(window, text="Servidor\nJogo da Memoria", bg=bg_janela, font=("Arial", 30))
    lbl_titulo.place(x=250, y = 5)

def players():
    quadro = tk.Frame(window, width=200, height=380, bg=bg_quadro)
    quadro.place(x=20, y=100)

    lbl_players = tk.Label(text="Jogadores", bg=bg_quadro, font=("arial", 22))
    lbl_players.place(x=40, y=120)
    global lbl_listPlayers
    lbl_listPlayers = tk.Label(text="João Vitor: 8 \nVinicius: 5", bg=bg_quadro, font=("arial", 20), justify="left")
    lbl_listPlayers.place(x=25, y=180)


def mesa():
    mesa = tk.Frame(window, width=500, height=380, bg=bg_quadro)
    mesa.place(x=250, y=100)
    mesa2 = tk.Frame(mesa, bg=bg_quadro, width=500, height=380)
    mesa2.place(x=75, y=7)
    for i in range(6):
        for j in range(6):
            cartas[i][j] = tk.Button(mesa2, width=4, height=2, cursor="hand2", bg=bg_carta, activebackground=bg_carta, command=lambda x1=i, y1=j: Escolher(x1,y1))
            cartas[i][j].grid(column=j, row=i, padx=12, pady=10)


def sortear():
    for i in range(18):
        seq_cores[i] = cores[i]
        seq_cores[i+18] = cores[i]
    shuffle(seq_cores)


def atribuir_cores():
    x = 0
    for i in range(6):
        for j in range(6):
            cartas[i][j].config(bg=seq_cores[x])
            x = x + 1

def atribuir_jogadores():
    global lbl_listPlayers

    listPlayesr = ""

    for jogador in listPlayers:
        listPlayesr = listPlayesr + jogador + ": " + str(listPontos[listPlayers.index(jogador)]) + "\n"

    lbl_listPlayers.config(text=listPlayesr)


def Escolher(y, x):
    print("\n\nEscolhido: \nCarta: ", y, x)



def main():
    print("Iniciando cliente")

    janela()
    players()
    mesa()
    sortear()
    atribuir_cores()
    atribuir_jogadores()

    window.mainloop()

    com.canal.basic_publish(exchange='', routing_key='com_jogador', body='sair')



