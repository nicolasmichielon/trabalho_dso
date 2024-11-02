class PessoaRepetidaException(Exception):
    def __init__(self, cpf):
        self.mensagem = "Uma pessoa com esse CPF {} já está cadastrada"
        super().__init__(self.mensagem.format(cpf))