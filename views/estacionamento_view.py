from exceptions.vaga_invalida_exception import VagaInvalidaException
from exceptions.cpf_invalido_exception import CPFInvalidoException
import PySimpleGUI as sg

class EstacionamentoView():
    def __init__(self) -> None:
        pass

    def mostra_linhas(self, linhas: list):
        layout = [[sg.Text(linha)] for linha in linhas] + [[sg.Button('Ok')]]
        window = sg.Window('Mostrar Linhas', layout)
        event, values = window.read()
        window.close()
        return None

    def mostrar_vagas(self, linhas: list):
        layout = [[sg.Text(linha)] for linha in linhas] + [[sg.Button('Ok')]]
        window = sg.Window('Mostrar Vagas', layout)
        event, values = window.read()
        window.close()
        return None

    def get_vaga(self):
        layout = [
            [sg.Text('Vaga:'), sg.InputText(key='vaga')],
            [sg.Button('Enviar')]
        ]
        window = sg.Window('Entrada de Vaga', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return None

            try:
                vaga = int(values['vaga'])
                if not (1 <= vaga <= 15):
                    raise VagaInvalidaException()
                window.close()
                return vaga
            except (ValueError, VagaInvalidaException) as e:
                sg.popup(str(e))
