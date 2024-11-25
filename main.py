from controllers.master_controller import MasterController
from views.master_view import MasterView

master_controller = MasterController()
master_view = MasterView()

def run_gui():
    switch = True
    while switch:
        options = master_controller.iniciarSistema()  # Get options from the controller
        master_view.mostra_opcoes(options)
        selected_value = master_view.solicitar_resposta()
        if selected_value is not None:
            switch = master_controller.process_selection(selected_value)  # Process the selected option
        else:
            switch = False

if __name__ == "__main__":
    run_gui()
