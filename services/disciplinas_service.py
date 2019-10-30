from infra.disciplina_dao import \
    listar as dao_listar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar, \
    alterar as dao_alterar, \
    remover as dao_remover, \
    reseta as dao_reseta


from model.disciplina import Disciplina


def listar():
    return [disciplina.__dict__() for disciplina in dao_listar()]


def localizar(id):
    disciplina = dao_consultar(id)
    if disciplina is None:
        return None
    return disciplina.__dict__()


def criar(disciplina_data):
    if localizar(disciplina_data['id']) is None:
        disciplina = Disciplina.criar(disciplina_data)
        return dao_cadastrar(disciplina)
    return None


def remover(id):
    dados_disciplina = localizar(id)
    if dados_disciplina is None:
        return 0
    dao_remover(Disciplina.criar(dados_disciplina))
    return 1
    if localizar(id) is None:
        return 0
    dao_remover(id)
    return 1


def atualizar(id, nome, status, plano_ensino, carga_horaria):
    disciplina = Disciplina.criar({"id": id, "nome": nome, "status": status, "plano_ensino": plano_ensino,
                                   "carga_horaria": carga_horaria})
    dao_alterar(disciplina)
    return localizar(id)

def reseta():
    return dao_reseta()