""" 
    Projeto SD - Jogo da Memória
    # Autor: Vinicius
    # Data de criação:      01/11/2022
    # Data de modificação:  19/12/2022
    # Este programa é o cliente do jogo da memória.
    # Ele é responsável por receber as mensagens do servidor e enviar as mensagens para o servidor.
    # Ele também é responsável por gerenciar a interface gráfica para o usuário.
 """

import comunicacao
import tela
import threading


# Função principal
if __name__ == '__main__':
    print("Iniciando Cliente...\n")
    
    vetorThreads = []

    # Inicia a comunicação
    print("Iniciando Comunicação")
    thread = threading.Thread(target=comunicacao.main, args=())
    thread.start()
    vetorThreads.append(thread)

    # Inicia a janela
    print("Iniciando Janela\n")
    target=tela.main()

    # Espera as threads terminarem
    for t in vetorThreads:
        t.join()
        

