from models.pessoa import Pessoa

class Vaga:
    def __init__(self, numero: int, pessoa: Pessoa, tipo_de_vaga: str, ocupado: bool=False):
        self.__numero = numero
        self.__pessoa = pessoa
        self.__ocupado = ocupado
        self.__tipo_de_vaga = tipo_de_vaga

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, value):
        self.__numero = value

    @property
    def pessoa(self):
        return self.__pessoa

    @pessoa.setter
    def pessoa(self, value):
        self.__pessoa = value

    @property
    def tipo_de_vaga(self):
        return self.__tipo_de_vaga

    @tipo_de_vaga.setter
    def tipo_de_vaga(self, value):
        self.__tipo_de_vaga = value

    @property
    def ocupado(self):
        return self.__ocupado

    @ocupado.setter
    def ocupado(self, value):
        self.__ocupado = value