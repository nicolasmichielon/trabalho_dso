
from controllers.ocorrencia_controller import OcorrenciaController
from controllers.pessoa_controller import PessoaController
from controllers.gasto_controller import GastoController
from controllers.estacionamento_controller import EstacionamentoController
from controllers.reserva_controller import ReservaController
from exceptions.entrada_invalida_exception import EntradaInvalidaException


class MasterController():
    def __init__(self):
        self.__ocorrencia_controller = OcorrenciaController(self)
        self.__pessoa_controller = PessoaController(self)
        self.__gasto_controller = GastoController(self)
        self.__estacionamento_controller = EstacionamentoController(self)
        self.__reserva_controller = ReservaController(self)

    def iniciarSistema(self):
        entrada = None
        print("================== MENU ==================")
        print("0: Fechar o sistema")
        print("1: Entrar no Menu de Pessoas")
        print("2: Entrar no Menu de Ocorrencias")
        print("3: Entrar no Menu do Estacionamento")
        print("4: Entrar no Menu de Gastos")
        print("===========================================")
        try:
            entrada = int(input("Escolha: "))
        except:
            print(EntradaInvalidaException())
            return True
        if entrada == 0:
            return False
        elif entrada == 1:
            switch = self.menuPessoa()
            while switch:
                switch = self.menuPessoa()
        elif entrada == 2:
            switch = self.menuOcorrencia()
            while switch:
                switch = self.menuOcorrencia()
        elif entrada == 3:
            switch = self.menuEstacionamento()
            while switch:
                switch = self.menuEstacionamento()
        elif entrada == 4:
            switch = self.menuGasto()
            while switch:
                switch = self.menuGasto()
        else: 
            print(EntradaInvalidaException())
        return True
    
    def menuPessoa(self):
        entrada = None
        print("================== MENU DE PESSOAS ==================")
        print("0: Retornar ao Menu Princial")
        print("1: Adicionar Morador")
        print("2: Adicionar Visitante")
        print("3: Adicionar Sindico")
        print("4: Visualizar todos os moradores")
        print("5: Visualizar todos os visitantes")
        print("6: Visualizar sindico")
        try:
            entrada = int(input("Escolha: "))
        except:
            print(EntradaInvalidaException())
            return True
        if entrada == 0:
            return False
        elif entrada == 1:
            self.__pessoa_controller.adicionar_morador()
        elif entrada == 2:
            self.__pessoa_controller.adicionar_visitante()
        elif entrada == 3:
            self.__pessoa_controller.adicionar_sindico()
        elif entrada == 4:
            self.__pessoa_controller.display_moradores()
        elif entrada == 5:
            self.__pessoa_controller.display_visitantes()
        elif entrada == 6:
            self.__pessoa_controller.display_sindico()
        else: 
            print(EntradaInvalidaException())
        return True

    def menuEstacionamento(self):
        entrada = None
        print("================== MENU DO ESTACIONAMENTO ==================")
        print("0: Retornar ao Menu Princial")
        print("1: Visualizar estacionamento")
        print("2: Ocupar vaga")
        print("3: Desocupar vaga")
        print("4: Visualizar vaga")
        try:
            entrada = int(input("Escolha: "))
        except:
            print(EntradaInvalidaException())
            return True
        if entrada == 0:
            return False
        elif entrada == 1:
            self.__estacionamento_controller.display_vagas()
        elif entrada == 2:
            self.__estacionamento_controller.ocupar_vaga()
        elif entrada == 3:
            self.__estacionamento_controller.desocupar_vaga()
        elif entrada == 4:
            self.__estacionamento_controller.display_vaga()
        else: 
            print(EntradaInvalidaException())
        return True

    def menuOcorrencia(self):
        entrada = None
        print("================== MENU DE OCORRENCIAS ==================")
        print("0: Retornar ao Menu Princial")
        print("1: Criar Ocorrencia")
        print("2: Buscar Ocorrencia por CPF de morador")
        print("3: Visualizar todas as ocorrências")
        try:
            entrada = int(input("Escolha: "))
        except:
            print(EntradaInvalidaException())
            return True
        if entrada == 0:
            return False
        elif entrada == 1:
            self.__ocorrencia_controller.adicionar_ocorrencia()
        elif entrada == 2:
            self.__ocorrencia_controller.busca_ocorrencias_por_cpf_de_morador()
        elif entrada == 3:
            self.__ocorrencia_controller.busca_ocorrencias()
        else: 
            print(EntradaInvalidaException())
        return True

    def menuGasto(self):
        entrada = None
        print("================== MENU DE GASTOS ==================")
        print("0: Retornar ao Menu Princial")
        print("1: Cadastrar gasto")
        print("2: Visualizar todos os gastos")
        print("3: Visualizar gasto por morador")
        try:
            entrada = int(input("Escolha: "))
        except:
            print(EntradaInvalidaException())
            return True
        if entrada == 0:
            return False
        elif entrada == 8:
            self.__gasto_controller.adicionar_gasto()
        elif entrada == 9:
            self.__gasto_controller.listar_gastos()
        elif entrada == 10:
            self.__gasto_controller.listar_gasto_por_cpf()
        else: 
            print(EntradaInvalidaException())
        return True



    @property
    def ocorrencia_controller(self):
        return self.__ocorrencia_controller
    
    @ocorrencia_controller.setter
    def ocorrencia_controller(self, oc_co):
        self.__ocorrencia_controller = oc_co

    @property
    def pessoa_controller(self):
        return self.__pessoa_controller
    
    @pessoa_controller.setter
    def pessoa_controller(self, pe_co):
        self.__pessoa_controller = pe_co

    @property
    def gasto_controller(self):
        return self.__gasto_controller
    
    @gasto_controller.setter
    def gasto_controller(self, ga_co):
        self.gasto_controller = ga_co

    @property
    def estacionamento_controller(self):
        return self.__estacionamento_controller
    
    @estacionamento_controller.setter
    def estacionamento_controller(self, es_co):
        self.estacionamento_controller = es_co

    @property
    def reserva_controller(self):
        return self.__reserva_controller
    
    @reserva_controller.setter
    def reserva_controller(self, re_co):
        self.reserva_controller = re_co