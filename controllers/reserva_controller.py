from models.reserva import Reserva
from views.reserva_view import ReservaView
from exceptions.morador_nao_encontrado_exception import MoradorNaoEncontradoException
from exceptions.nenhuma_reserva_exception import NenhumaReservaException
from exceptions.nenhuma_reserva_pro_cpf_exception import NenhumaReservaProCPFException
from exceptions.id_invalido_exception import IDInvalidoException

class ReservaController:
    def __init__(self, master_controller) -> None:
        self.__master_controller = master_controller
        self.__reserva_view = ReservaView()
        self.__reservas = []

    @property
    def reservas(self):
        return self.__reservas
    
    def lista_reservas(self):
        try:
            if len(self.__reservas) > 0:
                for reserva in self.__reservas:
                    self.__reserva_view.mostraReserva([
                        f"ID Reserva: {reserva.id}\n"
                        f"Solicitante: {reserva.solicitante.nome}\n"
                        f"Data: {reserva.data_reserva}\n"
                        f"Hora ínicio: {reserva.hora_inicio}\n"
                        f"Hora fim: {reserva.hora_fim}\n"
                        f"Custo: {reserva.custo}\n"
                        f"Espaço: {reserva.espaco}"
                    ])
            else:
                raise NenhumaReservaException()
        except NenhumaReservaException as e:
            self.__reserva_view.mostra_linhas([
                f"\n{e}\n"
            ])



    def lista_reservas_por_cpf(self):
        try:
            cpf = self.__master_controller.pessoa_controller.get_cpf()
            existe_morador = self.__master_controller.pessoa_controller.busca_morador_por_cpf(cpf)
            if existe_morador == None:
                raise MoradorNaoEncontradoException()
            if len(self.__reservas) > 0:
                for reserva in self.__reservas:
                    if reserva.solicitante.cpf == cpf:
                        self.__reserva_view.mostraReserva([
                            f"ID Reserva: {reserva.id}\n"
                            f"Solicitante: {reserva.solicitante.nome}\n"
                            f"Data: {reserva.data_reserva}\n"
                            f"Hora ínicio: {reserva.hora_inicio}\n"
                            f"Hora fim: {reserva.hora_fim}\n"
                            f"Custo: {reserva.custo}\n"
                            f"Espaço: {reserva.espaco}"
                        ])
                        return
                raise NenhumaReservaProCPFException()
            else:
                raise NenhumaReservaException()
        except MoradorNaoEncontradoException as e:
            self.__reserva_view.mostra_linhas([
                f"\n{e}\n"
            ])
        except NenhumaReservaProCPFException as e:
            self.__reserva_view.mostra_linhas([
                f"\n{e}\n"
            ])
        except NenhumaReservaException as e:
            self.__reserva_view.mostra_linhas([
                f"\n{e}\n"
            ])

    def adicionar_reserva(self):
        try:
            dados = self.__reserva_view.get_reserva()

            if len(self.__reservas) > 0:
                next_id = self.__reservas[-1].id + 1
            else:
                next_id = 1

            morador = self.__master_controller.pessoa_controller.busca_morador_por_cpf(dados["cpf_solicitante"])
            if morador == None:
                raise MoradorNaoEncontradoException()
            reserva = Reserva(next_id, morador, dados["data_reserva"], dados["hora_inicio"], dados["hora_fim"], dados["espaco"])
            self.__master_controller.gasto_controller.adicionar_gasto_reserva(reserva.custo, morador)
            self.__reservas.append(reserva)
        except MoradorNaoEncontradoException as e:
            self.__reserva_view.mostra_linhas([
                f"\n{e}\n"
            ])

    def remover_reserva(self):
        try:
            id = self.__reserva_view.get_reserva_id()
            for reserva in self.__reservas:
                if reserva.id == id:
                    self.__reservas.remove(reserva)
                    self.__reserva_view.reserva_removida()
                    return
            raise IDInvalidoException()
        except IDInvalidoException as e:
            self.__reserva_view.mostra_linhas([
                f"\n{e}\n"
            ])