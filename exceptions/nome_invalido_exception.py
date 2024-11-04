class NomeInvalidoException(Exception):
    def __init__(self):
        self.mensagem = f"Nome inválido! Deve ter pelo menos 2 caracteres."
        super().__init__(self.mensagem)