from daos.dao import DAO

class EstacionamentoDAO(DAO):
    def __init__(self):
        super().__init__('vagas.pkl')

    def adicionar_vaga(self, pessoa):
        if isinstance(pessoa, (Morador, Visitante, Sindico)):
            if pessoa.cpf not in [p.cpf for p in self.get_all()]:
                self.add(pessoa.cpf, pessoa)
            else:
                raise PessoaRepetidaException(pessoa.cpf)

    def remover_pessoa(self, cpf, tipo):
        pessoa = self.get(cpf)
        if isinstance(pessoa, tipo):
            self.remove(cpf)

    def buscar_pessoa_por_cpf(self, cpf, tipo):
        pessoa = self.get(cpf)
        if isinstance(pessoa, tipo):
            return pessoa
        return None

    def get_vagas(self):
        return self.get_all()
