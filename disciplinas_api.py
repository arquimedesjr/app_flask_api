from flask import Blueprint, jsonify, request
from services.disciplinas_service import \
    listar as service_listar, \
    localizar as service_localiza, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualiza

disciplinas_app = Blueprint('disciplinas_app', __name__, template_folder='templates')

disciplinas_db = service_listar()

# ROTAS PARA DISCIPLINA
@disciplinas_app.route("/disciplinas", methods = ["GET"])
def listar():
    return jsonify(disciplinas_db)

@disciplinas_app.route('/disciplinas', methods=['POST'])
def nova_disciplina():
    nova_disciplina = request.json
    if 'id' not in nova_disciplina or 'nome' not in nova_disciplina or 'status' not in nova_disciplina or 'plano_ensino' not in nova_disciplina or 'carga_horaria' not in nova_disciplina:
        return jsonify({'erro': 'faltam campos'}), 404
    for disciplina in disciplinas_db:
        if disciplina['id'] == nova_disciplina['id']:
            return jsonify({'erro': 'id já utilizada'}), 404
        else:
            pass
    # if 'id_coordenador' in nova_disciplina:
    #     for professor in professores_db:
    #         if professor['id'] == nova_disciplina['id_coordenador']:
    #             disciplinas_db.append(nova_disciplina)
    #             return jsonify(disciplinas_db)
    #         else:
    #             pass
    #     return jsonify({'erro': 'coordenador não encontrado'}), 404
    disciplinas_db.append(nova_disciplina)
    return jsonify(disciplinas_db)


@disciplinas_app.route('/disciplinas/<int:id_disciplina>', methods=['GET'])
def localiza_disciplina(id_disciplina):
    for disciplina in disciplinas_db:
        if disciplina['id'] == id_disciplina:
            return jsonify(disciplina)
    return jsonify({'erro': 'disciplina não encontrada'}), 404


@disciplinas_app.route('/disciplinas/<int:id_disciplina>', methods=['PUT'])
def edita_disciplina(id_disciplina):
    dados = request.json
    if 'nome' not in dados:
        return jsonify({'erro': 'disciplina sem nome'}), 404
    for disciplina in disciplinas_db:
        if disciplina['id'] == id_disciplina:
            disciplina['nome'] = dados['nome']
            disciplina['status'] = dados['status']
            disciplina['plano_ensino'] = dados['plano_ensino']
            disciplina['carga_horaria'] = dados['carga_horaria']
            return ""
    return jsonify({'erro': 'disciplina não encontrada'}), 404


@disciplinas_app.route('/disciplinas/<int:id_disciplina>', methods=['DELETE'])
def deleta_disciplina(id_disciplina):
    cont = 0
    for disciplina in disciplinas_db:
        if disciplina['id'] == id_disciplina:
            del(disciplinas_db[cont])
            return disciplinas_db
        else:
            cont += 1
    return jsonify({'erro': 'disciplina não encontrada'}), 404


@disciplinas_app.route('/disciplinas/reseta', methods=['POST'])
def reseta_disciplinas():
    while len(disciplinas_db) != 0:
        del(disciplinas_db[0])
    return jsonify(disciplinas_db)