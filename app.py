from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        "id": 0,
        "nome":"paulo",
        "habilidades":["Cobol","Clipper"]
    },
    {
        "id": 1,
        "nome":"bacalhau",
        "habilidades":["Prolog","Python"]        
    }
    ]

# Esta função consulta, altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET','PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == "GET":
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = "Desenvolvedor com ID {} não existe".format(id)
            response = {'status':'Completado com sucesso', 'mensagem':mensagem}
        except Exception:
            mensagem = "Erro desconhecido! Procure o administrador"
            response = {'status':'Completado com sucesso', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == "PUT":
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify({'status':'Completado com sucesso', 'mensagem':'Registro exluído'})

# Esta função permite incluir um desenvolvedor ou listar todos
@app.route('/dev/', methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method == "POST":
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        #return jsonify({'status':'Completado com sucesso', 'mensagem':'Registro incluído'})
        return jsonify(desenvolvedores[posicao])
    elif request.method == "GET":
        return jsonify(desenvolvedores)



if __name__ == "__main__":
    app.run(debug=True)
