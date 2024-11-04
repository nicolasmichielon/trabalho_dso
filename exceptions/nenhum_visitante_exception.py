class NenhumVisitanteException(Exception):
    def __init__(self):
        self.mensagem = f"Nao ha nenhum visitante cadastrado no sistema"
        super().__init__(self.mensagem)