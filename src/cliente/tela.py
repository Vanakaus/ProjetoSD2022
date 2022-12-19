""" 
    Projeto SD - Jogo da Memória
    # Autor: Vinicius
    # Data de criação:      01/11/2022
    # Data de modificação:  19/12/2022
    # Este programa é o cliente do jogo da memória.
    # Ele também é responsável por gerenciar a interface gráfica para o usuário.
 """

import comunicacao as com
import tkinter as tk
from random import shuffle

# Variáveis globais
window = tk.Tk()
bg_janela = "#00c8ff"
bg_quadro = "#fefefe"
bg_carta = "#e8c999"

# Variáveis dos jogadores e pontuação
lbl_pontuacao2 = tk.Label()
lbl_listPlayers = tk.Label()
lbl_jogadorAtual = tk.Label()
lbl_resposta = tk.Label()
btn_entrar = tk.Label()

# Variáveis das cartas
cartas = [[0 for x in range(6)] for x in range(6)]
controleCartas = [x for x in range(36)]
carta = [-1, -1]


# Funções

# Função que inicia a janela do cliente
def janela():
    window.title("Jogo da Memória")
    window.geometry("800x500+1000+200")
    window.configure(bg=bg_janela)
    window.resizable(False, False)
    window.iconbitmap("src/icons/play.ico")

    lbl_titulo = tk.Label(window, text="Jogo da Memoria", bg=bg_janela, font=("Arial", 32))
    lbl_titulo.place(x=220, y = 30)


# Função que inicia o quadro da pontuação
def pontuacao():
    quadro = tk.Frame(window, width=200, height=80, bg=bg_quadro)
    quadro.place(x=20, y=100)

    lbl_pontuacao = tk.Label(quadro, text="Sua Pontuação:", bg=bg_quadro, font=("arial", 20))
    lbl_pontuacao.place(x=0, y=0)
    global lbl_pontuacao2
    lbl_pontuacao2 = tk.Label(quadro, text="0", bg=bg_quadro, font=("arial", 20))
    lbl_pontuacao2.place(x=5, y=30)


# Função que inicia o quadro dos jogadores
def players():
    quadro2 = tk.Frame(window, width=200, height=280, bg=bg_quadro)
    quadro2.place(x=20, y=200)

    lbl_players = tk.Label(quadro2, text="Jogadores", bg=bg_quadro, font=("arial", 22))
    lbl_players.place(x=20, y=0)

    global lbl_listPlayers
    lbl_listPlayers = tk.Label(quadro2, text=" ", bg=bg_quadro, font=("arial", 18), justify="left")
    lbl_listPlayers.place(x=5, y=50)

    global lbl_jogadorAtual
    lbl_jogadorAtual = tk.Label(quadro2, text=" ", bg=bg_quadro, font=("arial", 14), justify="left")
    lbl_jogadorAtual.place(x=5, y=250)


# Função que inicia o quadro da mesa com as cartas
def mesa():
    mesa = tk.Frame(window, width=500, height=380, bg=bg_quadro)
    mesa.place(x=250, y=100)
    mesa2 = tk.Frame(mesa, bg=bg_quadro, width=500, height=380)
    mesa2.place(x=75, y=7)
    for i in range(6):
        for j in range(6):
            cartas[i][j] = tk.Button(mesa2, width=4, height=2, bg=bg_carta, activebackground=bg_carta, command=lambda x1=i, y1=j: Escolher(x1,y1))
            cartas[i][j].grid(column=j, row=i, padx=12, pady=10)


# Função que inicia o quadro do lobby
def lobby():

    global lbl_jogador
    lbl_jogador = tk.Label(window, text="Jogador: ", bg=bg_janela, font=("arial", 22, "bold"))
    lbl_jogador.place(x=400, y=140)

    global ipt_jogador
    ipt_jogador = tk.Entry(window, width=20, font=("arial", 18))
    ipt_jogador.place(x=340, y=220)

    global lbl_resposta
    lbl_resposta = tk.Label(window, text=" ", bg=bg_janela, font=("arial", 14))
    lbl_resposta.place(x=400, y=255)

    global btn_entrar
    btn_entrar = tk.Button(window, text="Entrar", width=15, bg="green", activebackground="darkgreen", font=("arial", 16, "bold"), command=lambda: entrar(ipt_jogador.get()))
    btn_entrar.place(x=360, y=320)


