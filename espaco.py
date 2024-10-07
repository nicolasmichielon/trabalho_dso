class Espaco:
    def __init__(self, id: int, valor_reserva: float, local: str, capacidade: int, horario_de_funcionamento: str):
        self.__id = id
        self.__valor_reserva = valor_reserva
        self.__local = local
        self.__capacidade = capacidade
        self.__horario_de_funcionamento = horario_de_funcionamento

    @property
    def id(self):
        return self.__id

    @property
    def valor_reserva(self):
        return self.__valor_reserva

    @valor_reserva.setter
    def valor_reserva(self, valor_reserva: float):
        self.__valor_reserva = valor_reserva

    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, local: str):
        self.__local = local

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade

    @property
    def horario_de_funcionamento(self):
        return self.__horario_de_funcionamento

    @horario_de_funcionamento.setter
    def horario_de_funcionamento(self, horario_de_funcionamento: str):
        self.__horario_de_funcionamento = horario_de_funcionamento