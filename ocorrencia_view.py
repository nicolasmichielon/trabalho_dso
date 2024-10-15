class OcorrenciaView():
    def __init__(self):
        pass

    def mostra_ocorrencias(self, linhas: list):
        for linha in linhas:
            print(linha)

    def get_name(self):
        return input("Nome: ")
    
    def get_ocorrencia(self):
        id = input("Id: ")
        morador = input("Nome do morador: ")
        descricao = input("Descrição: ")
        tipo = input("Tipo ( 0 - agua, 1 - cachorro, 2 - gato ): ")
        return [id, morador, descricao, tipo]