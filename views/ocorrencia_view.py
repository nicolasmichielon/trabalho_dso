import PySimpleGUI as sg
from exceptions.dados_invalidos_exception import DadosInvalidosException
from exceptions.descricao_invalida_exception import DescricaoInvalidaException
from exceptions.cpf_invalido_exception import CPFInvalidoException

class OcorrenciaView():
    def __init__(self):
        pass

    def mostra_ocorrencias(self, linhas: list):
        layout = [[sg.Text(linha)] for linha in linhas] + [[sg.Button('OK')]]
        window = sg.Window('Ocorrências', layout)
        event, values = window.read()
        window.close()

    def mostra_linhas(self, linhas: list):
        layout = [[sg.Text(linha)] for linha in linhas] + [[sg.Button('OK')]]
        window = sg.Window('Linhas', layout)
        event, values = window.read()
        window.close()

    def get_cpf(self):
        while True:
            layout = [[sg.Text('CPF:'), sg.InputText(key='cpf')],
                      [sg.Button('Enviar')]]
            window = sg.Window('CPF Input', layout)
            event, values = window.read()
            window.close()
            cpf = values['cpf']
            try:
                if len(cpf) != 11 or not cpf.isdigit():
                    raise CPFInvalidoException()
                cpf = int(cpf)
                break
            except CPFInvalidoException as e:
                sg.popup(e)
        return cpf

    def get_ocorrencia(self, last_id):
        id = last_id + 1

        while True:
            layout = [[sg.Text('CPF do morador:'), sg.InputText(key='cpf')],
                      [sg.Text('Descrição:'), sg.InputText(key='descricao')],
                      [sg.Button('Enviar')]]
            window = sg.Window('Nova Ocorrência', layout)
            event, values = window.read()
            window.close()
            cpf = values['cpf']
            descricao = values['descricao']
            try:
                if len(cpf) != 11 or not cpf.isdigit():
                    raise CPFInvalidoException()
                cpf = int(cpf)
                if len(descricao) < 6:
                    raise DescricaoInvalidaException()
                return {"id": id, "cpf": cpf, "descricao": descricao}
            except (CPFInvalidoException, DescricaoInvalidaException) as e:
                sg.popup(e)
            except:
                sg.popup(DadosInvalidosException())
