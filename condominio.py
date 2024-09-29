class Condominio():
    def __init__(self, id: int, endereco: str, nome: str):
        self.__id = id
        self.__endereco = endereco
        self.__nome = nome

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def adicionar_visitante(self, visitante):
        self.__visitantes.append(visitante)

    def adicionar_morador(self, morador):
        self.__moradores.append(morador)

    def trocar_sindico(self, sindico_antigo, sindico_novo):
        if self.__sindico == sindico_antigo:
            self.__sindico = sindico_novo
        else:
            raise ValueError("O síndico antigo não corresponde ao síndico atual.")