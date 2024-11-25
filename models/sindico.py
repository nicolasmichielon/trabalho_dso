from models.pessoa import Pessoa

class Sindico(Pessoa):
    def __init__(self, nome: str, telefone: str, cpf: str, idade: int):
        super().__init__(nome, telefone, cpf, idade)

    def random_method(self):
        return None
