from flask import Flask, request
from flask_restful import Api, Resource
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

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
# Esta classe consulta, altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = "Desenvolvedor com ID {} não existe".format(id)
            response = {'status':'Completado com sucesso', 'mensagem':mensagem}
        except Exception:
            mensagem = "Erro desconhecido! Procure o administrador"
            response = {'status':'Completado com sucesso', 'mensagem':mensagem}
        return (response)

    def put(self, id):    
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return (dados)

    def delete(self, id):
        desenvolvedores.pop(id)
        return ({'status':'Completado com sucesso', 'mensagem':'Registro exluído'})

    def post(self):
        pass

# Esta classe permite incluir um desenvolvedor ou listar todos
class ListaDesenvolvedores(Resource):
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return (desenvolvedores[posicao])
    
    def get(self):
        return (desenvolvedores)


api.add_resource (Desenvolvedor, "/dev/<int:id>/")
api.add_resource (ListaDesenvolvedores, "/dev/")
api.add_resource (Habilidades, "/habilidades/")

if __name__ == "__main__":
    app.run()
