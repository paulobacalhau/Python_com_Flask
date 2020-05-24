from flask import Flask, request
from flask_restful import Api, Resource
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)
# Esta classe consulta, altera e deleta um desenvolvedor
class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome = nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except:
            response ={'status': 'erro', 'mensagem':'Pessoa {} nao existe'.format(nome)}    
        return response

    def post(self):    
        pass

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome = nome).first()
        mensagem = "Pessoa {} excluída com sucesso".format(nome)
        return {'status': 'Sucesso', 'mensagem':mensagem}

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome = nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
            }
        return (response)    

# Esta classe permite incluir um desenvolvedor ou listar todos
class ListaPessoas(Resource):
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
            }
        return (response)    
    
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
        return(response)

# Esta classe permite incluir uma atividade ou listar todas
class ListaAtividades(Resource):
    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome = dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'id': atividade.id,
            'nome': atividade.nome,
            'pessoa': atividade.pessoa.nome
            }
        return (response)    
    
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id':i.id, 'pessoa':i.pessoa.nome, 'nome':i.nome} for i in atividades]
        return(response)


api.add_resource(Pessoa,'/pessoa/<string:nome>/')
api.add_resource(ListaPessoas,'/pessoa/')
api.add_resource(ListaAtividades,'/atividades/')

if __name__ == "__main__":
    app.run(debug=True)
