class GastoView():
    def __init__(self) -> None:
        pass

    def mostrar_gastos(self, linhas: list):
        for linha in linhas:
            print(linha)

    def get_gasto(self) -> list:
        cpf = input("CPF: ")
        tipo = input("Tipo de gasto: ")
        while True:
            try:
                valor = int(input("Valor: "))
                return {"cpf": cpf, "tipo": tipo, "valor": valor}
            except:
                print("Valor inválido!")

    def get_cpf(self):
        cpf = input("CPF: ")
        return cpf