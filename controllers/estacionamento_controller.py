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
            linhas = []
            linhaNum = ""
            linhaEst = ""
            for vaga in self.__vagas:
                if vaga.vaga_de_morador:
                    morador = "M"
                else:
                    morador = "V"

                if vaga.numero < 10:
                    linhaNum += f" {vaga.numero} {morador}  "
                else:
                    linhaNum += f"{vaga.numero} {morador}  "

                if vaga.ocupado:
                    linhaEst += f"  O   "
                else:
                    linhaEst += f"  -   "

                if vaga.numero % 3 == 0:
                    linhas.append(linhaNum)
                    linhas.append(linhaEst)
                    linhaNum = ""
                    linhaEst = ""

            self.__estacionamento_view.mostrar_vagas(linhas)

    def ocupar_vaga(self):
        try:
            cpf_pessoa = self.__estacionamento_view.get_cpf()
            num_vaga = self.__estacionamento_view.get_vaga()
            for v in self.__vagas:
                if v.numero == num_vaga:
                    if v.ocupado:
                        raise ValueError
                    else:
                        v.ocupado = True
                        v.pessoa = cpf_pessoa
                        print("Vaga ocupada")
                        return
        except ValueError:
            print("Esta vaga ja esta ocupada")

    def desocupar_vaga(self):
        try:
            cpf_pessoa = self.__estacionamento_view.get_cpf()
            num_vaga = self.__estacionamento_view.get_vaga()
            for v in self.__vagas:
                if v.numero == num_vaga and cpf_pessoa == v.pessoa:
                    if v.ocupado:
                        v.ocupado = False
                        print("Vaga desocupada")
                        return
                    else:
                        raise ValueError
        except ValueError:
            print("Esta vaga nao esta ocupada")

    def display_vaga(self):
        try:
            num_vaga = self.__estacionamento_view.get_vaga()
            for v in self.__vagas:
                if v.numero == num_vaga:                    
                    if v.vaga_de_morador:
                        tipo = "Morador" 
                    else:
                        tipo = "Visitante"

                    if v.ocupado:
                        pessoa = self.__master_controller.pessoa_controller.busca_morador_por_cpf(int(v.pessoa))
                        pessoa = pessoa.nome
                    else:
                        pessoa = "Ninguem"
                    self.__estacionamento_view.mostrar_vagas([
                        "------------------------------------",
                        f"Vaga {v.numero}",
                        f"Ocupado: {v.ocupado}",
                        f"Vaga de {tipo}",
                        f"Ocupado por {pessoa}",
                        "-------------------------------------"
                    ])
        except:
            print("Essa vaga nao existe")
