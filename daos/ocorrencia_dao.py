from daos.dao import DAO
from models.ocorrencia import Ocorrencia

class OcorrenciaDAO(DAO):
    def _init_(self):
        super()._init_('ocorrencias.pkl')

    def adicionar_ocorrencia(self, ocorrencia):
        if isinstance(ocorrencia, Ocorrencia):
            if ocorrencia.id not in [o.id for o in self.get_all()]:
                self.add(ocorrencia.id, ocorrencia)

    def remover_ocorrencia(self, ocorrencia_id):
        ocorrencia = self.get(ocorrencia_id)
        if isinstance(ocorrencia, Ocorrencia):
            self.remove(ocorrencia_id)

    def buscar_ocorrencia_por_id(self, ocorrencia_id):
        ocorrencia = self.get(ocorrencia_id)
        if isinstance(ocorrencia, Ocorrencia):
            return ocorrencia
        return None

    def get_all_ocorrencias(self):
        return [o for o in self.get_all() if isinstance(o, Ocorrencia)]