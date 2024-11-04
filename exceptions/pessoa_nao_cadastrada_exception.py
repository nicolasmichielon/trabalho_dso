class PessoaNaoCadastradaException(Exception):
    def __init__(self):
        self.mensagem = f"A pessoa com este cpf nao esta cadastrada no sistema"
        super().__init__(self.mensagem)