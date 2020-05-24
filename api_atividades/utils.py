from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome="Fonseca", idade=60)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all() #filter_by(nome="Paulo")
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome="Coucello").first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome="paulo bacalhau").first()
    pessoa.idade = 58
    pessoa.nome = 'Coucello'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Fonseca").first()
    pessoa.delete()

def insere_usuarios():
    usuario = Usuarios(login="Paulo", senha='12345')
    print(usuario)
    usuario.save()
    usuario = Usuarios(login="Bacalhau", senha='12345678')
    print(usuario)
    usuario.save()

def consulta_usuarios():
    usuario = Usuarios.query.all() #filter_by(nome="Paulo")
    print(usuario)

if __name__ == "__main__":
    #insere_pessoas()
    #altera_pessoa()
    #consulta_pessoas()
    #exclui_pessoa()
    #consulta_pessoas()
    ##insere_usuarios()
    consulta_usuarios()
