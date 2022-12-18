

import pika

conexao = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
canal = conexao.channel()


def msgJogador(ch, method, properties, body):
    print(body.decode('utf-8'))

    if body.decode('utf-8') == "sair":
        canal.stop_consuming()



def main():

    canal.queue_declare(queue='com_geral')
    canal.queue_declare(queue='com_jogador')

    canal.basic_consume(queue='com_jogador', on_message_callback=msgJogador, auto_ack=True)
    canal.start_consuming()
