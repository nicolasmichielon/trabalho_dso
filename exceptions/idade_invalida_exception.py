class IdadeInvalidaException(Exception):
    def __init__(self):
        self.mensagem = f"Idade inválida! Deve ser um número entre 0 e 130."
        super().__init__(self.mensagem)