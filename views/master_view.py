class MasterView():
    def __init__(self) -> None:
        pass

    def mostra_opcoes(self, linhas):
        for linha in linhas:
            print(linha)

    def solicitar_resposta(self):
        return int(input("Escolha: "))
    
    def mostra_erro(self, erro:Exception):
        print(f"\n{erro()}\n")