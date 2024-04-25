from flask import Flask, make_response, jsonify, request
import random
import json

from model import Session, Treinos

app = Flask(__name__)

with open('treinos.json', 'r', encoding='utf-8') as file:
    treinos = json.load(file)


@app.get('/')
def inicio():
    return jsonify({
        "Rotas": ["/treinos - GET - para ver todos os treinos", 
                  "/meutreino/<nivel>/<grupo_muscular> - GET - para ter um treino montado",
                  "/add - POST - para adicionar um treino ao banco de dados",
                  "/delete/treino/<id> - DELETE - para excluir um treino do banco de dados"],
                   "Niveis": "'basico', 'intermediario' e 'avancado'",
                   "Grupos musculares": "'peito', 'costas', 'biceps', 'triceps', 'ombro', 'trapezio', 'pernas'"})

#Retornar todos os treinos cadastrados
@app.get('/treinos')
def todos_os_treinos():
    try:
        # Conecta-se com o BD
        session = Session() 
        
        # Seleciona e cria uma lista com os treinos do grupo muscular selecionado
        treinos = session.query(Treinos).all()
        lista_de_treinos = [{'id': treino.id, 'grupo_muscular': treino.grupo_muscular, 'exercicio': treino.exercicio} for treino in treinos]
        
        # Retorna uma quantidade aleatória de exercícios, cuja quantidade dependerá do nível
        return make_response(lista_de_treinos), 200

    except json.JSONDecodeError as e:
        error_msg = "Requisição não entendida pelo servidor. Sintaxe inválida."
        return {"message": error_msg}, 400   

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível selecionar treino :/"
        return {"message": error_msg + str(e)}, 400



@app.get('/meutreino/<nivel>/<grupo_muscular>')
def monta_treino(nivel, grupo_muscular):
    
    # Define a quantidade de exercicios de acordo com o nivel do aluno
    if nivel == "iniciante":
            qtde_ex=3
    elif nivel == "intermediario":
            qtde_ex=4
    elif nivel == "avancado":
            qtde_ex=5
    else: return {"message": "Níveis permitidos: 'iniciante', 'intermediario', e 'avancado'"}
     
    try:
        # Conecta-se com o BD
        session = Session() 
        # Seleciona e cria uma lista com os treinos do grupo muscular selecionado
        grupo_selecionado = session.query(Treinos).filter(Treinos.grupo_muscular == grupo_muscular).all()
        if len(grupo_selecionado)==0:
            return {"message": "Grupo muscular inexistente.\nGrupos possíveis: 'peito', 'costas', 'biceps', 'triceps', 'ombro', 'trapezio', 'perna'"}
        lista_de_treinos = [{'id': treino.id, 'grupo_muscular': treino.grupo_muscular, 'exercicio': treino.exercicio} for treino in grupo_selecionado]
        
        # Retorna uma quantidade aleatória de exercícios, cuja quantidade dependerá do nível
        return make_response(random.sample(lista_de_treinos, qtde_ex)), 200


    except KeyError as e:
        error_msg = "Dados inválidos."
        return {"message": error_msg + str(e)}, 400

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível selecionar treino :/"
        return {"message": error_msg + str(e)}, 400



@app.post('/add')
def add_treino():

    if request.content_type == 'application/json':
        data = request.json  # Obter os dados JSON da requisição
    else:
        data = request.form  # Obter os dados de formulário da requisição
    
    grupo_muscular=data.get('grupo_muscular')
    exercicio=data.get('exercicio')
    
    treino_adicionado = Treinos(grupo_muscular=grupo_muscular, exercicio=exercicio)

    try:
        session=Session()
        session.add(treino_adicionado)
        session.commit()
        return jsonify({"message": f"Treino de id {treino_adicionado.id} adicionado com sucesso"}), 200
        
    except AttributeError as e:
        error_msg = "Dados inválidos."
        return {"message": error_msg + str(e)}, 400
    
    except TypeError as e:
        error_msg = "Dados inválidos."
        return {"message": error_msg + str(e)}, 400
        
    except Exception as e:
        # caso um erro fora do previsto
        session.rollback() #Reverte as alteracoes
        error_msg = "Não foi possível adicionar o treino :/"
        return {"message": error_msg + str(e)}, 400
    
    finally:
        session.close()



@app.delete('/delete/treino/<id>')
def delete(id):
    try:
        session = Session()
        treino_a_deletar = session.query(Treinos).filter(Treinos.id == id).first() #para colocar na msg dps
        count = session.query(Treinos).filter(Treinos.id == id).delete()
        session.commit()
        
        if count:
            return {"message": "treino removido"}
        
        else:
            error_msg = "Treino não encontrado na base :/"
            return {"message": error_msg + str(e)}, 400
    
    except Exception as e:
        # caso um erro fora do previsto
        session.rollback() #Reverte as alteracoes
        error_msg = "Não foi possível remover o treino :/"
        return {"message": error_msg + str(e)}, 400
    
    finally:
        session.close()
        


if __name__ == "__main__":
    app.run(port=5001, debug=True)