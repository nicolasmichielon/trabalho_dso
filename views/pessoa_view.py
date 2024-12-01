import PySimpleGUI as sg
from exceptions.cpf_invalido_exception import CPFInvalidoException
from exceptions.idade_invalida_exception import IdadeInvalidaException
from exceptions.telefone_invalido_exception import TelefoneInvalidoException
from exceptions.nome_invalido_exception import NomeInvalidoException

class PessoaView():
    def __init__(self) -> None:
        pass

    def mostrar_pessoa(self, linhas: list):
        layout = [[sg.Text(linha)] for linha in linhas] + [[sg.Button('Ok')]]
        window = sg.Window('Mostrar Pessoa', layout)
        event = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            window.close()
            return None

    def get_pessoa(self) -> dict:
        layout = [
            [sg.Text('Nome:'), sg.InputText(key='nome')],
            [sg.Text('Telefone:'), sg.InputText(key='telefone')],
            [sg.Text('CPF:'), sg.InputText(key='cpf')],
            [sg.Text('Idade:'), sg.InputText(key='idade')],
            [sg.Button('Enviar')]
        ]
        window = sg.Window('Cadastro de Pessoa', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Sair':
                window.close()
                return None

            try:
                nome = values['nome']
                if len(nome) < 2:
                    raise NomeInvalidoException()
                
                telefone = values['telefone']
                if len(telefone) < 11 or not telefone.isdigit():
                    raise TelefoneInvalidoException()
                
                cpf = values['cpf']
                if len(cpf) != 11 or not cpf.isdigit():
                    raise CPFInvalidoException()
                cpf = int(cpf)
                
                idade = int(values['idade'])
                if idade > 130 or idade < 0:
                    raise IdadeInvalidaException()
                
                window.close()
                return {"nome": nome, "telefone": telefone, "cpf": cpf, "idade": idade}
            except (NomeInvalidoException, TelefoneInvalidoException, CPFInvalidoException, IdadeInvalidaException) as e:
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

    def mostra_linhas(self, linhas: list):
        layout = [[sg.Text(linha)] for linha in linhas] + [[sg.Button('Ok')]]
        window = sg.Window('Mostrar Linhas', layout)
        event = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            window.close()
            return None

    def pessoa_repetida(self, msg):
        sg.popup(msg)