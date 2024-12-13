from daos.dao import DAO
from models.morador import Morador
from models.visitante import Visitante
from models.sindico import Sindico
from exceptions.pessoa_repetida_exception import PessoaRepetidaException

class PessoaDAO(DAO):
    def __init__(self):
        super().__init__('pessoas.pkl')

    def adicionar_pessoa(self, pessoa):
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

    def get_moradores(self):
        return [p for p in self.get_all() if isinstance(p, Morador)]

    def get_visitantes(self):
        return [p for p in self.get_all() if isinstance(p, Visitante)]
    
    def get_sindico(self):
        try:
            sindico = [p for p in self.get_all() if isinstance(p, Sindico)][0]
        except:
            sindico = None
        return sindico
