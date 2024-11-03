from models.reserva import ReservaDeEspaco
from views.reserva_view import ReservaView

class ReservaController:
    def __init__(self, master_controller) -> None:
        self.__master_controller = master_controller
        self.__reserva_view = ReservaView()
        self.__reservas = []

    @property
    def reservas(self):
        return self.__reservas
    
    def lista_reservas(self):
        for reserva in self.__reservas:
            self.__reserva_view.mostraReserva([
                f"ID Reserva: {reserva.id}\n"
                f"Solicitante: {reserva.solicitante}\n"
                f"Data: {reserva.data_reserva}\n"
                f"Hora ínicio: {reserva.hora_inicio}\n"
                f"Hora fim: {reserva.hora_fim}\n"
                f"Custo: {reserva.custo}\n"
                f"Espaço: {reserva.espaco}"
            ])

    def lista_reservas_por_cpf(self, cpf):
        for reserva in self.__reservas:
            if reserva.solicitante.cpf == cpf:
                self.__reserva_view.mostraReserva([
                    f"ID Reserva: {reserva.id}\n"
                    f"Solicitante: {reserva.solicitante.nome}\n"
                    f"Data: {reserva.data_reserva}\n"
                    f"Hora ínicio: {reserva.hora_inicio}\n"
                    f"Hora fim: {reserva.hora_fim}\n"
                    f"Custo: {reserva.custo}\n"
                    f"Espaço: {reserva.espaco}"
                ])