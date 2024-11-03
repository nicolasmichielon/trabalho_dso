
from controllers.ocorrencia_controller import OcorrenciaController
from controllers.pessoa_controller import PessoaController
from controllers.gasto_controller import GastoController
from controllers.estacionamento_controller import EstacionamentoController
from controllers.reserva_controller import ReservaController


class MasterController():
    def __init__(self):
        self.__ocorrencia_controller = OcorrenciaController(self)
        self.__pessoa_controller = PessoaController(self)
        self.__gasto_controller = GastoController(self)
        self.__estacionamento_controller = EstacionamentoController(self)
        self.__reserva_controller = ReservaController(self)

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