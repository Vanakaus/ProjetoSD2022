import tkinter as tk
from random import shuffle

window = tk.Tk()
bg_quadro = "#fefefe"
bg_carta = "#e8c999"
pontos = 0
lbl_pontuacao2 = tk.Label()
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
    window.configure(bg="#00c8ff")
    window.resizable(False, False)
    window.iconbitmap("src/icons/cartas.ico")

    lbl_titulo = tk.Label(window, text="Jogo da Memoria", bg="#00c8ff", font=("Arial", 32))
    lbl_titulo.place(x=220, y = 30)

def pontuacao():
    mesa = tk.Frame(window, width=200, height=80, bg=bg_quadro)
    mesa.place(x=20, y=100)

    lbl_pontuacao = tk.Label(text="Sua Pontuação:", bg=bg_quadro, font=("arial", 20))
    lbl_pontuacao.place(x=20, y=100)
    global lbl_pontuacao2
    lbl_pontuacao2 = tk.Label(text=pontos, bg=bg_quadro, font=("arial", 20))
    lbl_pontuacao2.place(x=25, y=130)

def players():
    mesa2 = tk.Frame(window, width=200, height=280, bg=bg_quadro)
    mesa2.place(x=20, y=200)

    lbl_players = tk.Label(text="Jogadores", bg=bg_quadro, font=("arial", 22))
    lbl_players.place(x=40, y=200)

    global lbl_listplayers
    lbl_listPlayers = tk.Label(text="João Vitor: 8 \nVinicius: 5", bg=bg_quadro, font=("arial", 18), justify="left")
    lbl_listPlayers.place(x=25, y=250)

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


def atrribuir_cores():
    x = 0
    for i in range(6):
        for j in range(6):
            cartas[i][j].config(bg=seq_cores[x])
            x = x + 1

def Escolher(y, x):
    print("Carta [{}][{}] escolhida".format(x, y))
    print("x", x)
    print("y", y)
    print("Cor: ", y*6 + x)

    cartas[y][x].config(bg=seq_cores[y*6 + x])
    cartas[y][x].config(state="disabled")
    if carta1[0] == -1 and carta1[1] == -1:
        carta1[0] = x
        carta1[1] = y
    elif carta2[0] == -1 and carta2[1] == -1:
        carta2[0] = x
        carta2[1] = y

        window.update()
        window.after(1000)

        if seq_cores[carta1[0] + carta1[1]*6] == seq_cores[carta2[0] + carta2[1]*6]:
            print("Acertou")
            cartas[carta1[1]][carta1[0]].destroy()
            cartas[carta2[1]][carta2[0]].destroy()
            carta1[0] = -1
            carta1[1] = -1
            carta2[0] = -1
            carta2[1] = -1

            global pontos
            pontos = pontos + 1
            lbl_pontuacao2.config(text=pontos)
        else:
            print("Errou")
            cartas[carta1[1]][carta1[0]].config(bg=bg_carta, state="normal")
            cartas[carta2[1]][carta2[0]].config(bg=bg_carta, state="normal")
            carta1[0] = -1
            carta1[1] = -1
            carta2[0] = -1
            carta2[1] = -1


def retirar(x, y):
    # cartas[x][y].destroy()
    # print("Carta [{}][{}] retirada".format(x, y))
    # print("x", x)
    # print("y", y)
    bg_carta = "white"
    cartas[x][y].config(bg=bg_carta)
    cartas[x][y].config(state="disabled")


if __name__ == "__main__":
    print("Iniciando cliente")

    janela()
    pontuacao()
    players()
    mesa()
    sortear()
    atrribuir_cores()

    window.mainloop()