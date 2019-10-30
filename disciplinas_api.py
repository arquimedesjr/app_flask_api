from flask import Blueprint, jsonify, request
from services.disciplinas_service import \
    listar as service_listar, \
    localizar as service_localiza, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualiza

disciplinas_app = Blueprint('disciplinas_app', __name__, template_folder='templates')


@disciplinas_app.route("/disciplinas", methods=["GET"])
def listar_disciplina():
    lista = service_listar()
    return jsonify(lista)


@disciplinas_app.route('/disciplinas', methods=['POST'])
def cadastrar_aluno():
    nova_disciplina = request.get_json()
    disciplina = service_criar(nova_disciplina)
    if disciplina is None:
        return jsonify({'erro': 'Disciplina já existe'}), 400
    return jsonify(disciplina)


@disciplinas_app.route('/disciplinas/<int:id>', methods=['PUT'])
def alterar_disciplina(id):
    disciplina_data = request.get_json()
    if 'disciplinas' not in disciplina_data:
        return jsonify({'erro': 'aluno sem nome'}), 400
    atualizado = service_atualiza(id, disciplina_data['nome'], disciplina_data['status'],
                                  disciplina_data['plano_ensino'],
                                  disciplina_data['carga_horaria'])
    if atualizado != None:
        return jsonify(atualizado)
    return jsonify({'erro': 'disciplina nao encontrado'}), 400


@disciplinas_app.route('/disciplinas/<int:id>', methods=['GET'])
def localizar_disciplina(id):
    disciplina = service_localiza(id)
    if disciplina != None:
        return jsonify(disciplina)
    return jsonify({'erro': 'disciplina nao encontrado'}), 400


@disciplinas_app.route('/disciplinas/<int:id>', methods=['DELETE'])
def remover_disciplina(id):
    removido = service_remover(id)
    if removido == 1:
        return jsonify(removido), 202
    return jsonify({'erro': 'disciplina nao encontrado'}), 400
