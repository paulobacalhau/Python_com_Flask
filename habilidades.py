from flask_restful import Resource

lista_habilidades = ['Cobol', 'Clipper', 'C++', 'Python', 'Java', 'PHP']

class Habilidades(Resource):
    def get(self):
        return(lista_habilidades)

