
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from app.cadastro_professores.model import Professor
from functools import wraps

def professor_jwt_required(func): 
    @wraps(func) #Pega uma função usada em um decorator e adiciona a funcionalidade de copiar sobre o nome da função wraps, a sequência de documentos, a lista de argumentos etc.
    def wrapper(*args, **kwargs):  # wrapper vai receber os argumentos que estão na rota; você acessa esses argumentos c o kwargs.get
        verify_jwt_in_request()
        professor = Professor.query.get(kwargs.get(id)) #se tem uma rota 'users/<int:id>', você verifica esse id no decorator com um kwargs.get(id)
        if kwargs.get('user_id') == get_jwt_identity(): 
            return func(*args, **kwargs)
        else: 
            return {'msg': 'permission denied'}

    return wrapper