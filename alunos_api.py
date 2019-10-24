from flask import Blueprint, jsonify, request
from services.alunos_service import \
    listar as service_listar, \
    localizar as service_localiza, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualiza

alunos_app = Blueprint('alunos_app', __name__, template_folder='templates')

alunos_db = service_listar()

# ROTAS PARA ALUNOS
@alunos_app.route("/alunos", methods = ["GET"])
def listar():
    return jsonify(alunos_db)

@alunos_app.route('/alunos', methods=['POST'])
def novo_aluno():
    novo_aluno = request.json
    if 'nome' not in novo_aluno:
        return jsonify({'erro': 'aluno sem nome'}), 404
    for aluno in alunos_db:
        if aluno['id'] == novo_aluno['id']:
            return jsonify({'erro': 'id já utilizada'}), 404
        else:
            pass
    alunos_db.append(novo_aluno)
    return jsonify(alunos_db)

@alunos_app.route('/alunos/<int:id_aluno>', methods=['GET'])
def localiza_aluno(id_aluno):
    for aluno in alunos_db:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return jsonify({'erro': 'aluno não encontrado'}), 404

@alunos_app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def edita_aluno(id_aluno):
    dados = request.json
    if 'nome' not in dados:
        return jsonify({'erro': 'aluno sem nome'}), 404
    for aluno in alunos_db:
        if aluno['id'] == id_aluno:
            aluno['nome'] = dados['nome']
            return ""
    return jsonify({'erro': 'aluno não encontrado'}), 404

@alunos_app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def deleta_aluno(id_aluno):
    cont = 0
    for aluno in alunos_db:
        if aluno['id'] == id_aluno:
            del(alunos_db[cont])
            return alunos_db
        else:
            cont += 1
    return jsonify({'erro': 'aluno não encontrado'}), 404

@alunos_app.route('/alunos/reseta', methods=['POST'])
def reseta_alunos():
    while len(alunos_db) != 0:
        del(alunos_db[0])
    return jsonify(alunos_db)