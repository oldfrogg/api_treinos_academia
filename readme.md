# API Treinos (secundária) - PUC Academia

## Objetivo
A aplicação tem como objetivo fazer o controle de cadastro de treinos para o uso de uma academia.


## Descrição
Ela tem as opções de adicionar e remover treinos, requisitar todos os treinos, elaborar um treino com base no nível e grupo muscular. Tudo isso através do acesso e manipulação de um banco de dados SQLite.

Importante: Esta API deve ser executada na porta 5001.


## Rotas
* / - GET - Mostra as rotas disponíveis e parâmetros aceitos nas rotas
* /treinos - GET - para ver todos os treinos"
* /meutreino/<nivel>/<grupo_muscular> - GET - para ter um treino montado"
* /add - POST - para adicionar um treino ao banco de dados"
* /delete/treino/<id> - DELETE - para excluir um treino do banco de dados"


## Execução da API 
Primeiro será mostrado como executar em modo de desenvolvimento, e depois como executar via Docker. Para ambos os casos o Banco de Dados, caso ainda não exista, será criado e populado.

### Execução em modo de desenvolvimento
Para executar a aplicação, é recomendável realizar a instalação dos pacotes necessários e executá-lo em um ambiente virtual.

Para criar um ambiente virtual é necessário navegar no terminal até o diretório da aplicação e dar o comando:
```
> python -m venv venv
```

Além de criar é necessário deixá-lo ativado para a instalação das bibliotecas e execução da aplicação.

Para ativar o ambiente virtual, faça o  seguinte:
    No Windows:
    ```
    > .\venv\Scripts\activate
    ```

    No Linux:
    ```
    > source venv/bin/activate
    ```

Pronto, agora deve aparecer um "(venv)" no início da sua linha de comando no terminal. 

Isso indica que o ambiente virtual está ativo.

Caso queira desativá-lo, basta executar:
```
> deactivate
```


Agora, com o ambiente virtual ativo, você deve instalar as bibliotecas necessárias na aplicação.

Para isso, execute o comando:
```
> pip install -r requirements.txt
```

Com isso, a aplicação estará pronta para a execução.

O banco de dados utilizado é o SQLite, o arquivo db.sqlite3 será criado em sua máquina na primeira execução do programa.

Por fim, para executar a aplicação, basta executar o flask da seguinte forma:
```
> flask run --port 5001
```

Com isso a aplicação ficará ativa em um servidor local. Você poderá acessá-lo através do navegador utilizando:
    <http://localhost:5001>
ou:
    <http://127.0.0.1:5001>

Você terá 3 escolhas de documentação, mas é recomendável a utilização do Swagger.



### Execução via Docker
Caso não o tenha, instale o Docker em sua máquina.

Navegue através do terminal até o diretório onde encontra-se o Dockerfile e os arquivos da aplicação e execute como administrador (Coloca 'sudo' antes do comando no Linux) o seguinte comando para construir a imagem Docker:
```
> $ docker build -t treinos-api .
```

Após criada a imagem, execute-a como admnistrador:
```
> $ docker run --network bridge --name treinos-container -d -p 5001:5001 treinos-api
```

Agora, basta abrir o 
    <http://localhost:5001>
