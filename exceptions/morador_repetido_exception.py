class MoradorRepetidoException(Exception):
    def __init__(self, cpf):
        self.mensagem = "O morador com CPF {} já existe"
        super().__init__(self.mensagem.format(cpf))