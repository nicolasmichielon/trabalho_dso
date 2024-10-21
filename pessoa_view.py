class PessoaView():
    def __init__(self) -> None:
        pass

    def mostrar_moradores_ou_sindico(self, linhas: list):
        for linha in linhas:
            print(linha)

    def get_pessoa(self) -> list:
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        cpf = input("CPF: ")
        while True:
            try:
                idade = int(input("Idade: "))
                if idade > 130 or idade < 0:
                    raise ValueError
                
                return {"nome": nome, "telefone": telefone, "cpf": cpf, "idade": idade}
            except:
                print("Valor inválido!")
