from exceptions.dados_invalidos_exception import DadosInvalidosException

class OcorrenciaView():
    def __init__(self):
        pass

    def mostra_ocorrencias(self, linhas: list):
        for linha in linhas:
            print(linha)

    def get_cpf(self):
        return int(input("CPF: "))
    
    def get_ocorrencia(self, last_id):
        id = last_id + 1
        cpf = int(input("CPF do morador: "))
        descricao = input("Descrição: ")
        while True:
            try:
                tipo = int(input("Tipo ( 0 - agua, 1 - cachorro, 2 - gato ): "))
                return {"id": id, "cpf": cpf, "descricao": descricao, "tipo": tipo}
            except:
                print(DadosInvalidosException())
        