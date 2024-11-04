class DescricaoInvalidaException(Exception):
    def __init__(self):
        self.mensagem = f"Descricao inválida! Elabore um pouco mais"
        super().__init__(self.mensagem)