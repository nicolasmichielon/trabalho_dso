from daos.dao import DAO
from models.estacionamento import Estacionamento

class EstacionamentoDAO(DAO):
    def __init__(self):
        super().__init__('vagas.pkl')

    def initialize_vagas(self, estacionamento: Estacionamento):
        self.add("estacionamento", estacionamento)

    def ocupar_vaga(self, vaga, pessoa):
        novo_estacionamento = self.get("estacionamento")
        for v in novo_estacionamento.vagas:
            if v.numero == vaga.numero:
                v.ocupado = True
                v.pessoa = pessoa
        self.update("estacionamento", novo_estacionamento)

    def desocupar_vaga(self, vaga):
        novo_estacionamento = self.get("estacionamento")
        for v in novo_estacionamento.vagas:
            if v.numero == vaga.numero:
                v.ocupado = False
                v.pessoa = None
        self.update("estacionamento", novo_estacionamento)

    def get_vagas(self):
        return self.get("estacionamento").vagas
