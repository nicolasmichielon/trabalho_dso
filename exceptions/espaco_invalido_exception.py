class EspacoInvalidoException(Exception):
    def __init__(self):
        self.mensagem = f"Espaco inválido! Por favor escolha um espaco valido."
        super().__init__(self.mensagem)