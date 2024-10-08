from pessoa import Pessoa
# from ocorrencia import Ocorrencia
from sindico import Sindico
from registro_ocorrencias import RegistroOcorrencias
from tipo_ocorrencia import TipoDeOcorrencia

class Morador(Pessoa):
    def __init__(self, nome: str, telefone: int, cpf: int, idade: int):
        super().__init__(nome, telefone, cpf, idade)
        self.__gastos = []

    # def criar_ocorrencia(self, descricao: str, sindico: Sindico, moradores: list, registro: RegistroOcorrencias, tipo_de_ocorrencia:TipoDeOcorrencia, resolvida: bool = False):
    #     ocorrencia = Ocorrencia(self, sindico, descricao, tipo_de_ocorrencia)
        
