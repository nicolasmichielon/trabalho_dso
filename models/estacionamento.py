from vaga import Vaga

class Estacionamento:
    def __init__(self, qtd_vagas_morador: int, qtd_vagas_visitante: int):
        self.__vagas = []
        for i in range(1, qtd_vagas_morador + 1):
            self.__vagas.append(Vaga(i, True))
        for i in range(1, qtd_vagas_visitante + 1):
            self.__vagas.append(Vaga(i + qtd_vagas_morador, False))

    @property
    def vagas(self):
        return self.__vagas

    def ocupar_vaga(self, numero: int):
        for vaga in self.__vagas:
            if vaga.numero == numero:
                vaga.ocupar()
                break

    def desocupar_vaga(self, numero: int):
        for vaga in self.__vagas:
            if vaga.numero == numero:
                vaga.desocupar()
                break
