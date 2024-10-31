from models.pessoa import Pessoa

class Visitante(Pessoa):
    def __init__(self, nome: str, telefone: str, cpf: str, idade: int):
        super().__init__(nome, telefone, cpf, idade)