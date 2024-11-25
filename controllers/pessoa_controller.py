from views.pessoa_view import PessoaView
from models.morador import Morador
from models.sindico import Sindico
from models.visitante import Visitante
from exceptions.pessoa_repetida_exception import PessoaRepetidaException
from exceptions.dados_invalidos_exception import DadosInvalidosException
from exceptions.morador_nao_encontrado_exception import MoradorNaoEncontradoException
from exceptions.visitante_nao_encontrado_exception import VisitanteNaoEncontradoException
from exceptions.pessoa_nao_cadastrada_exception import PessoaNaoCadastradaException
from exceptions.nenhum_morador_exception import NenhumMoradorException
from exceptions.nenhum_visitante_exception import NenhumVisitanteException
from exceptions.nenhum_sindico_exception import NenhumSindicoException

class PessoaController():
    def __init__(self, master_controller):
        self.__master_controller = master_controller
        self.__pessoas_view = PessoaView()
        self.__moradores = []
        self.__visitantes = []
        self.__sindico = None

    @property
    def moradores(self):
        return self.__moradores

    def adicionar_sindico(self):
        try:
            dados = self.__pessoas_view.get_pessoa()
            sindico = Sindico(dados.get("nome"), dados.get("telefone"), dados.get("cpf"), dados.get("idade"))
        except:
            self.__pessoas_view.mostra_linhas([
                f"\n{DadosInvalidosException()}\n"
            ])

        self.__sindico = sindico


    def adicionar_morador(self):
        try:
            dados = self.__pessoas_view.get_pessoa()
            morador = Morador(dados.get("nome"), dados.get("telefone"), dados.get("cpf"), dados.get("idade"))
            cpfs = []
            for m in self.__moradores:
                cpfs.append(m.cpf)
            for v in self.__visitantes:
                cpfs.append(v.cpf)
            if morador.cpf not in cpfs:
                self.__moradores.append(morador)
                self.__pessoas_view.mostrar_pessoa([morador])
            else:
                raise PessoaRepetidaException(morador.cpf)
        except PessoaRepetidaException as e:
            self.__pessoas_view.pessoa_repetida(e)


    def adicionar_visitante(self):
        try:
            dados = self.__pessoas_view.get_pessoa()
            visitante = Visitante(dados.get("nome"), dados.get("telefone"), dados.get("cpf"), dados.get("idade"))
            cpfs = []
            for morador in self.__moradores:
                cpfs.append(morador.cpf)
            for visitante in self.__visitantes:
                cpfs.append(visitante.cpf)
            if visitante.cpf not in cpfs:
                self.__visitantes.append(visitante)
                self.__pessoas_view.mostrar_pessoa([visitante])
            else:
                raise PessoaRepetidaException(visitante.cpf)
        except PessoaRepetidaException as e:
            self.__pessoas_view.pessoa_repetida(e)

    def remover_morador(self):
        try:
            cpf_morador = self.__pessoas_view.get_cpf()
            morador = self.busca_morador_por_cpf(cpf_morador)
        except:
            self.__pessoas_view.mostra_linhas([
                f"\n{DadosInvalidosException()}\n"
            ])
        if morador == None:
            self.__pessoas_view.mostra_linhas([
                f"\n{MoradorNaoEncontradoException()}\n"
            ])
        elif morador in self.__moradores:
            self.__moradores.remove(morador)
            self.__pessoas_view.mostrar_pessoa([morador])

    def remover_visitante(self):
        try:
            cpf_visitante = self.__pessoas_view.get_cpf()
            visitante = self.busca_visitante_por_cpf(cpf_visitante)
        except:
            self.__pessoas_view.mostra_linhas([
                f"\n{DadosInvalidosException()}\n"
            ])
        if visitante == None:
            self.__pessoas_view.mostra_linhas([
                f"\n{VisitanteNaoEncontradoException()}\n"
            ])
        if visitante in self.__visitantes:
            self.__visitantes.remove(visitante)
            self.__pessoas_view.mostrar_pessoa([visitante])

    def busca_morador_por_cpf(self, cpf) -> Morador:
        self.__pessoas_view.mostra_linhas([
            f"Procurando pelo CPF: {cpf}..."
        ])
        for morador in self.__moradores:
            if morador.cpf == cpf:
                self.__pessoas_view.mostrar_pessoa([
                    "-------------------------------",
                    f"Nome: {morador.nome}",
                    "-------------------------------"])
                return morador
        return None

    def busca_visitante_por_cpf(self, cpf) -> Visitante:
        self.__pessoas_view.mostra_linhas([
            f"Procurando pelo CPF: {cpf}..."
        ])
        for visitante in self.__visitantes:
            if visitante.cpf == cpf:
                self.__pessoas_view.mostrar_pessoa([
                    "-------------------------------",
                    f"Nome: {visitante.nome}",
                    "-------------------------------"])
                return visitante
        return None
            
    def get_sindico(self) -> Sindico:
        return self.__sindico

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

            
    def get_cpf(self) -> str:
        return self.__pessoas_view.get_cpf()

    def trocar_sindico(self, novo_sindico: Sindico):
        self.__sindico = novo_sindico
        self.__pessoas_view.mostra_linhas([
            f"Sindico trocado com sucesso."
        ])


    def display_sindico(self):
        if self.__sindico != None:
            self.__pessoas_view.mostrar_pessoa([
                    "-------------------------------",
                    f"Nome: {self.__sindico.nome}",
                    f"CPF: {self.__sindico.cpf}",
                    "-------------------------------",
                ])
        else:
            self.__pessoas_view.mostra_linhas([
                f"\n{NenhumSindicoException()}\n"
            ])


    def display_moradores(self):
        if len(self.__moradores) > 0:
            for morador in self.__moradores:
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
        if len(self.__visitantes) > 0:
            for visitante in self.__visitantes:
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

