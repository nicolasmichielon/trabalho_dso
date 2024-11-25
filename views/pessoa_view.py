from exceptions.cpf_invalido_exception import CPFInvalidoException
from exceptions.idade_invalida_exception import IdadeInvalidaException
from exceptions.telefone_invalido_exception import TelefoneInvalidoException
from exceptions.nome_invalido_exception import NomeInvalidoException

class PessoaView():
    def __init__(self) -> None:
        pass

    def mostrar_pessoa(self, linhas: list):
        for linha in linhas:
            print(linha)

    def get_pessoa(self) -> dict:
        while True:
            try:
                nome = input("Nome: ")
                if len(nome) < 2:
                    raise NomeInvalidoException()
                break
            except NomeInvalidoException as e:
                print(e)
        
        while True:
            try:
                telefone = input("Telefone: ")
                if len(telefone) < 11 or not telefone.isdigit():
                    raise TelefoneInvalidoException()
                break
            except TelefoneInvalidoException as e:
                print(e)

        while True:
            try:
                cpf = input("CPF: ")
                if len(cpf) != 11 or not cpf.isdigit():
                    raise CPFInvalidoException()
                cpf = int(cpf)
                break
            except CPFInvalidoException as e:
                print(e)
        
        while True:
            try:
                idade = int(input("Idade: "))
                if idade > 130 or idade < 0:
                    raise IdadeInvalidaException()
                break
            except IdadeInvalidaException as e:
                print(e)
        
        return {"nome": nome, "telefone": telefone, "cpf": cpf, "idade": idade}

    def get_cpf(self) -> int:
        while True:
            try:
                cpf = input("CPF: ")
                if len(cpf) != 11 or not cpf.isdigit():
                    raise CPFInvalidoException()
                cpf = int(cpf)
                break
            except CPFInvalidoException as e:
                print(e)
        return cpf

    def mostra_linhas(self, linhas: list):
        for linha in linhas:
            print(linha)

    def pessoa_repetida(self, msg):
        print(msg)