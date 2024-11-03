from controllers.master_controller import MasterController

master_controller = MasterController()
switch = master_controller.iniciarSistema()
while switch:
    switch = master_controller.iniciarSistema()
