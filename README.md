# ProjetoSD2022
Repositório para o projeto de desenvolvimento de aplicação distribuída, para a matéria de sistemas distribuídos, 2022/2.

## Tema:
Um jogo da memória multijogador - local.   
   
### Diagrama de Arquitetura de Sistema:
![alt text](https://github.com/Vanakaus/ProjetoSD2022/blob/main/images/ArquiteturaSist.png?raw=true "Arquitetura do Sistema")   
O programa vai consistir de um servidor, onde ficam armazenados os dados de partida, com as cartas, jogadores conectados e suas respectivas pontuações, e diversos clientes, onde será mostrado a tela do jogo para o usuário, e onde ele irá interagir com o jogo.  

![alt text](https://github.com/Vanakaus/ProjetoSD2022/blob/main/images/ArquiteturaNet.png?raw=true "Arquitetura da Rede")   
A comunicação entre o servidor e os clientes será feita através de uma serviço de mensagem, contendo duas filas de mensagens, uma para o servidor enviar mensagens para os clientes, e outra para os clientes enviarem mensagens para o servidor.

1. Usuario utiliza uma fila de mensagens para enviar uma mensagem para o servidor, atravez de uma publicação simples.
2. Uma fila de mensagens para o servidor receber mensagens dos clientes, atravez de uma publicação simples.
3. A mensagem consiste no formato json, com a ação que sera realizada, e os dados necessários para a ação.
4. O servidor recebe a mensagem, e realiza a ação, e envia uma mensagem para o cliente, atravez de uma publicação simples.
5. Uma fila de mensagens pra o servidor enviar mensagens para os clientes, que se inscrevem nela atravez de um *bind*.
6. A mensagem consiste no formato json, com a ação que sera realizada, e os dados necessários para a ação.

### Diagrama de Telas:   
![alt text](https://github.com/Vanakaus/ProjetoSD2022/blob/main/images/Telas.png?raw=true "Telas")

## Tecnologias: 
Para desenvolver essa aplicação usamos a linguagem python, com a biblioteca gráfica Tkinter. Com isso, conseguimos criar uma aplicação distribuída, com um servidor e vários clientes, que se comunicam através de uma fila de mensagens, criada com o RabbitMQ.

## Alunos: 
João Vitor Zavatin - Ra: 1923242  
Vinicius Vieira - Ra: 2046474  
  
Inicialmente o projeto foi desenvolvido em dupla, mas, por motivos de desistência, o projeto foi finalizado por apenas um aluno, Vinicius vieira.

## Como rodar o projeto:
### Pré-requisitos:
- Python 3.10
- RabbitMQ

### Servidor:
Para rodar o servidor, basta executar o arquivo `server.py` através do diretorio do projeto `src/servidor/servidor.py`.

### Cliente:
Para rodar o cliente, basta executar o arquivo `client.py` através do diretorio do projeto `src/cliente/cliente.py`.

## Professor:
Prof. Rodrigo Campiolo
