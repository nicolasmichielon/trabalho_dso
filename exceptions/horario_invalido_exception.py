class HorarioInvalidoException(Exception):
    def __init__(self):
        self.mensagem = f"Horario inválido! Por favor escolha um horario entre 00 e 24 horas."
        super().__init__(self.mensagem)