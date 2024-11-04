from views.ocorrencia_view import OcorrenciaView
from models.ocorrencia import Ocorrencia
from exceptions.dados_invalidos_exception import DadosInvalidosException

class OcorrenciaController():
    def __init__(self, master_controller):
        self.__master_controller = master_controller
        self.__ocorrencia_view = OcorrenciaView()
        self.__ocorrencias = []

    def adicionar_ocorrencia(self):
        dados = self.__ocorrencia_view.get_ocorrencia(self.busca_ultimo_id())
        sindico_atual = self.__master_controller.pessoa_controller.get_sindico()
        morador = self.__master_controller.pessoa_controller.busca_morador_por_cpf(dados.get("cpf"))        
        try:
            ocorrencia = Ocorrencia(dados.get("id"), morador, sindico_atual, dados.get("descricao"), dados.get("tipo"))
        except:
            raise DadosInvalidosException()
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

    def busca_ocorrencias_por_cpf_de_morador(self):
        cpf = self.__ocorrencia_view.get_cpf()
        if not isinstance(cpf, int):
            raise ValueError("CPF deve ser inteiro")
        if len(self.__ocorrencias) == 0:
            self.__ocorrencia_view.mostra_ocorrencias(["Nenhuma ocorrência encontrada!"])
        for ocorrencia in self.__ocorrencias:
            if ocorrencia.morador.cpf == cpf:
                self.__ocorrencia_view.mostra_ocorrencias([
                    "-------------------------------",
                    f"Ocorrência id: {ocorrencia.id}",
                    f"Morador: {ocorrencia.morador.nome}",
                    f"Sindico: {ocorrencia.sindico.nome}",
                    f"Descrição: {ocorrencia.descricao}",
                    f"Resolvida? {"Sim" if ocorrencia.resolvida else "Não"}",
                    "-------------------------------"])
        
                
    def busca_ultimo_id(self) -> int:
        if len(self.__ocorrencias) > 0:
            return self.__ocorrencias[-1].id
        else: 
            return 0
