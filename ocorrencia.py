from tipo_ocorrencia import TipoOcorrencia
from sindico import Sindico
from morador import Morador

class Ocorrencia:
    def __init__(self, id:int, morador:Morador, sindico: Sindico, descricao: str, tipoDeOcorrencia: TipoOcorrencia, resolvida: bool = False):
        self.__id = id
        self.__morador = morador
        self.__sindico = sindico
        self.__descricao = descricao
        self.__resolvida = resolvida
        self.__tipoDeOcorrencia = tipoDeOcorrencia

    @property
    def tipoDeOcorrencia(self):
        return self.__tipoDeOcorrencia

    @tipoDeOcorrencia.setter
    def tipoDeOcorrencia(self, tipo):
        self.__tipoDeOcorrencia = tipo

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