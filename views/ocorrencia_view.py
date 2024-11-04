from exceptions.dados_invalidos_exception import DadosInvalidosException
from exceptions.descricao_invalida_exception import DescricaoInvalidaException
from exceptions.cpf_invalido_exception import CPFInvalidoException

class OcorrenciaView():
    def __init__(self):
        pass

    def mostra_ocorrencias(self, linhas: list):
        for linha in linhas:
            print(linha)

    def get_cpf(self):
        while True:
            try:
                cpf = input("CPF: ")
                if len(cpf) != 11 or not cpf.isdigit():
                    raise CPFInvalidoException()
                cpf = int(cpf)
                break
            except CPFInvalidoException as e:
                print(e)
        return cpf
    
    def get_ocorrencia(self, last_id):
        id = last_id + 1

        while True:
            try:
                cpf = input("CPF do morador: ")
                if len(cpf) != 11 or not cpf.isdigit():
                    raise CPFInvalidoException()
                cpf = int(cpf)
                break
            except CPFInvalidoException as e:
                print(e)
                
        while True:
            try:
                descricao = input("Descrição: ")
                if len(descricao) < 6:
                    raise DescricaoInvalidaException()
                break
            except DescricaoInvalidaException as e:
                print(e)

        while True:
            try:
                return {"id": id, "cpf": cpf, "descricao": descricao}
            except:
                print(DadosInvalidosException())
        