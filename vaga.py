
from tipo_de_vaga import TipoDeVaga

class Vaga:
    def __init__(self, numero: int, tipo_de_vaga: TipoDeVaga, ocupado: bool=False):
        self.__numero = numero
        self.__ocupado = ocupado
        self.__tipo_de_vaga = tipo_de_vaga

    @property
    def tipo_de_vaga(self):
        return self.__tipo_de_vaga

    @tipo_de_vaga.setter
    def tipo_de_vaga(self, value):
        self.__tipo_de_vaga = value
        
    def ocupar(self):
        self.__ocupado = True

    def desocupar(self):
        self.__ocupado = False

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, value):
        self.__numero = value

    @property
    def ocupado(self):
        return self.__ocupado

    @ocupado.setter
    def ocupado(self, value):
        self.__ocupado = value