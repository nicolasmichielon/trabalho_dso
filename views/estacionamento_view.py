class EstacionamentoView():
    def __init__(self) -> None:
        pass

    def mostrar_vagas(self, linhas: list):
        for linha in linhas:
            print(linha)

    def get_vaga(self) -> int:
        while True:
            try:
                vaga = int(input("Vaga: "))
                if not vaga >= 1 and not vaga <= 15:
                    raise ValueError
                break
            except ValueError:
                print("A Vaga escolhida é inválida!")
        return vaga
    
    def get_cpf(self) -> int:
        while True:
            try:
                cpf = input("CPF: ")
                if len(cpf) != 11 or not cpf.isdigit():
                    raise ValueError
                break
            except ValueError:
                print("CPF inválido! Deve conter 11 dígitos numéricos.")
        return int(cpf)