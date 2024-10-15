from tipo_ocorrencia import TipoDeOcorrencia

class Ocorrencia:
    def __init__(self, id:int, morador, sindico, descricao: str, tipoDeOcorrencia: str, resolvida: bool = False):
        self.__id = id
        self.__morador = morador
        self.__sindico = sindico
        self.__descricao = descricao
        self.__resolvida = resolvida
        self.__tipoDeOcorrencia = TipoDeOcorrencia(tipoDeOcorrencia)

    @property
    def tipoDeOcorrencia(self):
        return self.__tipoDeOcorrencia

    @property
    def id(self):
        return self.__id

    @property
    def morador(self):
        return self.__morador

    @property
    def sindico(self):
        return self.__sindico

    @property
    def descricao(self):
        return self.__descricao

    @property
    def resolvida(self):
        return self.__resolvida

    @resolvida.setter
    def resolvida(self, value: bool):
        self.__resolvida = value

    @tipoDeOcorrencia.setter
    def tipoDeOcorrencia(self, tipo):
        self.__tipoDeOcorrencia = tipo
        
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
