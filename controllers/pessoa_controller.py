from morador import Morador
from views.pessoa_view import PessoaView
from sindico import Sindico
from exceptions.morador_repetido_exception import MoradorRepetidoException

class PessoaController():
    def __init__(self, master_controller):
        self.__master_controller = master_controller
        self.__pessoas_view = PessoaView()
        self.__moradores = []
        self.__sindico = None

    def adicionar_sindico(self):
        try:
            dados = self.__pessoas_view.get_pessoa()
            sindico = Sindico(dados.get("nome"), dados.get("telefone"), dados.get("cpf"), dados.get("idade"))
        except:
            raise ValueError("Dados inválidos foram inseridos")
        self.__sindico = sindico


    def adicionar_morador(self):
        try:
            dados = self.__pessoas_view.get_pessoa()
            morador = Morador(dados.get("nome"), dados.get("telefone"), dados.get("cpf"), dados.get("idade"))
            cpfs = [morador.cpf for morador in self.__moradores]
            if morador.cpf not in cpfs:
                self.__moradores.append(morador)
                self.__pessoas_view.mostrar_moradores_ou_sindico([morador])
            else:
                raise MoradorRepetidoException(morador.cpf)
        except MoradorRepetidoException as e:
            self.__pessoas_view.morador_repetido(e)

    def remover_morador(self):
        try:
            morador = self.__pessoas_view.get_pessoa()
        except:
            raise ValueError("Dados inválidos foram inseridos ou o morador não existe")
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
    
    def get_morador_por_cpf(self) -> str:
        cpf = self.__pessoas_view.get_cpf()
        for morador in self.__moradores:
            if morador.cpf == cpf:
                return morador
            
    def get_cpf(self) -> str:
        return self.__pessoas_view.get_cpf()

    def trocar_sindico(self, novo_sindico: Sindico):
        self.__sindico = novo_sindico

    def display_sindico(self):
        self.__pessoas_view.mostrar_moradores_ou_sindico([self.__sindico])

    def display_moradores(self):
        for morador in self.__moradores:
            self.__pessoas_view.mostrar_moradores_ou_sindico([
                "-------------------------------",
                f"Nome: {morador.nome}",
                f"CPF: {morador.cpf}",
            ])