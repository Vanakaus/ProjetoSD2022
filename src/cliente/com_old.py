# from client import canal


def teste(ch, method, properties, body):

    print(body.decode('utf-8'))

    if body.decode('utf-8') == "sair":
        canal.stop_consuming()

    print(" [x] Received %r" % body)
    print(body[0])
    print(body[1])

def comunicacao(cnl):
    global canal
    canal = cnl
    canal.basic_consume(queue='teste', on_message_callback=teste, auto_ack=True)
    canal.start_consuming()
    print("teste")