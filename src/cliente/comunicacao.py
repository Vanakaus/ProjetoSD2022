""" 
    Projeto SD - Jogo da Memória
    # Autor: Vinicius
    # Data de criação:      01/11/2022
    # Data de modificação:  19/12/2022
    # Este programa é o cliente do jogo da memória.
    # Ele é responsável por receber as mensagens do servidor e enviar as mensagens para o servidor.
 """
import tela
import pika
import json


# Deefinição da fila de comunicação e do canal de comunicação
conexao = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
canal = conexao.channel()

# Deefinição do nome da fila de comunicação
queue_name = canal.queue_declare(queue='', exclusive=True)
queue_name = queue_name.method.queue

# Variáveis globais
emJogo = False
nomeJogador = ""
pontos = 0


# Função para setar a variável emJogo
def setEmJogo(entrou):
    global emJogo
    emJogo = entrou

# Função para setar a variável nomeJogador
def setNomeJogador(nome):
    global nomeJogador
    nomeJogador = nome


# Função que trata as mensagens do servidor
def msgServidor(ch, method, properties, body):
    print("\nMensagem do Servidor:")

    mensagem = body.decode('utf-8').replace('\'', '"')
    msg = json.loads(mensagem)
    
    print(msg["acao"])

    match msg["acao"]:
        case "atualizar":

            listPlayers = ""
            pontos = 0
            for jogador in msg["jogadores"]:
                if nomeJogador == jogador:
                    pontos = msg["pontos"][msg["jogadores"].index(jogador)]
                    print("\nMeus Pontos: " + str(pontos))
                
                listPlayers = listPlayers + jogador + ": " + str(msg["pontos"][msg["jogadores"].index(jogador)]) + "\n"

            print("\n", listPlayers)

            tela.atualizar(listPlayers, pontos)


        case "vezJogador":

            if nomeJogador == msg["jogador"]:
                suaVez = True
                mensagem = "Sua vez de jogar"
            else:
                suaVez = False
                mensagem = "Vez de " + msg["jogador"]
            
            tela.vezJogador(mensagem, suaVez)


        case "iniciarJogo":
            tela.iniciarJogo()


        case "entrar":
            if not emJogo and nomeJogador == msg["jogador"]:
                tela.entrarResposta(msg["mensagem"], msg["cor"])

        case "virar":
            tela.virarCarta(msg["x"], msg["y"], msg["cor"])

        case "desvirar":
            tela.desvirarCarta(msg["x"], msg["y"])

        case "retirar":
            tela.retirarCartas(msg["carta1"][0], msg["carta1"][1], msg["carta2"][0], msg["carta2"][1])

        case "sair":
            canal.stop_consuming()
        case _:
            print("Ação não reconhecida")


# Função principal
def main():

    # Definição daa filaa de comunicação
    canal.queue_declare(queue='com_jogador')
    canal.exchange_declare(exchange='com_geral', exchange_type='direct')


    # Definição da fila que será escutada
    canal.queue_bind(exchange='com_geral', queue=queue_name, routing_key="")


    # Inicia o consumo da fila
    canal.basic_consume(queue=queue_name, on_message_callback=msgServidor, auto_ack=True)
    canal.start_consuming()