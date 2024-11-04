class VagaInvalidaException(Exception):
    def __init__(self):
        self.mensagem = f"A Vaga escolhida é inválida!"
        super().__init__(self.mensagem)