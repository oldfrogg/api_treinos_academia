# API Treinos (secundária) - PUC Academia

## Objetivo
A aplicação tem como objetivo fazer o controle de cadastro de treinos para o uso de uma academia.


## Descrição
Projeto acadêmico de um MVP para a sprint "Desenvolvimento Back End Avançado" da pós graduação de "Desenvolvimento Full Stack" da PUC-RJ.

Esta API tem as opções de adicionar e remover treinos, requisitar todos os treinos, elaborar um treino com base no nível e grupo muscular. Tudo isso através do acesso e manipulação de um banco de dados SQLite.

Importante: Esta API deve ser executada na porta 5001.


## Rotas
* / - GET - Mostra as rotas disponíveis e parâmetros aceitos nas rotas
* /treinos - GET - para ver todos os treinos"
* /meutreino/<nivel>/<grupo_muscular> - GET - para ter um treino montado"
* /add - POST - para adicionar um treino ao banco de dados"
* /delete/treino/<id> - DELETE - para excluir um treino do banco de dados"

Parâmetros aceitos em <níivel>:  'iniciante', 'intermediario', 'avancado';
Parâmetros aceitos em <grupo_muscular>: 'peito', 'costas', 'biceps', 'triceps', 'trapezio', 'ombros', 'pernas';
Parâmetros aceitos em <id>: Númreros decimais sem o 0, cujo limite depende da quantidade de exercicios cadastrados.

## Execução da API 
Primeiro será mostrado como executar em modo de desenvolvimento, e depois como executar via Docker. Para ambos os casos o Banco de Dados, caso ainda não exista, será criado e populado.

## Execução em modo de desenvolvimento
Para executar a aplicação, deve-se realizar a instalação dos pacotes necessários e executá-lo em um ambiente virtual.

Para criar um ambiente virtual é necessário navegar no terminal até o diretório da aplicação e dar o comando:
```
python -m venv venv
```

Além de criar é necessário deixá-lo ativado para a instalação das bibliotecas e execução da aplicação.

Para ativar o ambiente virtual, faça o  seguinte:
*No Windows:
```
.\venv\Scripts\activate
```

* No Linux:
```
source venv/bin/activate
```

Pronto, agora deve aparecer um "(venv)" no início da sua linha de comando no terminal. 

Isso indica que o ambiente virtual está ativo.

Caso queira desativá-lo, basta executar:
```
deactivate
```


Agora, com o ambiente virtual ativo, você deve instalar as bibliotecas necessárias na aplicação.

Para isso, execute o comando:
```
pip install -r requirements.txt
```

Com isso, a aplicação estará pronta para a execução.

O banco de dados utilizado é o SQLite, o arquivo db.sqlite3 será criado em sua máquina na primeira execução do programa.

Por fim, para executar a aplicação, basta executar o flask da seguinte forma:
```
flask run --port 5001
```

Com isso a aplicação ficará ativa em um servidor local. Você poderá acessá-lo utilizando, podendo utilizar o Postman ou similar para fazer as requisições disponíveis:
<http://localhost:5001>
ou:
<http://127.0.0.1:5001>



## Execução via Docker
Caso não o tenha, instale o Docker em sua máquina.


### Para instalar o Docker no Windows
Baixar o wsl com o terminal Windows em modo de administrador
```
wsl --install
```

Siga os passos disponíveis no link a seguir:

<https://docs.docker.com/desktop/install/windows-install/>

De preferência, instalar com componentes requeridos para o WSL 2


Após instalado, o comando "ubuntu" irá transformar o cmd ou powershell em um terminal linux, mas também é possível abrir um terminal no vscode e adicionar um terminal wsl, utilizando a extensão "WSL".



### Para instalar o Docker no Linux
Siga os passos disponíveis para a sua distribuição informados no link a seguir:

<https://docs.docker.com/desktop/install/linux-install/>


### Para instalar o Docker no mac
Siga os passos informados no link a seguir:

<https://docs.docker.com/desktop/install/mac-install/>


Para todos os casos, o modo de virtualização precisa estar ativado na BIOS.


## Com o Docker instalado em sua máquina

Navegue através do terminal até o diretório onde encontra-se o Dockerfile e os arquivos da aplicação e execute como administrador (Coloca 'sudo' antes do comando no Linux) o seguinte comando para construir a imagem Docker com o nome "treinos-api":
```
docker build -t treinos-api .
```

Após criada a imagem, crie e execute um container dessa imagem como admnistrador, com o nome "treinos-api":
```
docker run --network bridge --name treinos-container -d -p 5001:5001 treinos-api
```

Pronto, o container já deve estar ativo! Para verificar, basta abrir o: 
<http://localhost:5001>

Caso queira ver os container em execução execute o comando 
```
docker ps
```


Caso queira parar a execução do container, execute o comando 
```
docker stop treinos-container
```


Caso queira re-executar o container, execute o comando
```
docker start treinos-contaienr
```


Caso queira excluir o container, pare sua execução e o remova com o comando
```
docker rm treinos-container
```


Para listar as imagens construídas no Docker, execute o comando:
```
docker images
```


Caso queira excluir a imagem, execute o comando
```
docker rmi treinos-api
```
