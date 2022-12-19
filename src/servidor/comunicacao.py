""" 
    Projeto SD - Jogo da Memória
    # Autor: Vinicius
    # Data de criação:      01/11/2022
    # Data de modificação:  19/12/2022
    # Este programa é o servidor do jogo da memória.
    # Ele é responsável por receber as mensagens dos jogadores e enviar as mensagens para os jogadores.
    """

import pika
import json
import tela

# Deefinição da fila de comunicação e do canal de comunicação
conexao = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
canal = conexao.channel()


# Função que trata as mensagens do jogador
def msgJogador(ch, method, properties, body):
    print("\nMensagem do jogador: ")

    mensagem = body.decode('utf-8').replace('\'', '"')
    msg = json.loads(mensagem)
    
    print(msg["acao"])

    match msg["acao"]:
        case "escolher":
            tela.escolherCarta(msg["x"], msg["y"])

        case "entrar":
            tela.entrar(msg["nome"])

        case "sair":
            canal.stop_consuming()
        
        case _:
            print("Ação não reconhecida")



# Função principal
def main():

    # Deefinições das filas de comunicação
    canal.queue_declare(queue='com_geral')
    canal.queue_declare(queue='com_jogador')

    # Associação da função de tratamento de mensagens do jogador
    canal.basic_consume(queue='com_jogador', on_message_callback=msgJogador, auto_ack=True)
    canal.start_consuming()
