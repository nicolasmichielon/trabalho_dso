class PessoaView():
    def __init__(self) -> None:
        pass

    def mostrar_moradores_ou_sindico(self, linhas: str):
        for linha in linhas:
            print(linha)

    def get_pessoa(self) -> list:
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        cpf = input("CPF: ")
        idade = int(input("Idade: "))
        return [nome, telefone, cpf, idade]