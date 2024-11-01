class TipoVagaIncompativelException(Exception):
    def __init__(self, cpf):
        self.mensagem = f"O tipo de vaga não é compatível com o tipo da pessoa com CPF {cpf}."
        super().__init__(self.mensagem)
