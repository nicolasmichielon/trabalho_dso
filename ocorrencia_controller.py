from ocorrencia_view import OcorrenciaView
from ocorrencia import Ocorrencia

class OcorrenciaController():
    def __init__(self, master_controller):
        self.__master_controller = master_controller
        self.__ocorrencia_view = OcorrenciaView()
        self.__ocorrencias = []

    def adicionar_ocorrencia(self):
        dados = self.__ocorrencia_view.get_ocorrencia()
        sindico_atual = self.__master_controller.pessoa_controller.get_sindico()
        morador = self.__master_controller.pessoa_controller.busca_morador_por_nome(dados[1])
        ocorrencia = Ocorrencia(dados[0], morador, sindico_atual, dados[2], dados[3])
        for oc in self.__ocorrencias:
            if oc.id == ocorrencia.id:
                return
        self.__ocorrencias.append(ocorrencia)


    def remover_ocorrencia(self, ocorrencia):
        if ocorrencia in self.__ocorrencias:
            self.__ocorrencias.remove(ocorrencia)

    def busca_ocorrencias(self):
        for ocorrencia in self.__ocorrencias:
            self.__ocorrencia_view.mostra_ocorrencias([
                "-------------------------------",
                f"Ocorrência id: {ocorrencia.id}",
                f"Morador: {ocorrencia.morador}",
                f"Sindico: {ocorrencia.sindico}",
                f"Descrição: {ocorrencia.descricao}",
                f"Resolvida? {"Sim" if ocorrencia.resolvida else "Não"}",
                "-------------------------------"])

    def busca_ocorrencias_por_nome_de_morador(self):
        nome = self.__ocorrencia_view.get_name()
        for ocorrencia in self.__ocorrencias:
            if ocorrencia.morador.nome == nome:
                self.__ocorrencia_view.mostra_ocorrencias([
                    f"Ocorrência id: {ocorrencia.id}",
                    f"Morador: {ocorrencia.morador.nome}",
                    f"Sindico: {ocorrencia.sindico.nome}",
                    f"Descrição: {ocorrencia.descricao}",
                    f"Resolvida? {"Sim" if ocorrencia.resolvida else "Não"}"])
