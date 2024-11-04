class NenhumMoradorException(Exception):
    def __init__(self):
        self.mensagem = f"Nao ha nenhum morador cadastrado no sistema"
        super().__init__(self.mensagem)