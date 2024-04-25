from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text

# importando os elementos definidos no modelo
from model.base import Base
from model.treinos import Treinos


import os


# Defino um diretório para o BD
db_path = "database/"
# Verifica se o diretorio não existe
if not os.path.exists(db_path):
   # então cria o diretorio
   os.makedirs(db_path)

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'sqlite:///%s/db.sqlite3' % db_path


# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Cria uma fábrica de sessões com o banco
Session = sessionmaker(bind=engine)

# Atribuo o caminho para popular o BD
sql_file_path = 'popular.sql'

# cria o banco se ele não existir 
if not database_exists(engine.url):
    create_database(engine.url) 

    # cria as tabelas do banco, caso não existam
    Base.metadata.create_all(engine)
    # Está pegando todas as classes que foram definidas no model que herdam da classe Base. 
    # Com a estrutura, cria o banco

    # Populo o BD apos a criacao, com os dados iniciais
    with engine.connect() as connection: #abre a conexao e fecha apos o uso por conta do with
        with open(sql_file_path, 'r', encoding="utf-8") as file: #abro o arquivo de popular o BD
            sql_commands = file.read() #armazeno o conteudo do arquivo na variavel
            for statement in sql_commands.split(';'): #separo os comandos sql
                if statement.strip(): #limpo espacos em branco
                    connection.execute(text(statement))
                    connection.commit()
