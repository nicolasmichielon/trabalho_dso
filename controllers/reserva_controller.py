from models.reserva import Reserva
from views.reserva_view import ReservaView
from exceptions.morador_nao_encontrado_exception import MoradorNaoEncontradoException
from exceptions.nenhuma_reserva_exception import NenhumaReservaException
from exceptions.nenhuma_reserva_pro_cpf_exception import NenhumaReservaProCPFException
from exceptions.id_invalido_exception import IDInvalidoException
from daos.reserva_dao import ReservaDAO

class ReservaController:
    def __init__(self, master_controller) -> None:
        self.__master_controller = master_controller
        self.__reserva_view = ReservaView()
        self.__reserva_dao = ReservaDAO()

    @property
    def reservas(self):
        return self.__reserva_dao.get_reservas()

    def lista_reservas(self):
        try:
            reservas = self.__reserva_dao.get_reservas()
            if len(reservas) > 0:
                for reserva in reservas:
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
            reservas = self.__reserva_dao.get_reservas()
            if len(reservas) > 0:
                for reserva in reservas:
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

            reservas = self.__reserva_dao.get_reservas()
            if len(reservas) > 0:
                next_id = max(reserva.id for reserva in reservas) + 1
            else:
                next_id = 1

            morador = self.__master_controller.pessoa_controller.busca_morador_por_cpf(dados["cpf_solicitante"])
            if morador == None:
                raise MoradorNaoEncontradoException()
            reserva = Reserva(next_id, morador, dados["data_reserva"], dados["hora_inicio"], dados["hora_fim"], dados["espaco"])
            self.__master_controller.gasto_controller.adicionar_gasto_reserva(reserva.custo, morador)
            self.__reserva_dao.adicionar_reserva(reserva)
        except MoradorNaoEncontradoException as e:
            self.__reserva_view.mostra_linhas([
                f"\n{e}\n"
            ])

    def remover_reserva(self):
        try:
            id = self.__reserva_view.get_reserva_id()
            reserva = self.__reserva_dao.buscar_reserva_por_id(id)
            if reserva:
                self.__reserva_dao.remover_reserva(id)
                self.__reserva_view.reserva_removida()
            else:
                raise IDInvalidoException()
        except IDInvalidoException as e:
            self.__reserva_view.mostra_linhas([
                f"\n{e}\n"
            ])