from daos.dao import DAO
from models.reserva import Reserva

class ReservaDAO(DAO):
    def __init__(self):
        super().__init__('reservas.pkl')

    def adicionar_reserva(self, reserva):
        if isinstance(reserva, Reserva):
            self.add(reserva.id, reserva)

    def remover_reserva(self, reserva_id):
        self.remove(reserva_id)

    def buscar_reserva_por_id(self, reserva_id):
        return self.get(reserva_id)

    def get_reservas(self):
        return self.get_all()
