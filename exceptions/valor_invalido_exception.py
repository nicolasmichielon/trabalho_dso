class ValorInvalidoException(Exception):
    def __init__(self):
        self.mensagem = f"Valor inválido!"
        super().__init__(self.mensagem)