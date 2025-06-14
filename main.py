from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulando um "banco de dados" em memória
livros = [
    {"id": 1, "titulo": "O Alquimista", "autor": "Paulo Coelho"},
    {"id": 2, "titulo": "1984", "autor": "George Orwell"}
]


# Rota GET para listar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros), 200


# Rota POST para adicionar um novo livro
@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro), 201


# Rota PUT para atualizar um livro pelo ID
@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    livro_atualizado = request.get_json()
    for livro in livros:
        if livro["id"] == id:
            livro.update(livro_atualizado)
            return jsonify(livro), 200
    return jsonify({"erro": "Livro não encontrado"}), 404


# Rota DELETE para remover um livro pelo ID
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    for livro in livros:
        if livro["id"] == id:
            livros.remove(livro)
            return jsonify({"mensagem": "Livro removido"}), 200
    return jsonify({"erro": "Livro não encontrado"}), 404


# Executa o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
