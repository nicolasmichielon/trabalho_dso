from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, telefone: str, cpf: str, idade: int):
        self.__nome = nome
        self.__telefone = telefone
        self.__cpf = cpf
        self.__idade = idade

    @abstractmethod
    def abstract_method(self):
        None

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str = None):
        if telefone is not None:
            self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str = None):
        if nome is not None:
            self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str = None):
        if cpf is not None:
            self.__cpf = cpf

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int = None):
        if idade is not None:
            self.__idade = idade