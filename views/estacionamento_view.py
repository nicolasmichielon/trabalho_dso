class EstacionamentoView():
    def __init__(self) -> None:
        pass

    def mostrar_vagas(self, linhas: list):
        for linha in linhas:
            print(linha)

    def get_vaga(self) -> int:
        vaga = int(input("Qual vaga ira ocupar: "))
        return vaga