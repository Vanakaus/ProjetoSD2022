# ProjetoSD2022
Repositório para o projeto de desenvolvimento de aplicação distribuída, para a matéria de sistemas distribuídos, 2022/2.

## Tema:
Um jogo da memória multijogador - local.   
   
### Diagrama de Arquitetura de Sistema:
![alt text](https://github.com/Vanakaus/ProjetoSD2022/blob/main/images/ArquiteturaSist.png?raw=true "Arquitetura")   
O programa vai consistir de um servidor, onde ficam armazenados os dados de partida, com as cartas, jogadores conectados e suas respectivas pontuações, e diversos clientes, onde será mostrado a tela do jogo para o usuário, e onde ele irá interagir com o jogo.

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
