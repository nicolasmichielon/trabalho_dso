from models.visitante import Visitante
from models.morador import Morador
from models.sindico import Sindico

class Condominio():
    def __init__(self, id: int, endereco: str, nome: str):
        self.__id = id
        self.__endereco = endereco
        self.__nome = nome
        self.__espacos = []
        self.__moradores = []
        self.__visitantes = []
        self.__estacionamento = None
        self.__sindico = None

    @property
    def estacionamento(self):
        return self.__estacionamento

    @estacionamento.setter
    def estacionamento(self, estacionamento):
        self.__estacionamento = estacionamento
        
    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco

    @property
    def espacos(self):
        return self.__espacos
    
    def adicionar_espaco(self, espaco):
        self.__espacos.append(espaco)

    @espacos.setter
    def espacos(self, espacos: list):
        self.__espacos = espacos

    def adicionar_visitante(self, visitante:Visitante):
        self.__visitantes.append(visitante)

    def adicionar_morador(self, morador:Morador):
        self.__moradores.append(morador)

    def trocar_sindico(self, sindico_antigo: Sindico, sindico_novo: Sindico):
        if self.__sindico == sindico_antigo:
            self.__sindico = sindico_novo
        else:
            raise ValueError("O síndico antigo não corresponde ao síndico atual.")