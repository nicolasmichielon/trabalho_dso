class MoradorNaoEncontradoException(Exception):
    def __init__(self):
        self.mensagem = f"Morador nao encontrado no sistema"
        super().__init__(self.mensagem)