
from time import sleep
import comunicacao as com
import tkinter as tk
from random import shuffle

window = tk.Tk()
bg_janela = "#00c8ff"
bg_quadro = "#fefefe"
bg_carta = "#e8c999"

listPlayers = []
listPontos = []
lbl_listPlayers = tk.Label()
btn_iniciar = tk.Button()
playerAtual = 0
jogoIniciado = False

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
    window.geometry("800x500+200+200")
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
    lbl_listPlayers = tk.Label(text="", bg=bg_quadro, font=("arial", 20), justify="left")
    lbl_listPlayers.place(x=25, y=180)


def mesa():
    mesa = tk.Frame(window, width=500, height=380, bg=bg_quadro)
    mesa.place(x=250, y=100)
    mesa2 = tk.Frame(mesa, bg=bg_quadro, width=500, height=380)
    mesa2.place(x=75, y=7)
    for i in range(6):
        for j in range(6):
            # cartas[i][j] = tk.Button(mesa2, width=4, height=2, cursor="hand2", bg=bg_carta, activebackground=bg_carta, relief="groove", command=lambda x1=i, y1=j: vezJogador())
            cartas[i][j] = tk.Button(mesa2, width=4, height=2, cursor="arrow", bg=bg_carta, activebackground=bg_carta, state="disabled")
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

    listPlayersTxt = ""

    for jogador in listPlayers:
        listPlayersTxt = listPlayersTxt + jogador + ": " + str(listPontos[listPlayers.index(jogador)]) + "\n"

    lbl_listPlayers.config(text=listPlayersTxt)

    atualizar()


def lobby():
    global btn_iniciar
    btn_iniciar = tk.Button(window, text="Iniciar Jogo", font=("Arial", 18), bg="lightgreen", activebackground="lightgreen", state="disable", command=iniciarJogo)
    btn_iniciar.place(x=50, y=40)


def main():

    janela()
    players()
    mesa()
    lobby()

    window.mainloop()

    com.canal.basic_publish(exchange='', routing_key='com_jogador', body="{'acao': 'sair'}")


def iniciarJogo():
    print("\nIniciando Jogo: ")

    global btn_iniciar
    btn_iniciar.destroy()

    global jogoIniciado
    jogoIniciado = True

    sortear()
    atribuir_cores()
    atribuir_jogadores()
    com.canal.basic_publish(exchange='com_geral', routing_key='', body="{'acao': 'iniciarJogo', 'mensagem': 'Jogo iniciado!'}")

    global listPlayers
    shuffle(listPlayers)

    vezJogador()



def entrar(jogador):
    print("\Jogador entrando: ", jogador)

    global listPlayers
    global listPontos
    global btn_iniciar

    if jogoIniciado:
        com.canal.basic_publish(exchange='com_geral', routing_key='', body="{'acao': 'entrar', 'jogador':'" + jogador + "', 'mensagem': 'Jogo ja iniciado!', 'cor': 'red'}")
    elif jogador not in listPlayers:
        listPlayers.append(jogador)
        listPontos.append(0)
        atribuir_jogadores()
        com.canal.basic_publish(exchange='com_geral', routing_key='', body="{'acao': 'entrar', 'jogador':'" + jogador + "', 'mensagem': 'Voce entrou no jogo!', 'cor': 'green'}")
    else:
        com.canal.basic_publish(exchange='com_geral', routing_key='', body="{'acao': 'entrar', 'jogador':'" + jogador + "', 'mensagem': 'Nome de jogador ja existe!', 'cor': 'red'}")
    
    if len(listPlayers) > 1:
        btn_iniciar.config(state="normal")
    


def atualizar():
    print("\nAtualizando Jogadores: ")

    global listPlayers
    global listPontos

    mensagem = {"acao": "atualizar", "jogadores": listPlayers, "pontos": listPontos}

    print(mensagem["jogadores"])
    print(mensagem["pontos"])

    com.canal.basic_publish(exchange='com_geral', routing_key='', body=str(mensagem))


def virar(x, y):
    print("\nVirando Carta: ", x, y)
    cartas[x][y].config(relief="sunken")

    mensagem = {"acao": "virar", "x": x, "y": y, "cor": cartas[x][y].cget("bg")}

    com.canal.basic_publish(exchange='com_geral', routing_key='', body=str(mensagem))


def desvirar(x, y):
    print("\nDesvirando Carta: ", x, y)
    cartas[x][y].config(relief="groove")

    mensagem = {"acao": "desvirar", "x": x, "y": y}

    com.canal.basic_publish(exchange='com_geral', routing_key='', body=str(mensagem))


def retirar():

    print("\nRetirar: ", carta1, carta2)

    cartas[carta1[0]][carta1[1]].config(relief="raised")
    cartas[carta2[0]][carta2[1]].config(relief="raised")

    mensagem = {"acao": "retirar", "carta1": carta1, "carta2": carta2}

    com.canal.basic_publish(exchange='com_geral', routing_key='', body=str(mensagem))


def vezJogador():
    print("\nVez do Jogador: ", listPlayers[playerAtual])

    mensagem = {"acao": "vezJogador", "jogador": listPlayers[playerAtual]}

    com.canal.basic_publish(exchange='com_geral', routing_key='', body=str(mensagem))


def escolherCarta(x, y):

    global playerAtual
    global carta1
    global carta2

    print(listPlayers[playerAtual])
    print("\nEscolheu Carta: ", x, y)

    print(carta1)

    if carta1 == [-1, -1]:
        print("carta1")
        carta1[0] = x
        carta1[1] = y
        virar(x, y)
        print("virou")

    elif carta2 == [-1, -1]:
        carta2[0] = x
        carta2[1] = y
        virar(x, y)
        sleep(1)

        if cartas[carta1[0]][carta1[1]].cget("bg") == cartas[carta2[0]][carta2[1]].cget("bg"):
            listPontos[playerAtual] = listPontos[playerAtual] + 1
            retirar()
            atribuir_jogadores()
        else:
            desvirar(carta1[0], carta1[1])
            desvirar(carta2[0], carta2[1])
            playerAtual = playerAtual + 1
            if playerAtual >= len(listPlayers):
                playerAtual = 0
        
        carta1[0] = -1
        carta1[1] = -1
        carta2[0] = -1
        carta2[1] = -1
    
    vezJogador()
