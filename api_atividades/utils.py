from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome="Fonseca", idade=60)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all() #filter_by(nome="Paulo")
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome="Paulo").first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Paulo").first()
    pessoa.idade = 30

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Fonseca").first()
    pessoa.delete()

if __name__ == "__main__":
    #insere_pessoas()
    #altera_pessoa()
    consulta_pessoas()
    exclui_pessoa()
    consulta_pessoas()