class EntradaInvalidaException(Exception):
    def __init__(self):
        self.mensagem = f"Entrada inválida!"
        super().__init__(self.mensagem)