# Função que inicia a janela do cliente
def main():
    janela()
    pontuacao()
    players()
    lobby()

    # Mantém a janela aberta
    window.mainloop()

    # Fecha a conexão com o servidor
    com.canal.basic_publish(exchange='com_geral', routing_key='', body="{'acao': 'sair'}")



# Função de entrada do jogador
def entrar(nome):
    print("\nEntrando...")
    print("Nome: {}".format(nome))
    com.setNomeJogador(nome)
    if nome == "":
        global lbl_resposta
        lbl_resposta.config(text="Digite um nome!", fg="red")
    else:
        global btn_entrar
        btn_entrar.config(state="disable")
        com.canal.basic_publish(exchange='', routing_key='com_jogador', body="{'acao': 'entrar', 'nome': '" + nome + "'}")


# Função que recebe a resposta do servidor sobre a entrada do jogador
def entrarResposta(mensagem, cor):
    global lbl_resposta
    global btn_entrar

    lbl_resposta.config(text=mensagem, fg=cor)
    
    if cor == 'red':
        btn_entrar.config(state="normal")
    else:
        com.setEmJogo(True)


# Função para virar uma carta
def virarCarta(x, y, cor):
    print("\nvirando carta: [{}][{}]".format(x, y))
    cartas[x][y].config(bg=cor, cursor="arrow")
    cartas[x][y]["state"] = "disabled"


# Função para desvirar uma carta
def desvirarCarta(x, y):
    print("\ndesvirando carta: [{}][{}]".format(x, y))
    cartas[x][y].config(bg=bg_carta, cursor="arrow")
    cartas[x][y]["state"] = "disabled"

    carta[0] = -1
    carta[1] = -1

# Função para retirar um par de cartas
def retirarCartas(x1, y1, x2, y2):
    print("\nretirando carta: ")
    print("carta1: [{}][{}]".format(x1, y1))
    print("carta2: [{}][{}]".format(x2, y2))

    cartas[x1][y1].config(bg=bg_quadro, activebackground=bg_quadro, cursor="arrow", borderwidth=0)
    cartas[x1][y1]["state"] = "disabled"

    cartas[x2][y2].config(bg=bg_quadro, activebackground=bg_quadro, cursor="arrow", borderwidth=0) 
    cartas[x2][y2]["state"] = "disabled"

    controleCartas.pop(controleCartas.index(x1*6+y1))
    controleCartas.pop(controleCartas.index(x2*6+y2))

    carta[0] = -1
    carta[1] = -1

# Função para atualizar a pontuação e a lista de jogadores
def atualizar(listPlayersTxt, pontos):
    print("\natualizando...")

    print(listPlayersTxt)

    global lbl_listPlayers
    global lbl_pontuacao2

    lbl_listPlayers.config(text=listPlayersTxt)
    lbl_pontuacao2.config(text=pontos)
    
    print("atualizado")


# Função para atualizar a vez do jogador
def vezJogador(mensagem, suaVez):
    print("\n", mensagem)

    global lbl_jogadorAtual
    lbl_jogadorAtual.config(text=mensagem)

    if suaVez:
        jogar()


# Função para habilitar as cartas para o jogador jogar
def habilitaCartas():
    for i in range(6):
        for j in range(6):
            if i*6+j in controleCartas:
                cartas[i][j]["state"] = "normal"
                cartas[i][j].config(cursor="hand2")
    
    if carta[0] != -1 and carta[1] != -1:
        cartas[carta[0]][carta[1]]["state"] = "disabled"


# Função para desabilitar as cartas para o jogador não jogar
def desabilitaCartas():
    for i in range(6):
        for j in range(6):
            if i*6+j in controleCartas:
                cartas[i][j]["state"] = "disable"
                cartas[i][j].config(cursor="arrow")


# Função para iniciar o jogo
def iniciarJogo():
    print("\nIniciando Jogo!")

    global lbl_jogador
    lbl_jogador.destroy()

    global ipt_jogador
    ipt_jogador.destroy()

    global btn_entrar
    btn_entrar.destroy()

    global lbl_resposta
    lbl_resposta.destroy()

    mesa()
    desabilitaCartas()


# Função para jogar
def jogar():
    print("\nJogando:")

    habilitaCartas()



# Função para escolher uma carta
def Escolher(x, y):
    print("Carta [{}][{}] escolhida".format(x, y))

    desabilitaCartas()

    global carta
    carta[0] = x
    carta[1] = y

    mensagem = {"acao": "escolher", "x": x, "y": y}

    com.canal.basic_publish(exchange='', routing_key='com_jogador', body=str(mensagem))

