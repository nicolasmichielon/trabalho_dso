class ReservaView:
    def __init__(self) -> None:
        pass

    def mostraReserva(self, linhas: list):
        for linha in linhas:
            print(linha)

    def get_reserva(self) -> dict:
        cpf_solicitante = int(input("CPF do solicitante: "))
        data_reserva = input("Data da reserva: ")
        hora_inicio = int(input("Hora de início: "))
        hora_fim = int(input("Hora de fim: "))
        espaco = input("Espaço: ")
        return {
            "cpf_solicitante": cpf_solicitante,
            "data_reserva": data_reserva,
            "hora_inicio": hora_inicio,
            "hora_fim": hora_fim,
            "espaco": espaco
        }
    
    def get_cpf(self):
        return int(input("CPF: "))