class NenhumGastoProCPFException(Exception):
    def __init__(self):
        self.mensagem = f"Nao ha nenhum gasto neste cpf cadastrado no sistema"
        super().__init__(self.mensagem)