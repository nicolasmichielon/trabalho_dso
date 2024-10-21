from morador import Morador
from pessoa_view import PessoaView
from sindico import Sindico

class PessoaController():
    def __init__(self, master_controller):
        self.__master_controller = master_controller
        self.__pessoas_view = PessoaView()
        self.__moradores = []
        self.__sindico = None

    def adicionar_sindico(self):
        dados = self.__pessoas_view.get_pessoa()
        sindico = Sindico(dados[0], dados[1], dados[2], dados[3])
        self.__sindico = sindico


    def adicionar_morador(self):
        dados = self.__pessoas_view.get_pessoa()
        morador = Morador(dados.get("nome"), dados.get("telefone"), dados.get("cpf"), dados.get("idade"))
        if morador not in self.__moradores:
            self.__moradores.append(morador)
            self.__pessoas_view.mostrar_moradores_ou_sindico([morador])

    def remover_morador(self, morador: Morador):
        if morador in self.__moradores:
            self.__moradores.remove(morador)
            self.__pessoas_view.mostrar_moradores_ou_sindico([morador])

    def busca_morador_por_cpf(self, cpf) -> Morador:
        for morador in self.__moradores:
            if morador.cpf == cpf:
                self.__pessoas_view.mostrar_moradores_ou_sindico([
                    "-------------------------------",
                    f"Nome: {morador.nome}",
                    "-------------------------------"])
                return morador
            
    def get_sindico(self) -> Sindico:
        return self.__sindico

    def trocar_sindico(self, novo_sindico: Sindico):
        self.__sindico = novo_sindico

    def display_sindico(self):
        self.__pessoas_view.mostrar_moradores_ou_sindico([self.__sindico])

    def display_moradores(self):
        self.__pessoas_view.mostrar_moradores_ou_sindico(self.__moradores)
