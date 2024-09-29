from ocorrencia import Ocorrencia

class RegistroOcorrencias:
    def __init__(self, ocorrencias):
        self.__ocorrencias = ocorrencias

    def adicionar_ocorrencia(self, ocorrencia: Ocorrencia):
        self.__ocorrencias.append(ocorrencia)

    def listar_ocorrencias(self):
        return self.__ocorrencias

    def buscar_ocorrencia_por_id(self, id: int):
        for ocorrencia in self.__ocorrencias:
            if ocorrencia.id == id:
                return ocorrencia
        return None

    def resolver_ocorrencia(self, id: int):
        ocorrencia = self.buscar_ocorrencia_por_id(id)
        if ocorrencia:
            ocorrencia.resolvida = True
            return True
        return False