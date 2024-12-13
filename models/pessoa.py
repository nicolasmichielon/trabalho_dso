class Pessoa():
    def __init__(self, nome: str, telefone: str, cpf: str, idade: int):
        if not nome or not isinstance(nome, str):
            raise ValueError("O atributo 'nome' deve ser uma string válida.")
        if not telefone or not isinstance(telefone, str):
            raise ValueError("O atributo 'telefone' deve ser uma string válida.")
        if not cpf:
            raise ValueError("O atributo 'cpf' deve ser uma string numérica com 11 dígitos.")
        if not isinstance(idade, int) or idade <= 0:
            raise ValueError("O atributo 'idade' deve ser um número inteiro positivo.")
        
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.idade = idade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if not nome or not isinstance(nome, str):
            raise ValueError("O nome deve ser uma string válida.")
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        if not telefone or not isinstance(telefone, str):
            raise ValueError("O telefone deve ser uma string válida.")
        self.__telefone = telefone

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if not cpf:
            raise ValueError("O CPF deve ser uma string numérica com 11 dígitos.")
        self.__cpf = cpf

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        if not isinstance(idade, int) or idade <= 0:
            raise ValueError("A idade deve ser um número inteiro positivo.")
        self.__idade = idade
