from exceptions.dados_invalidos_exception import DadosInvalidosException
from exceptions.cpf_invalido_exception import CPFInvalidoException
from exceptions.id_invalido_exception import IDInvalidoException

class GastoView():
    def __init__(self) -> None:
        pass

    def mostrar_gastos(self, linhas: list):
        for linha in linhas:
            print(linha)

    def get_gasto(self) -> list:
        tipo = input("Tipo de gasto: ")
        while True:
            try:
                valor = int(input("Valor: "))
                return {"tipo": tipo, "valor": valor}
            except:
                print(DadosInvalidosException())

    def get_cpf(self):
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
    
    def get_gasto_id(self):
        while True:
            try:
                id = input("ID do gasto a ser pago: ")
                if not id.isdigit():
                    raise IDInvalidoException()
                id = int(id)
                break
            except IDInvalidoException as e:
                print(e)
        return id
    
    def mostra_linhas(self, linhas: list):
        for linha in linhas:
            print(linha)
    
    def gasto_pago(self):
        print("Gasto pago com sucesso!")