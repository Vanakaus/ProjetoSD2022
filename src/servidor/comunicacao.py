

import pika
import json
import tela

conexao = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
canal = conexao.channel()


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



def main():

    canal.queue_declare(queue='com_geral')
    canal.queue_declare(queue='com_jogador')

    canal.basic_consume(queue='com_jogador', on_message_callback=msgJogador, auto_ack=True)
    canal.start_consuming()
