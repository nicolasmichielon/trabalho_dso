from models.morador import Morador

class Gasto():
    def __init__(self, id: int, valor:float, morador:Morador, pago:bool, tipo_de_gasto:str):
        self.__id = id
        self.__valor = valor
        self.__morador = morador
        self.__pago = pago
        self.__tipo_de_gasto = tipo_de_gasto

    @property
    def id(self):
        return self.__id

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
    def morador(self):
        return self.__morador

    @morador.setter
    def morador(self, morador: Morador):
        self.__morador = morador

    @property
    def pago(self):
        return self.__pago

    @pago.setter
    def pago(self, pago: bool):
        self.__pago = pago