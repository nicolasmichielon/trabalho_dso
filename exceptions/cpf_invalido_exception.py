class CPFInvalidoException(Exception):
    def __init__(self):
        self.mensagem = f"CPF inválido! Deve conter 11 dígitos numéricos."
        super().__init__(self.mensagem)