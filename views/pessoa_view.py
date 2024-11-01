class PessoaView():
    def __init__(self) -> None:
        pass

    def mostrar_pessoa(self, linhas: list):
        for linha in linhas:
            print(linha)

    def get_pessoa(self) -> dict:
        while True:
            try:
                nome = input("Nome: ")
                if len(nome) < 2:
                    raise ValueError
                break
            except ValueError:
                print("Nome inválido! Deve ter pelo menos 2 caracteres.")
        
        while True:
            try:
                telefone = input("Telefone: ")
                if len(telefone) < 11 or not telefone.isdigit():
                    raise ValueError
                break
            except ValueError:
                print("Telefone inválido! Deve conter pelo menos 11 dígitos numéricos.")

        while True:
            try:
                cpf = input("CPF: ")
                if len(cpf) != 11 or not cpf.isdigit():
                    raise ValueError
                cpf = int(cpf)
                break
            except ValueError:
                print("CPF inválido! Deve conter 11 dígitos numéricos.")
        
        while True:
            try:
                idade = int(input("Idade: "))
                if idade > 130 or idade < 0:
                    raise ValueError
                break
            except ValueError:
                print("Idade inválida! Deve ser um número entre 0 e 130.")
        
        return {"nome": nome, "telefone": telefone, "cpf": cpf, "idade": idade}

    def get_cpf(self) -> str:
        cpf = input("CPF: ")
        return cpf

    def pessoa_repetida(self, msg):
        print(msg)