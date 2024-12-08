from daos.dao import DAO
from exceptions.pessoa_repetida_exception import PessoaRepetidaException
from models.estacionamento import Estacionamento
from models.morador import Morador
from models.sindico import Sindico
from models.visitante import Visitante

class EstacionamentoDAO(DAO):
    def __init__(self):
        super().__init__('vagas.pkl')

    def initialize_vagas(self, estacionamento: Estacionamento):
        self.add("estacionamento", estacionamento)

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
        return self.get("estacionamento").vagas
