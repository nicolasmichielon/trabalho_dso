import PySimpleGUI as sg

class MasterView:
    def __init__(self) -> None:
        self.window = None
        self.selected_value = None

    def mostra_opcoes(self, linhas):
        layout = [[sg.Text(line)] for line in linhas]
        layout.append([sg.Listbox(values=linhas[1:], size=(30, 6), key='-LIST-', enable_events=True)])
        layout.append([sg.Button('Submit'), sg.Button('Cancel')])
        self.window = sg.Window('Master View', layout)

    def solicitar_resposta(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                self.window.close()
                return None
            if event == 'Submit':
                if not values['-LIST-']:
                    sg.popup_error("Nenhuma opção selecionada")
                else:
                    self.selected_value = values['-LIST-'][0]
                    self.window.close()
                    return self.selected_value

    def mostra_erro(self, erro: Exception):
        sg.popup_error(f"Erro: {str(erro)}")

    def stop(self):
        if self.window:
            self.window.close()

    def run(self):
        if self.window:
            self.window.read()

    def get_selected_value(self):
        return self.selected_value