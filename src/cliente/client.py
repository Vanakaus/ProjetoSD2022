import tkinter as tk

window = tk.Tk()
cartas = [[0 for x in range(6)] for x in range(6)]
bg_quadro = "#fefefe"


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
    lbl_pontuacao2 = tk.Label(text="5", bg=bg_quadro, font=("arial", 20))
    lbl_pontuacao2.place(x=25, y=130)

def players():
    mesa2 = tk.Frame(window, width=200, height=280, bg=bg_quadro)
    mesa2.place(x=20, y=200)

    lbl_players = tk.Label(text="Jogadores:", bg=bg_quadro, font=("arial", 22))
    lbl_players.place(x=40, y=200)

    lbl_listPlayers = tk.Label(text="João Vitor - 8 \nVinicius - 5", bg=bg_quadro, font=("arial", 18), justify="left")
    lbl_listPlayers.place(x=25, y=250)

def mesa():
    mesa = tk.Frame(window, width=500, height=380, bg=bg_quadro)
    mesa.place(x=250, y=100)
    mesa2 = tk.Frame(mesa, bg=bg_quadro, width=500, height=380)
    mesa2.place(x=75, y=7)
    for i in range(6):
        for j in range(6):
            cartas[i][j] = tk.Button(mesa2, width=4, height=2, cursor="hand2", bg="#e8c999", activebackground="#e8c999", command=lambda x1=i, y1=j: retirar(x1,y1))
            cartas[i][j].grid(column=j, row=i, padx=12, pady=10)



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
    window.mainloop()