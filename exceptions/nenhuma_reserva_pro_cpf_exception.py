class NenhumaReservaProCPFException(Exception):
    def __init__(self):
        self.mensagem = f"Nao ha nenhuma reserva neste cpf cadastrada no sistema"
        super().__init__(self.mensagem)