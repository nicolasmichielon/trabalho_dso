class OcorrenciaView():
    def __init__(self):
        pass

    def mostra_ocorrencias(self, linhas: list):
        for linha in linhas:
            print(linha)

    def get_cpf(self):
        return input("CPF: ")
    
    def get_ocorrencia(self, last_id):
        id = last_id + 1
        cpf = input("CPF do morador: ")
        descricao = input("Descrição: ")
        tipo = input("Tipo ( 0 - agua, 1 - cachorro, 2 - gato ): ")
        return [id, cpf, descricao, tipo]