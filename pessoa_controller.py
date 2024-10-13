from morador import Morador
from pessoa_view import PessoaView
from sindico import Sindico

class PessoaController():
    def __init__(self):
        self.__pessoas_view = PessoaView()
        self.__moradores = []
        self.__sindico = None

    def adicionar_sindico(self, sindico: Sindico):
        self.__sindico = sindico

    def adicionar_morador(self, morador: Morador):
        if morador not in self.__moradores:
            self.__moradores.append(morador)
            self.__pessoas_view.mostra_moradores([morador])

    def remover_morador(self, morador: Morador):
        if morador in self.__moradores:
            self.__moradores.remove(morador)
            self.__pessoas_view.mostra_moradores([morador])

    def busca_morador(self):
        for morador in self.__moradores:
            self.__pessoas_view.mostra_moradores([
                "-------------------------------",
                f"Ocorrência ID: {morador.id}",
                "-------------------------------"])

    def trocar_sindico(self, novo_sindico: Sindico):
        self.__sindico = novo_sindico
