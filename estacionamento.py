from vaga import Vaga

class Estacionamento:
    def __init__(self, vagas: Vaga):
        self.__vagas = vagas

    def listar_vagas(self):
        return [vaga.numero for vaga in self.__vagas]

    def vagas_ocupadas(self):
        return [vaga.numero for vaga in self.__vagas if vaga.ocupado]

    def vagas_disponiveis(self):
        return [vaga.numero for vaga in self.__vagas if not vaga.ocupado]
