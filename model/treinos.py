from sqlalchemy import Column, String, Integer

from model import Base

class Treinos(Base):
    # O objeto Treinos terá um mapeamento direto com a tabela 'treinos'
    __tablename__ = 'treinos'
    
    id = Column(Integer, primary_key=True)
    grupo_muscular = Column(String(16))
    exercicio = Column(String(64))
    
    
    def __init__(self, grupo_muscular:str, exercicio:str):
        self.grupo_muscular = grupo_muscular
        self.exercicio = exercicio