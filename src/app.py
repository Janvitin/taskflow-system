from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = []

@app.route('/')
def home():
    return "Sistema de Gerenciamento de Tarefas"


@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)


@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.json
    tarefas.append(dados)

    return jsonify({
        "mensagem": "Tarefa criada com sucesso"
    }), 201


if __name__ == '__main__':
    app.run(debug=True)