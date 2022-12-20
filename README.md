# ProjetoSD2022
Repositório para o projeto de desenvolvimento de aplicação distribuída, para a matéria de sistemas distribuídos, 2022/2.

## Tema:
Um jogo da memória multijogador - local. Com jogadores conectados em uma mesma rede local, e um servidor, que armazena os dados da partida, e envia as informações para os clientes, que são as telas do jogo. Podendo haver diversos jogadores conectados ao mesmo tempo, e cada um com sua própria tela de jogo. Usando o RabbitMQ como serviço de mensagens, para a comunicação entre o servidor e os clientes.   
   
## Diagrama de Arquitetura de Sistema:
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

## Interface de Serviço:   

### Cliente
![alt text](https://github.com/Vanakaus/ProjetoSD2022/blob/main/images/InterfaceDeServicoCom.jpg?raw=true "Interface de Serviço 1 do Servidor")
O servidor escuta as reuisições dos clientes atraves de uma fila de mensagens, então executa uma função com o corpo da mensagem recebida, esta função verifica o tipo de ação a ser executada e executa a funcao de acordo com a requisição. Caso a reuisição nao seja reconhecido mostra uma mensagem de aviso.

![alt text](https://github.com/Vanakaus/ProjetoSD2022/blob/main/images/InterfaceDeServicoTela.jpg?raw=true "Interface de Serviço 2 do Servidor")
De acordo com a ação requisitada o servidor as realiza e retorna uma mensagem para tdos os clientes informando a ação realizada e atualizando os dados do jogo e dos clientes.  

### Cliente
![alt text](https://github.com/Vanakaus/ProjetoSD2022/blob/main/images/InterfaceDeServicoComCliente.png?raw=true "Interface de Serviço 1 do Cliente")
O cliente está inscrito na fila de comunicacação do servidor. Assim como o sevidor, ele recebe amensagem e executa uma função com o corpo da mensagem, e de acordo com a atualização ele executa sua função correspondente. 

![alt text](https://github.com/Vanakaus/ProjetoSD2022/blob/main/images/InterfaceDeServicoTelaCliente.png?raw=true "Interface de Serviço 2 do Cliente")
Após o usuario realizar uma ação dentro do jogo, esta informação é encapsulada em uma mensagem e enviada para o servidor, que controla o jogo, poder gerenciar as aç`~oes e atualizar todos os cliente.

### Diagrama de Telas:   
![alt text](https://github.com/Vanakaus/ProjetoSD2022/blob/main/images/Telas.png?raw=true "Telas")

## Tecnologias: 
Para desenvolver essa aplicação usamos a linguagem python, com a biblioteca gráfica Tkinter. Com isso, conseguimos criar uma aplicação distribuída, com um servidor e vários clientes, que se comunicam através de uma fila de mensagens, criada com o RabbitMQ.

* Python 3.10 - Linguagem de Programação: Para desenvolvimento da aplicação, tanto do servidor, quanto do cliente.
* Tkinter - Biblioteca gráfica do Python: Para desenvolvimento da interface gráfica.
* RabbitMQ - Serviço de Mensagem: Para criar um canal de comunicação com duas filas entre o servidor e os clientes.

## Alunos: 
João Vitor Zavatin - Ra: 1923242  
Vinicius Vieira - Ra: 2046474  
  
Inicialmente o projeto foi desenvolvido em dupla, mas, por motivos de desistência, o projeto foi finalizado por apenas um aluno, Vinicius vieira.

## Executar o projeto:
### Pré-requisitos:
- Python 3.10
- RabbitMQ

### Servidor:
Para iniciar o servidor, basta executar o arquivo `server.py` através do diretorio raíz do projeto `python3 src/servidor/servidor.py`.

### Cliente:
Para iniciar o cliente, basta executar o arquivo `client.py` através do diretorio raíz do projeto `python3 src/cliente/cliente.py`.
  

## Professor:
Prof. Rodrigo Campiolo
