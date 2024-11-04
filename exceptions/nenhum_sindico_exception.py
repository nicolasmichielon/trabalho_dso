class NenhumSindicoException(Exception):
    def __init__(self):
        self.mensagem = f"Nao ha nenhum sindico cadastrado no sistema"
        super().__init__(self.mensagem)