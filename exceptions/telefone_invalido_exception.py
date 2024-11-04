class TelefoneInvalidoException(Exception):
    def __init__(self):
        self.mensagem = f"Telefone inválido! Deve conter pelo menos 11 dígitos numéricos."
        super().__init__(self.mensagem)