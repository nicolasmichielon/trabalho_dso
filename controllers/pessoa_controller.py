from views.pessoa_view import PessoaView
from models.morador import Morador
from models.sindico import Sindico
from models.visitante import Visitante
from exceptions.pessoa_repetida_exception import PessoaRepetidaException
from exceptions.dados_invalidos_exception import DadosInvalidosException

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
            raise DadosInvalidosException()
        self.__sindico = sindico


    def adicionar_morador(self):
        try:
            dados = self.__pessoas_view.get_pessoa()
            morador = Morador(dados.get("nome"), dados.get("telefone"), dados.get("cpf"), dados.get("idade"))
            cpfs = []
            for morador in self.__moradores:
                cpfs.append(morador.cpf)
            for visitante in self.__visitantes:
                cpfs.append(visitante.cpf)
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
            morador = self.__pessoas_view.get_pessoa()
        except:
            raise DadosInvalidosException()
        if morador in self.__moradores:
            self.__moradores.remove(morador)
            self.__pessoas_view.mostrar_pessoa([morador])

    def remover_visitante(self):
        try:
            visitante = self.__pessoas_view.get_pessoa()
        except:
            raise DadosInvalidosException()
        if visitante in self.__visitantes:
            self.__visitantes.remove(visitante)
            self.__pessoas_view.mostrar_pessoa([visitante])

    def busca_morador_por_cpf(self, cpf) -> Morador:
        print(f"Procurando pelo CPF: {cpf}...")
        for morador in self.__moradores:
            if morador.cpf == cpf:
                self.__pessoas_view.mostrar_pessoa([
                    "-------------------------------",
                    f"Nome: {morador.nome}",
                    "-------------------------------"])
                return morador
        print("CPF nao encontrado")
        return None

    def busca_visitante_por_cpf(self, cpf) -> Visitante:
        print(f"Procurando pelo CPF: {cpf}...")
        for visitante in self.__visitantes:
            if visitante.cpf == cpf:
                self.__pessoas_view.mostrar_pessoa([
                    "-------------------------------",
                    f"Nome: {visitante.nome}",
                    "-------------------------------"])
                return visitante
        print("CPF nao encontrado")
        return None
            
    def get_sindico(self) -> Sindico:
        return self.__sindico

   # def busca_pessoa_por_cpf(self, cpf: int):
   #     if cpf == self.__sindico.cpf:
   #        return self.__sindico
   #     else:
   #         for v in self.__visitantes:
   #             if v.cpf == cpf:
   #                 return v
   #         for m in self.__moradores:
   #             if m.cpf == cpf:
   #                 return m
   #     return f"Pessoa nao encontrada no sistema..."

    def get_tipo_de_pessoa(self, cpf: int) -> str:
        if self.busca_morador_por_cpf(cpf):
            return f"Morador"
        elif self.busca_visitante_por_cpf(cpf):
            return f"Visitante"
        else:
            return f"Sindico"

            
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
