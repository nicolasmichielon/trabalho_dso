from exceptions.dados_invalidos_exception import DadosInvalidosException

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
        return int(input("CPF: "))