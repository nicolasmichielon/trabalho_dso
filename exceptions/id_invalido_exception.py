class IDInvalidoException(Exception):
    def __init__(self):
        self.mensagem = f"ID inválido! Deve estar contido na lista."
        super().__init__(self.mensagem)