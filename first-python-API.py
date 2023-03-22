'''
1. Objetivo: Criar um API que disponibilize a consulta, criação e exclusão de livros.
2. URL base - localhost
3. Endpoints - quais as funcionalidades do API? o endereço que a pessoa precisa digitar 
    e chamar através de uma ferramenta, como o Postman. 
    -localhost/livros (GET) - obter todos os livros
    -localhost/livros (POST) - criar um novo livro
    -localhost/livros/id(GET) - obter um livro por id
    -localhost/livros/id(PUT) - possibilidade de modificar/alterar um livro por id.
    -localhost/livros/id(DELETE) - excluir um livro pelo id.
4. Quais recursos? Livros'''


#importando as libraries do Flask
from flask import Flask, jsonify, request

#criar o aplicativo Flask; criando uma aplicação Flask com o nome do arquivo atual.

app = Flask(__name__)

#fonte de dados: armazenando dentro de um dictionary

livros = [
    {
    'id': 1,
    'título': 'O Senhor dos Anéis - A Sociedade do Anel',
    'autor': 'J.R.R Tolkien'
    },
    {
    'id': 2,
    'título': 'Harry Potter e a Pedra FIlosofal',
    'autor': 'J.K Howling'
    },
    {
    'id': 3,
    'título': 'James Clear',
    'autor': 'Hábitos Atômicos'
    }
]

'''localhost/livros (GET) - consultar todos
#posso criar uma função que vai retornar algo
#uso um decorator para que seja um api'''

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#-localhost/livros/id(GET) - consultar por id

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

'''localhost/livros/id(PUT) - editar
vou receber informação do usuário e depois preciso usar essa informação.
para receber info que foi enviada pelo usario posso usar o request'''

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

'''localhost/livros/id(DELETE) - incluir novo livro'''

@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


'''localhost/livros/id(DELETE) - excluir'''

@app.route('/livros/<int:id>', methods=['DELETE'])  
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


app.run(port=5000,host='localhost', debug=True)
