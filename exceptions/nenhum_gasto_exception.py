class NenhumGastoException(Exception):
    def __init__(self):
        self.mensagem = f"Nao ha nenhum gasto cadastrado no sistema"
        super().__init__(self.mensagem)