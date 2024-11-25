from models.vaga import Vaga

class Estacionamento:
    def __init__(self, qtd_vagas_morador: int, qtd_vagas_visitante: int, qtd_vagas_sindico: int = 1):
        self.__vagas = []
        for i in range(1, qtd_vagas_morador + 1):
            self.__vagas.append(Vaga(i, None, "Morador"))
        for i in range(1, qtd_vagas_sindico + 1):
            self.__vagas.append(Vaga(i + qtd_vagas_morador, None, "Sindico"))
        for i in range(1, qtd_vagas_visitante + 1):
            self.__vagas.append(Vaga(i + qtd_vagas_morador + 1, None, "Visitante"))

    @property
    def vagas(self):
        return self.__vagas
