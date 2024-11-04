class NenhumaReservaException(Exception):
    def __init__(self):
        self.mensagem = f"Nao ha nenhuma reserva cadastrada no sistema"
        super().__init__(self.mensagem)