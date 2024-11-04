class DataInvalidaException(Exception):
    def __init__(self):
        self.mensagem = f"Data inválida! Por favor escolha uma data valida no formato: 'dd/mm/yyyy'"
        super().__init__(self.mensagem)