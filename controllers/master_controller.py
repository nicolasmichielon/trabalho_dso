from controllers.ocorrencia_controller import OcorrenciaController
from controllers.pessoa_controller import PessoaController
from controllers.gasto_controller import GastoController
from controllers.estacionamento_controller import EstacionamentoController
from controllers.reserva_controller import ReservaController
from exceptions.entrada_invalida_exception import EntradaInvalidaException
from views.master_view import MasterView


class MasterController():
    def __init__(self):
        self.__ocorrencia_controller = OcorrenciaController(self)
        self.__pessoa_controller = PessoaController(self)
        self.__gasto_controller = GastoController(self)
        self.__estacionamento_controller = EstacionamentoController(self)
        self.__reserva_controller = ReservaController(self)
        self.__master_view = MasterView()

    def iniciarSistema(self):
        entrada = None
        self.__master_view.mostra_opcoes([
            "================== MENU ==================",
            "0: Fechar o sistema",
            "1: Entrar no Menu de Pessoas",
            "2: Entrar no Menu de Ocorrencias",
            "3: Entrar no Menu do Estacionamento",
            "4: Entrar no Menu de Gastos",
            "5: Entrar no Menu de Reservas",
            "==========================================="
        ])
        try:
            entrada = self.__master_view.solicitar_resposta()
        except:
            self.__master_view.mostra_erro(EntradaInvalidaException)
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
        elif entrada == 5:
            switch = self.menuReserva()
            while switch:
                switch = self.menuReserva()
        else: 
            self.__master_view.mostra_erro(EntradaInvalidaException)
        return True
    
    def menuPessoa(self):
        entrada = None
        self.__master_view.mostra_opcoes([
            "================== MENU DE PESSOAS ==================",
            "0: Retornar ao Menu Princial",
            "1: Adicionar Morador",
            "2: Adicionar Visitante",
            "3: Adicionar Sindico",
            "4: Visualizar todos os moradores",
            "5: Visualizar todos os visitantes",
            "6: Visualizar sindico",
            "7: Remover Morador por CPF",
            "8: Remover Visitante por CPF",
        ])
        try:
            entrada = self.__master_view.solicitar_resposta()
        except:
            self.__master_view.mostra_erro(EntradaInvalidaException)
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
        elif entrada == 7:
            self.__pessoa_controller.remover_morador()
        elif entrada == 8:
            self.__pessoa_controller.remover_visitante()
        else: 
            self.__master_view.mostra_erro(EntradaInvalidaException)
        return True

    def menuEstacionamento(self):
        entrada = None
        self.__master_view.mostra_opcoes([
            "================== MENU DO ESTACIONAMENTO ==================",
            "0: Retornar ao Menu Principal",
            "1: Visualizar estacionamento",
            "2: Ocupar vaga",
            "3: Desocupar vaga",
            "4: Visualizar vaga",
        ])
        try:
            entrada = self.__master_view.solicitar_resposta()
        except:
            self.__master_view.mostra_erro(EntradaInvalidaException)
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
            self.__master_view.mostra_erro(EntradaInvalidaException)
        return True

    def menuOcorrencia(self):
        entrada = None
        self.__master_view.mostra_opcoes([
            "================== MENU DE OCORRENCIAS ==================",
            "0: Retornar ao Menu Principal",
            "1: Criar Ocorrencia",
            "2: Buscar Ocorrencia por CPF de morador",
            "3: Visualizar todas as ocorrências",
        ])
        try:
            entrada = self.__master_view.solicitar_resposta()
        except:
            self.__master_view.mostra_erro(EntradaInvalidaException)
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
            self.__master_view.mostra_erro(EntradaInvalidaException)
        return True

    def menuGasto(self):
        entrada = None
        self.__master_view.mostra_opcoes([
            "================== MENU DE GASTOS ==================",
            "0: Retornar ao Menu Principal",
            "1: Cadastrar gasto",
            "2: Visualizar todos os gastos",
            "3: Visualizar gasto por morador",
            "4: Gerar relatório geral de gastos",
            "5: Pagar gasto",
        ])
        try:
            entrada = self.__master_view.solicitar_resposta()
        except:
            self.__master_view.mostra_erro(EntradaInvalidaException)
            return True
        if entrada == 0:
            return False
        elif entrada == 1:
            self.__gasto_controller.adicionar_gasto()
        elif entrada == 2:
            self.__gasto_controller.listar_gastos()
        elif entrada == 3:
            self.__gasto_controller.listar_gasto_por_cpf()
        elif entrada == 4:
            self.__gasto_controller.gerar_relatorio()
        elif entrada == 5:
            self.__gasto_controller.pagar_gasto()
        else: 
            self.__master_view.mostra_erro(EntradaInvalidaException)
        return True
    
    def menuReserva(self):
        entrada = None
        self.__master_view.mostra_opcoes([
            "================== MENU DE RESERVAS ==================",
            "0: Retornar ao Menu Principal",
            "1: Cadastrar reserva",
            "2: Visualizar todas as reservas",
            "3: Visualizar reserva por morador",
            "4: Remover reserva por ID",
        ])
        try:
            entrada = self.__master_view.solicitar_resposta()
        except:
            self.__master_view.mostra_erro(EntradaInvalidaException)
            return True
        if entrada == 0:
            return False
        elif entrada == 1:
            self.__reserva_controller.adicionar_reserva()
        elif entrada == 2:
            self.__reserva_controller.lista_reservas()
        elif entrada == 3:
            self.__reserva_controller.lista_reservas_por_cpf()
        elif entrada == 4:
            self.__reserva_controller.remover_reserva()
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