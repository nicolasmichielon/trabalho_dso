
from ocorrencia_controller import OcorrenciaController
from pessoa_controller import PessoaController


class MasterController():
    def __init__(self):
        self.__ocorrencia_controller = OcorrenciaController(self)
        self.__pessoa_controller = PessoaController(self)

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