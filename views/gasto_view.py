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