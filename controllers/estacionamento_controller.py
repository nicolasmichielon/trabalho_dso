from models.estacionamento import Estacionamento
from views.estacionamento_view import EstacionamentoView

class EstacionamentoController():
    def __init__(self, master_controller) -> None:
        self.__master_controller = master_controller
        self.__estacionamento = Estacionamento(12, 3)
        self.__vagas = self.__estacionamento.vagas
        self.__estacionamento_view = EstacionamentoView()

    def display_vagas(self):
            numeros = []
            estado = []
            for vaga in self.__vagas:
                numeros.append(f"{vaga.numero}   ")
                if vaga.ocupado:
                    estado.append("O   ")
                else:
                    estado.append("-   ")

            linhas_numeros = []
            linhas_estado = []
            for i in range(0, len(numeros), 3):
                linhas_numeros.append("".join(numeros[i:i+3]).strip())
                linhas_estado.append("".join(estado[i:i+3]).strip())

            linhas = [f"{num}\n{est}" for num, est in zip(linhas_numeros, linhas_estado)]
            self.__estacionamento_view.mostrar_vagas(linhas)

    def ocupar_vaga(self):
        num_vaga = self.__estacionamento_view.get_vaga()
        print(num_vaga)
        for v in self.__vagas:
            print(v.numero)
            print(v.vaga_de_morador)
            print(v.ocupado)
            if v.numero == num_vaga:
                v.ocupado = True
                print("nicholas")
            print(v.ocupado)