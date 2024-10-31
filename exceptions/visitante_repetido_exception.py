class VisitanteRepetidoException(Exception):
    def __init__(self, cpf):
        self.mensagem = "O visitante com esse CPF {} já existe"
        super().__init__(self.mensagem.format(cpf))