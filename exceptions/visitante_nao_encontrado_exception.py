class VisitanteNaoEncontradoException(Exception):
    def __init__(self):
        self.mensagem = f"Visitante nao encontrado no sistema"
        super().__init__(self.mensagem)