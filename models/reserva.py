from models.espaco import Espaco
from models.gasto import Gasto
from models.morador import Morador

class Reserva:
    def __init__(self, id: int, solicitante: Morador, data_reserva, hora_inicio, hora_fim, espaco: str):
        self.__id = id
        self.__solicitante = solicitante
        self.__data_reserva = data_reserva
        self.__hora_inicio = hora_inicio
        self.__hora_fim = hora_fim
        # implementar self.__gasto, talvez chamar gasto controller para adicionar o gasto da reserva para o morador
        self.__custo = (hora_fim - hora_inicio)*50
        self.__espaco = espaco

    @property
    def id(self):
        return self.__id
    
    @property
    def custo(self):
        return self.__custo

    @property
    def solicitante(self):
        return self.__solicitante

    @property
    def data_reserva(self):
        return self.__data_reserva

    @property
    def hora_inicio(self):
        return self.__hora_inicio

    @property
    def hora_fim(self):
        return self.__hora_fim

    @property
    def espaco(self):
        return self.__espaco

    @solicitante.setter
    def solicitante(self, value):
        self.__solicitante = value

    @data_reserva.setter
    def data_reserva(self, value):
        self.__data_reserva = value

    @hora_inicio.setter
    def hora_inicio(self, value):
        self.__hora_inicio = value

    @hora_fim.setter
    def hora_fim(self, value):
        self.__hora_fim = value

    @espaco.setter
    def espaco(self, value: Espaco):
        self.__espaco = value