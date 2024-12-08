from daos.dao import DAO
from models.gasto import Gasto

class GastoDAO(DAO):
    def __init__(self):
        super().__init__('gastos.pkl')

    def adicionar_gasto(self, gasto):
        if isinstance(gasto, Gasto):
            if gasto.id not in [g.id for g in self.get_all()]:
                self.add(gasto.id, gasto)

    def remover_gasto(self, id):
        gasto = self.get(id)
        if isinstance(gasto, Gasto):
            self.remove(id)

    def buscar_gasto_por_id(self, id):
        gasto = self.get(id)
        if isinstance(gasto, Gasto):
            return gasto
        return None

    def get_gastos(self):
        return [g for g in self.get_all() if isinstance(g, Gasto)]

    def get_next_id(self):
        gastos = self.get_all()
        if len(gastos) == 0:
            return 1
        else:
            return max(gasto.id for gasto in gastos) + 1
