from morador import Morador
from tipo_de_gasto import TipoDeGasto


class Gasto():
    def __init__(self, valor:float, cpf:str, pago:bool, tipo_de_gasto:TipoDeGasto):
        self.__valor = valor
        self.__cpf = cpf
        self.__pago = pago
        self.__tipo_de_gasto = tipo_de_gasto

    @property
    def tipo_de_gasto(self):
        return self.__tipo_de_gasto

    @tipo_de_gasto.setter
    def tipo_de_gasto(self, tipo_de_gasto: float):
        self.__tipo_de_gasto = tipo_de_gasto

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def pago(self):
        return self.__pago

    @pago.setter
    def pago(self, pago: bool):
        self.__pago = pago