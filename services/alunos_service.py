from infra.alunos_dao import \
    listar as dao_listar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar, \
    alterar as dao_alterar, \
    remover as dao_remover

from model.aluno import Aluno


def listar():
    return [aluno.__dict__() for aluno in dao_listar()]


def localizar(id):
    aluno = dao_consultar(id)
    if aluno == None:
        return None
    return aluno.__dict__()


def criar(aluno_data):
    if localizar(aluno_data['id']) is None:
        aluno = Aluno.criar(aluno_data)
        professor = dao_cadastrar(aluno)
        return professor
    return None


def remover(id):
    dados_aluno = localizar(id)
    if dados_aluno is None:
        return 0
    dao_remover(Aluno.criar(dados_aluno))
    return 1


def atualizar(id, nome):
    aluno = Aluno.criar({"id": id, "nome":nome})
    dao_alterar(aluno)
    return localizar(id)