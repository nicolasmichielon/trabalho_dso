from views.ocorrencia_view import OcorrenciaView
from models.ocorrencia import Ocorrencia
from exceptions.dados_invalidos_exception import DadosInvalidosException
from exceptions.morador_nao_encontrado_exception import MoradorNaoEncontradoException
from exceptions.nenhum_sindico_exception import NenhumSindicoException
from daos.ocorrencia_dao import OcorrenciaDAO

class OcorrenciaController():
    def _init_(self, master_controller):
        self.__master_controller = master_controller
        self.__ocorrencia_view = OcorrenciaView()
        self.__ocorrencia_dao = OcorrenciaDAO()

    def adicionar_ocorrencia(self):
        dados = self.__ocorrencia_view.get_ocorrencia(self.busca_ultimo_id())
        sindico_atual = self.__master_controller.pessoa_controller.get_sindico()
        morador = self.__master_controller.pessoa_controller.busca_morador_por_cpf(dados.get("cpf"))
        try:
            if morador == None:
                raise MoradorNaoEncontradoException()
            if sindico_atual == None:
                raise NenhumSindicoException()
            ocorrencia = Ocorrencia(dados.get("id"), morador, sindico_atual, dados.get("descricao"), dados.get("tipo"))
            if self.__ocorrencia_dao.buscar_ocorrencia_por_id(ocorrencia.id) is None:
                self.__ocorrencia_dao.adicionar_ocorrencia(ocorrencia)
                self.__ocorrencia_view.mostra_linhas([
                    "Ocorrencia Criada com sucesso"
                ])
        except MoradorNaoEncontradoException as e:
                self.__ocorrencia_view.mostra_linhas([
                    f"\n{e}\n"
                ])
        except NenhumSindicoException as e:
                self.__ocorrencia_view.mostra_linhas([
                    f"\n{e}\n"
                ])
        except Exception as e:
                self.__ocorrencia_view.mostra_linhas([
                    f"\n{e}\n"
                ])

    def remover_ocorrencia(self, ocorrencia):
        if self.__ocorrencia_dao.buscar_ocorrencia_por_id(ocorrencia.id) is not None:
            self.__ocorrencia_dao.remover_ocorrencia(ocorrencia.id)
            self.__ocorrencia_view.mostra_ocorrencias([
                "Ocorrência removida com sucesso!"
                ])
        else:
            self.__ocorrencia_view.mostra_ocorrencias(["Nenhuma ocorrência encontrada!"])

    def busca_ocorrencias(self):
        try:
            ocorrencias = self.__ocorrencia_dao.get_all_ocorrencias()
            if len(ocorrencias) > 0:
                for ocorrencia in ocorrencias:
                    self.__ocorrencia_view.mostra_ocorrencias([
                        "-------------------------------",
                        f"Ocorrência id: {ocorrencia.id}",
                        f"Morador: {ocorrencia.morador.nome}",
                        f"Sindico: {ocorrencia.sindico.nome}",
                        f"Descrição: {ocorrencia.descricao}",
                        f"Resolvida? {'Sim' if ocorrencia.resolvida else 'Não'}",
                        "-------------------------------"])
            else:
                raise ValueError()
        except ValueError:
            self.__ocorrencia_view.mostra_ocorrencias(["Nenhuma ocorrência encontrada!"])

    def busca_ocorrencias_por_cpf_de_morador(self):
        try:
            cpf = self.__master_controller.pessoa_controller.get_cpf()
            existe_morador = self.__master_controller.pessoa_controller.busca_morador_por_cpf(cpf)
            if existe_morador == None:
                raise MoradorNaoEncontradoException()
            ocorrencias = self.__ocorrencia_dao.get_all_ocorrencias()
            if len(ocorrencias) > 0:
                for ocorrencia in ocorrencias:
                    if ocorrencia.morador.cpf == cpf:
                        self.__ocorrencia_view.mostra_ocorrencias([
                            "-------------------------------",
                            f"Ocorrência id: {ocorrencia.id}",
                            f"Morador: {ocorrencia.morador.nome}",
                            f"Sindico: {ocorrencia.sindico.nome}",
                            f"Descrição: {ocorrencia.descricao}",
                            f"Resolvida? {'Sim' if ocorrencia.resolvida else 'Não'}",
                            "-------------------------------"])
                        return
                self.__ocorrencia_view.mostra_ocorrencias(["Nenhuma ocorrência encontrada feita por este morador!"])
            else:
                self.__ocorrencia_view.mostra_ocorrencias(["Nenhuma ocorrência encontrada!"])
        except MoradorNaoEncontradoException as e:
            self.__ocorrencia_view.mostra_linhas([
                f"\n{e}\n"
            ])

    def busca_ultimo_id(self) -> int:
        ocorrencias = self.__ocorrencia_dao.get_all_ocorrencias()
        if len(ocorrencias) > 0:
            return ocorrencias[-1].id
        else: 
            return 0