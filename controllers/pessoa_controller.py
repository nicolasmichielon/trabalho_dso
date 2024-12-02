from views.pessoa_view import PessoaView
from models.morador import Morador
from models.sindico import Sindico
from models.visitante import Visitante
from exceptions.pessoa_repetida_exception import PessoaRepetidaException
from exceptions.dados_invalidos_exception import DadosInvalidosException
from exceptions.pessoa_nao_cadastrada_exception import PessoaNaoCadastradaException
from exceptions.nenhum_morador_exception import NenhumMoradorException
from exceptions.nenhum_visitante_exception import NenhumVisitanteException
from exceptions.nenhum_sindico_exception import NenhumSindicoException
from daos.pessoa_dao import PessoaDAO

class PessoaController():
    def __init__(self, master_controller):
        self.__master_controller = master_controller
        self.__pessoas_view = PessoaView()
        self.__pessoa_dao = PessoaDAO()

    @property
    def moradores(self):
        return self.__pessoa_dao.get_moradores()
    
    @property
    def pessoa_view(self):
        return self.__pessoas_view

    def adicionar_sindico(self):
        try:
            dados = self.__pessoas_view.get_pessoa()
            sindico = Sindico(dados.get("nome"), dados.get("telefone"), dados.get("cpf"), dados.get("idade"))
            self.__pessoa_dao.adicionar_pessoa(sindico)
        except:
            self.__pessoas_view.mostra_linhas([
                f"\n{DadosInvalidosException()}\n"
            ])

    def adicionar_morador(self):
        try:
            dados = self.__pessoas_view.get_pessoa()
            morador = Morador(dados.get("nome"), dados.get("telefone"), dados.get("cpf"), dados.get("idade"))
            self.__pessoa_dao.adicionar_pessoa(morador)
            self.__pessoas_view.mostrar_pessoa([f"O morador {morador.nome} com o CPF {morador.cpf} foi adicionado com sucesso!"])
        except PessoaRepetidaException as e:
            self.__pessoas_view.pessoa_repetida(e)

    def adicionar_visitante(self):
        try:
            dados = self.__pessoas_view.get_pessoa()
            visitante = Visitante(dados.get("nome"), dados.get("telefone"), dados.get("cpf"), dados.get("idade"))
            self.__pessoa_dao.adicionar_pessoa(visitante)
            self.__pessoas_view.mostrar_pessoa([f"O visitante {visitante.nome} com o CPF {visitante.cpf} foi adicionado com sucesso!"])
        except PessoaRepetidaException as e:
            self.__pessoas_view.pessoa_repetida(e)

    def remover_morador(self):
        try:
            cpf_morador = self.__pessoas_view.get_cpf()
            self.__pessoa_dao.remover_pessoa(cpf_morador, Morador)
            self.__pessoas_view.mostra_linhas([f"Morador com o CPF {cpf_morador} foi removido com sucesso!"])
        except:
            self.__pessoas_view.mostra_linhas([
                f"\n{DadosInvalidosException()}\n"
            ])

    def remover_visitante(self):
        try:
            cpf_visitante = self.__pessoas_view.get_cpf()
            self.__pessoa_dao.remover_pessoa(cpf_visitante, Visitante)
            self.__pessoas_view.mostra_linhas([f"Visitante com o CPF {cpf_visitante} foi removido com sucesso!"])
        except:
            self.__pessoas_view.mostra_linhas([
                f"\n{DadosInvalidosException()}\n"
            ])

    def busca_morador_por_cpf(self, cpf) -> Morador:
        return self.__pessoa_dao.buscar_pessoa_por_cpf(cpf, Morador)

    def busca_visitante_por_cpf(self, cpf) -> Visitante:
        return self.__pessoa_dao.buscar_pessoa_por_cpf(cpf, Visitante)

    def get_sindico(self) -> Sindico:
        return self.__pessoa_dao.get_sindico()

    def get_tipo_de_pessoa(self, cpf: int) -> str:
        if self.busca_morador_por_cpf(cpf):
            return f"Morador"
        elif self.busca_visitante_por_cpf(cpf):
            return f"Visitante"
        elif cpf == self.get_sindico().cpf:
            return f"Sindico"
        else:
            self.__pessoas_view.mostra_linhas([
                f"\n{PessoaNaoCadastradaException()}\n"
            ])

    def trocar_sindico(self, novo_sindico: Sindico):
        self.__pessoa_dao.adicionar_pessoa(novo_sindico)
        self.__pessoas_view.mostra_linhas([
            f"Sindico trocado com sucesso."
        ])

    def display_sindico(self):
        sindico = self.__pessoa_dao.get_sindico()
        if sindico:
            self.__pessoas_view.mostrar_pessoa([
                "-------------------------------",
                f"Nome: {sindico.nome}",
                f"CPF: {sindico.cpf}",
                "-------------------------------",
            ])
        else:
            self.__pessoas_view.mostra_linhas([
                f"\n{NenhumSindicoException()}\n"
            ])

    def display_moradores(self):
        moradores = self.__pessoa_dao.get_moradores()
        if moradores:
            for morador in moradores:
                self.__pessoas_view.mostrar_pessoa([
                    "-------------------------------",
                    f"Nome: {morador.nome}",
                    f"CPF: {morador.cpf}",
                    "-------------------------------",
                ])
        else:
            self.__pessoas_view.mostra_linhas([
                f"\n{NenhumMoradorException()}\n"
            ])

    def display_visitantes(self):
        visitantes = self.__pessoa_dao.get_visitantes()
        if visitantes:
            for visitante in visitantes:
                self.__pessoas_view.mostrar_pessoa([
                    "-------------------------------",
                    f"Nome: {visitante.nome}",
                    f"CPF: {visitante.cpf}",
                    "-------------------------------",
                ])
        else:
            self.__pessoas_view.mostra_linhas([
                f"\n{NenhumVisitanteException()}\n"
            ])

    def get_cpf(self):
        return self.__pessoas_view.get_cpf()

