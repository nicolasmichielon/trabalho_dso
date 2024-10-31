class Vaga:
    def __init__(self, numero: int, pessoa: str, vaga_de_morador: bool, ocupado: bool=False):
        self.__numero = numero
        self.__pessoa = pessoa
        self.__ocupado = ocupado
        self.__vaga_de_morador = vaga_de_morador

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
    def vaga_de_morador(self):
        return self.__vaga_de_morador

    @vaga_de_morador.setter
    def vaga_de_morador(self, value):
        self.__vaga_de_morador = value

    @property
    def ocupado(self):
        return self.__ocupado

    @ocupado.setter
    def ocupado(self, value):
        self.__ocupado = value