from views.pessoa_view import PessoaView
from models.morador import Morador
from models.sindico import Sindico
from models.visitante import Visitante
from exceptions.morador_repetido_exception import MoradorRepetidoException
from exceptions.visitante_repetido_exception import VisitanteRepetidoException

class PessoaController():
    def __init__(self, master_controller):
        self.__master_controller = master_controller
        self.__pessoas_view = PessoaView()
        self.__moradores = []
        self.__visitantes = []
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
            self.__pessoas_view.pessoa_repetida(e)


    def adicionar_visitante(self):
        try:
            dados = self.__pessoas_view.get_pessoa()
            visitante = Visitante(dados.get("nome"), dados.get("telefone"), dados.get("cpf"), dados.get("idade"))
            cpfs = [visitante.cpf for visitante in self.__visitantes]
            if visitante.cpf not in cpfs:
                self.__visitantes.append(visitante)
                self.__pessoas_view.mostrar_pessoa([visitante])
            else:
                raise VisitanteRepetidoException(visitante.cpf)
        except VisitanteRepetidoException as e:
            self.__pessoas_view.pessoa_repetida(e)

    def remover_morador(self):
        try:
            morador = self.__pessoas_view.get_pessoa()
        except:
            raise ValueError("Dados inválidos foram inseridos ou o morador não existe")
        if morador in self.__moradores:
            self.__moradores.remove(morador)
            self.__pessoas_view.mostrar_pessoa([morador])

    def remover_visitante(self):
        try:
            visitante = self.__pessoas_view.get_pessoa()
        except:
            raise ValueError("Dados inválidos foram inseridos ou o visitante não existe")
        if visitante in self.__visitantes:
            self.__visitantes.remove(visitante)
            self.__pessoas_view.mostrar_pessoa([visitante])

    def busca_morador_por_cpf(self, cpf) -> Morador:
        for morador in self.__moradores:
            if morador.cpf == cpf:
                self.__pessoas_view.mostrar_pessoa([
                    "-------------------------------",
                    f"Nome: {morador.nome}",
                    "-------------------------------"])
                return morador

    def busca_visitante_por_cpf(self, cpf) -> Visitante:
        for visitante in self.__visitantes:
            if visitante.cpf == cpf:
                self.__pessoas_view.mostrar_pessoa([
                    "-------------------------------",
                    f"Nome: {visitante.nome}",
                    "-------------------------------"])
                return visitante
            
    def get_sindico(self) -> Sindico:
        return self.__sindico
    
    def get_morador_por_cpf(self) -> str:
        cpf = self.__pessoas_view.get_cpf()
        for morador in self.__moradores:
            if morador.cpf == cpf:
                return morador
    
    def get_visitante_por_cpf(self) -> str:
        cpf = self.__pessoas_view.get_cpf()
        for visitante in self.__visitantes:
            if visitante.cpf == cpf:
                return visitante
            
    def get_cpf(self) -> str:
        return self.__pessoas_view.get_cpf()

    def trocar_sindico(self, novo_sindico: Sindico):
        self.__sindico = novo_sindico

    def display_sindico(self):
        self.__pessoas_view.mostrar_pessoa([self.__sindico])

    def display_moradores(self):
        for morador in self.__moradores:
            self.__pessoas_view.mostrar_pessoa([
                "-------------------------------",
                f"Nome: {morador.nome}",
                f"CPF: {morador.cpf}",
            ])

    def display_visitantes(self):
        for visitante in self.__visitantes:
            self.__pessoas_view.mostrar_pessoa([
                "-------------------------------",
                f"Nome: {visitante.nome}",
                f"CPF: {visitante.cpf}",
            ])
