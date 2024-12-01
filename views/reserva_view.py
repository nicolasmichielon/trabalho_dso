import PySimpleGUI as sg
from exceptions.cpf_invalido_exception import CPFInvalidoException
from exceptions.data_invalida_exception import DataInvalidaException
from exceptions.espaco_invalido_exception import EspacoInvalidoException
from exceptions.horario_invalido_exception import HorarioInvalidoException
from exceptions.id_invalido_exception import IDInvalidoException

class ReservaView:
    def __init__(self) -> None:
        pass

    def mostraReserva(self, linhas: list):
        layout = [[sg.Text(linha)] for linha in linhas] + [[sg.Button('Ok')]]
        window = sg.Window('Mostrar Reserva', layout)
        event, values = window.read()
        window.close()

    def get_reserva(self) -> dict:
        layout = [
            [sg.Text('CPF do solicitante:'), sg.InputText(key='cpf_solicitante')],
            [sg.Text('Data da reserva:'), sg.InputText(key='data_reserva')],
            [sg.Text('Hora de início:'), sg.InputText(key='hora_inicio')],
            [sg.Text('Hora de fim:'), sg.InputText(key='hora_fim')],
            [sg.Text('Espaço:'), sg.InputText(key='espaco')],
            [sg.Button('Enviar')]
        ]
        window = sg.Window('Cadastro de Reserva', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Sair':
                window.close()
                return None

            try:
                cpf_solicitante = values['cpf_solicitante']
                if len(cpf_solicitante) != 11 or not cpf_solicitante.isdigit():
                    raise CPFInvalidoException()
                cpf_solicitante = int(cpf_solicitante)
                
                data_reserva = values['data_reserva']
                if len(data_reserva) < 10:
                    raise DataInvalidaException()
                
                hora_inicio = int(values['hora_inicio'])
                if not (hora_inicio <= 24 and hora_inicio >= 0):
                    raise HorarioInvalidoException()
                
                hora_fim = int(values['hora_fim'])
                if not (hora_fim <= 24 and hora_fim >= 0):
                    raise HorarioInvalidoException()
                
                espaco = values['espaco']
                if len(espaco) < 5:
                    raise EspacoInvalidoException()
                
                window.close()
                return {
                    "cpf_solicitante": cpf_solicitante,
                    "data_reserva": data_reserva,
                    "hora_inicio": hora_inicio,
                    "hora_fim": hora_fim,
                    "espaco": espaco
                }
            except (CPFInvalidoException, DataInvalidaException, HorarioInvalidoException, EspacoInvalidoException) as e:
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

    def get_reserva_id(self):
        layout = [
            [sg.Text('ID da reserva a ser deletada:'), sg.InputText(key='id')],
            [sg.Button('Enviar')]
        ]
        window = sg.Window('Entrada de ID da Reserva', layout)

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

    def reserva_removida(self):
        sg.popup("Reserva removida com sucesso!")