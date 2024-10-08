from ocorrencia_view import OcorrenciaView
from ocorrencia import Ocorrencia

class OcorrenciaController():
    def __init__(self):
        self.__ocorrencia_view = OcorrenciaView()
        self.__ocorrencias = []

    def adicionar_ocorrencia(self, ocorrencia: Ocorrencia):
        if ocorrencia not in self.__ocorrencias:
            self.__ocorrencias.append(ocorrencia)
            self.__ocorrencia_view.mostra_ocorrencias([ocorrencia])

    def remover_ocorrencia(self, ocorrencia):
        if ocorrencia in self.__ocorrencias:
            self.__ocorrencias.remove(ocorrencia)
            self.__ocorrencia_view.mostra_ocorrencias([ocorrencia])

    def busca_ocorrencias(self):
        for ocorrencia in self.__ocorrencias:
            self.__ocorrencia_view.mostra_ocorrencias([
                "-------------------------------",
                f"Ocorrência ID: {ocorrencia.id}",
                f"Morador: {ocorrencia.morador}",
                f"Sindico: {ocorrencia.sindico}",
                f"Descrição: {ocorrencia.descricao}",
                f"Resolvida? {"Sim" if ocorrencia.resolvida else "Não"}",
                "-------------------------------"])

    def busca_ocorrencias_por_id_de_morador(self, id: int):
        for ocorrencia in self.__ocorrencias:
            if ocorrencia.morador.id == id:
                self.__ocorrencia_view.mostra_ocorrencias([
                    f"Ocorrência ID: {ocorrencia.id}",
                    f"Morador: {ocorrencia.morador}",
                    f"Sindico: {ocorrencia.sindico}",
                    f"Descrição: {ocorrencia.descricao}",
                    f"Resolvida? {"Sim" if ocorrencia.resolvida else "Não"}"])
