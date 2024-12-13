class Morador():
    def __init__(self, nome: str, telefone: int, cpf: int, idade: int):
        super().__init__(nome, telefone, cpf, idade)
        self.__gastos = []