from exceptions.vaga_invalida_exception import VagaInvalidaException
from exceptions.cpf_invalido_exception import CPFInvalidoException

class EstacionamentoView():
    def __init__(self) -> None:
        pass

    def mostra_linhas(self, linhas: list):
        for linha in linhas:
            print(linha)

    def mostrar_vagas(self, linhas: list):
        for linha in linhas:
            print(linha)

    def get_vaga(self) -> int:
        while True:
            try:
                vaga = int(input("Vaga: "))
                if not vaga >= 1 and not vaga <= 15:
                    raise VagaInvalidaException()
                break
            except VagaInvalidaException as e:
                print(e)
        return vaga
    
    def get_cpf(self) -> int:
        while True:
            try:
                cpf = input("CPF: ")
                if len(cpf) != 11 or not cpf.isdigit():
                    raise CPFInvalidoException()
                break
            except CPFInvalidoException as e:
                print(e)
        return int(cpf)