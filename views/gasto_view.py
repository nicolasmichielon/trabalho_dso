import PySimpleGUI as sg
from exceptions.dados_invalidos_exception import DadosInvalidosException
from exceptions.cpf_invalido_exception import CPFInvalidoException
from exceptions.id_invalido_exception import IDInvalidoException
from exceptions.valor_invalido_exception import ValorInvalidoException
from exceptions.descricao_invalida_exception import DescricaoInvalidaException

class GastoView:
    def __init__(self) -> None:
        pass

    def mostrar_gasto(self, linhas: list):
        layout = [[sg.Text(linha)] for linha in linhas] + [[sg.Button('Ok')]]
        window = sg.Window('Mostrar Gasto', layout)
        event, values = window.read()
        window.close()
        return None

    def get_gasto(self) -> dict:
        layout = [
            [sg.Text('Descrição:'), sg.InputText(key='descricao')],
            [sg.Text('Valor:'), sg.InputText(key='valor')],
            [sg.Button('Enviar')]
        ]
        window = sg.Window('Cadastro de Gasto', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Sair':
                window.close()
                return None

            try:
                descricao = values['descricao']
                if len(descricao) < 5:
                    raise DescricaoInvalidaException()
                
                valor = values['valor']
                if not valor.replace('.', '', 1).isdigit():
                    raise ValorInvalidoException()
                valor = float(valor)
                
                window.close()
                return {"descricao": descricao, "valor": valor}
            except (DescricaoInvalidaException, ValorInvalidoException) as e:
                sg.popup(str(e))

    def get_cpf(self):
        layout = [
            [sg.Text('CPF:'), sg.InputText(key='cpf')],
            [sg.Button('Enviar')]
        ]
        window = sg.Window('Entrada de CPF', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return None

            try:
                cpf = values['cpf']
                if len(cpf) != 11 or not cpf.isdigit():
                    raise CPFInvalidoException()
                cpf = int(cpf)
                window.close()
                return cpf
            except CPFInvalidoException as e:
                sg.popup(str(e))

    def get_gasto_id(self):
        layout = [
            [sg.Text('ID do gasto a ser deletado:'), sg.InputText(key='id')],
            [sg.Button('Enviar')]
        ]
        window = sg.Window('Entrada de ID do Gasto', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return None

            try:
                id = values['id']
                if not id.isdigit():
                    raise IDInvalidoException()
                id = int(id)
                window.close()
                return id
            except IDInvalidoException as e:
                sg.popup(str(e))

    def mostra_linhas(self, linhas: list):
        layout = [[sg.Text(linha)] for linha in linhas] + [[sg.Button('Ok')]]
        window = sg.Window('Mostrar Linhas', layout)
        event, values = window.read()
        window.close()
        return None

    def gasto_pago(self):
        sg.popup("Gasto pago com sucesso!")