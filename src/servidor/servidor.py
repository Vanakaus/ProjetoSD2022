
import comunicacao
import tela
import threading


if __name__ == '__main__':

    print("Iniciando servidor")

    vetorThreads = []

    print("Iniciando Comunicação")
    thread = threading.Thread(target=comunicacao.main, args=())
    thread.start()
    vetorThreads.append(thread)

    print("Iniciando Tela")
    target=tela.main()

    for t in vetorThreads:
        t.join()
        