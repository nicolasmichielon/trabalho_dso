from exceptions.cpf_invalido_exception import CPFInvalidoException
from exceptions.data_invalida_exception import DataInvalidaException
from exceptions.espaco_invalido_exception import EspacoInvalidoException
from exceptions.horario_invalido_exception import HorarioInvalidoException

class ReservaView:
    def __init__(self) -> None:
        pass

    def mostraReserva(self, linhas: list):
        for linha in linhas:
            print(linha)

    def get_reserva(self) -> dict:
        while True:
            try:
                cpf_solicitante = int(input("CPF do solicitante: "))
                if len(cpf_solicitante) != 11 or not cpf_solicitante.isdigit():
                    raise CPFInvalidoException()
                cpf_solicitante = int(cpf_solicitante)
                break
            except CPFInvalidoException as e:
                print(e)

        while True:
            try:
                data_reserva = input("Data da reserva: ")
                if len(data_reserva) < 10:
                    raise DataInvalidaException()
                break
            except DataInvalidaException as e:
                print(e)

        while True:
            try:
                hora_inicio = int(input("Hora de início: "))
                if not hora_inicio <= 24 and not hora_inicio >= 0:
                    raise HorarioInvalidoException()
                break
            except HorarioInvalidoException as e:
                print(e)

        while True:
            try:
                hora_fim = int(input("Hora de fim: "))
                if not hora_fim <= 24 and not hora_fim >= 0:
                    raise HorarioInvalidoException()
                break
            except HorarioInvalidoException as e:
                print(e)

        while True:
            try:
                espaco = input("Espaço: ")
                if len(espaco) < 6:
                    raise EspacoInvalidoException()
                break
            except EspacoInvalidoException as e:
                print(e)

        return {
            "cpf_solicitante": cpf_solicitante,
            "data_reserva": data_reserva,
            "hora_inicio": hora_inicio,
            "hora_fim": hora_fim,
            "espaco": espaco
        }
    
    def get_cpf(self):
        while True:
            try:
                cpf = int(input("CPF: "))
                if len(cpf) != 11 or not cpf.isdigit():
                    raise CPFInvalidoException()
                cpf = int(cpf)
                break
            except CPFInvalidoException as e:
                print(e)
        return cpf