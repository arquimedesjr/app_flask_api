from flask import Blueprint, jsonify, request
from services.professores_service import \
    listar as service_listar, \
    localizar as service_localiza, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualiza

professores_app = Blueprint('professores_app', __name__, template_folder='templates')

professores_db = service_listar()

# ROTAS PARA PROFESSOR
@professores_app.route("/professores", methods = ["GET"])
def listar():
    return jsonify(professores_db)

@professores_app.route('/professores', methods=['POST'])
def novo_professor():
    novo_professor = request.json
    if 'nome' not in novo_professor:
        return jsonify({'erro': 'professor sem nome'}), 404
    for professor in professores_db:
        if professor['id'] == novo_professor['id']:
            return jsonify({'erro': 'id já utilizada'}), 404
        else:
            pass
    professores_db.append(novo_professor)
    return jsonify(professores_db)

@professores_app.route('/professores/<int:id_professor>', methods=['GET'])
def localiza_professor(id_professor):
    for professor in professores_db:
        if professor['id'] == id_professor:
            return jsonify(professor)
    return jsonify({'erro': 'professor não encontrado'}), 404

@professores_app.route('/professores/<int:id_professor>', methods=['PUT'])
def edita_professor(id_professor):
    dados = request.json
    if 'nome' not in dados:
        return jsonify({'erro': 'professor sem nome'}), 404
    for professor in professores_db:
        if professor['id'] == id_professor:
            professor['nome'] = dados['nome']
            return ""
    return jsonify({'erro': 'professor não encontrado'}), 404

@professores_app.route('/professores/<int:id_professor>', methods=['DELETE'])
def deleta_professor(id_professor):
    cont = 0
    for professor in professores_db:
        if professor['id'] == id_professor:
            del(professores_db[cont])
            return professores_db
        else:
            cont+=1
    return jsonify({'erro': 'professor não encontrado'}), 404

@professores_app.route('/professores/reseta', methods=['POST'])
def reseta_professores():
    while len(professores_db) != 0:
        del(professores_db[0])
    return jsonify(professores_db)