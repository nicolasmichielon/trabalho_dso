class DadosInvalidosException(Exception):
    def __init__(self):
        self.mensagem = f"Dados inválidos foram inseridos"
        super().__init__(self.mensagem)