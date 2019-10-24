class Disciplina():
    def __init__(self, id, nome, status, plano_ensino, carga_horaria):
        self.id = id
        self.nome = nome
        self.status = status
        self.plano_ensino = plano_ensino
        self.carga_hotaria = carga_horaria

    def atualizar(self, dados):
        try:
            id = dados["id"]
            nome = dados["nome"]
            status = dados["status"]
            plano_ensino = dados["plano_ensino"]
            carga_horaria = dados["carga_horaria"]

            self.id, self.nome, self.status, self.plano_ensino, self.carga_hotaria = id, nome, status, plano_ensino, carga_horaria
            return self
        except Exception as e:
            print("Problema ao criar novo aluno!")
            print(e)

    def __dict__(self):
        d = dict()
        d['id'] = self.id
        d['nome'] = self.nome
        d['status'] = self.status
        d['plano_ensino'] = self.plano_ensino
        d['carga_horaria'] = self.carga_hotaria
        return d

    @staticmethod
    def criar(dados):
        try:
            id = dados["id"]
            nome = dados["nome"]
            status = dados["status"]
            plano_ensino = dados["plano_ensino"]
            carga_horaria = dados["carga_horaria"]
            return Disciplina(id=id, nome=nome, status=status, plano_ensino=plano_ensino, carga_horaria=carga_horaria)
        except Exception as e:
            print("Problema ao criar novo aluno!")
            print(e)
