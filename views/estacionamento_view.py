from exceptions.vaga_invalida_exception import VagaInvalidaException
from exceptions.cpf_invalido_exception import CPFInvalidoException

class EstacionamentoView():
    def __init__(self) -> None:
        pass

    def mostra_linhas(self, linhas: list):
        layout = [[sg.Text(linha)] for linha in linhas] + [[sg.Button('Ok')]]
        window = sg.Window('Mostrar Linhas', layout)
        event = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            window.close()
            return None

    def mostrar_vagas(self, linhas: list):
        layout = [[sg.Text(linha)] for linha in linhas] + [[sg.Button('Ok')]]
        window = sg.Window('Mostrar Vagas', layout)
        event = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            window.close()
            return None

    def get_vaga(self) -> int:
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

    def get_cpf(self) -> int:
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
