from models.gasto import Gasto
from views.gasto_view import GastoView
from exceptions.dados_invalidos_exception import DadosInvalidosException
from exceptions.morador_nao_encontrado_exception import MoradorNaoEncontradoException
from exceptions.nenhum_gasto_pro_cpf_exception import NenhumGastoProCPFException
from exceptions.nenhum_gasto_exception import NenhumGastoException
from exceptions.id_invalido_exception import IDInvalidoException
from daos.gasto_dao import GastoDAO

class GastoController():
    def __init__(self, master_controller) -> None:
        self.__master_controller = master_controller
        self.__gastos_view = GastoView()
        self.__gasto_dao = GastoDAO()

    def adicionar_gasto(self):
        try:
            dados = self.__gastos_view.get_gasto()
            morador = self.__master_controller.pessoa_controller.busca_morador_por_cpf(self.__master_controller.pessoa_controller.get_cpf())
            if morador == None:
                raise MoradorNaoEncontradoException()
            id = self.__gasto_dao.get_next_id()
            gasto = Gasto(id, dados.get("valor"), morador, False, dados.get("descricao"))
            self.__gasto_dao.adicionar_gasto(gasto)
        except MoradorNaoEncontradoException as e:
            self.__gastos_view.mostra_linhas([
                f"\n{e}\n"
            ])

    def adicionar_gasto_reserva(self, valor, morador):
        if morador == None:
            raise MoradorNaoEncontradoException()
        id = self.__gasto_dao.get_next_id()
        gasto = Gasto(id, valor, morador, False, "reserva")
        self.__gasto_dao.adicionar_gasto(gasto)

    def listar_gasto_por_cpf(self):
        try:
            cpf = self.__master_controller.pessoa_controller.get_cpf()
            existe_morador = self.__master_controller.pessoa_controller.busca_morador_por_cpf(cpf)
            if existe_morador == None:
                raise MoradorNaoEncontradoException()
            gastos = self.__gasto_dao.get_gastos()
            if len(gastos) > 0:
                existe_gasto = 0
                for gasto in gastos:
                    if gasto.morador.cpf == cpf:
                        self.__gastos_view.mostrar_gasto([
                            "--------------------------",
                            f"ID: {gasto.id}", 
                            f"Valor: {gasto.valor}",
                            f"Tipo: {gasto.tipo_de_gasto}",
                            f"Pago? {'Sim' if gasto.pago else 'Não'}"
                        ])
                        existe_gasto = 1
                if not existe_gasto:
                    self.__gastos_view.mostra_linhas([
                        f"\n{NenhumGastoProCPFException()}\n"
                    ])
            else:
                self.__gastos_view.mostra_linhas([
                   f"\n{NenhumGastoException()}\n"
                ])
        except MoradorNaoEncontradoException as e:
            self.__gastos_view.mostra_linhas([
                f"\n{e}\n"
            ])

    def listar_gastos(self):
        try:
            gastos = self.__gasto_dao.get_gastos()
            if len(gastos) > 0:
                for gasto in gastos:
                    self.__gastos_view.mostrar_gasto([
                        "---------------------",
                        f"CPF: {gasto.morador.cpf}",
                        f"Valor: {gasto.valor}",
                        f"Tipo: {gasto.tipo_de_gasto}",
                        f"Pago? {'Sim' if gasto.pago else 'Não'}"
                    ])
            else:
                raise NenhumGastoException()
        except NenhumGastoException as e:
            self.__gastos_view.mostra_linhas([
                f"\n{e}\n"
            ])

    def total_de_gastos_do_morador(self, cpf) -> int:
        try:
            existe_morador = self.__master_controller.pessoa_controller.busca_morador_por_cpf(cpf)
            if existe_morador == None:
                raise MoradorNaoEncontradoException()
            gastos = self.__gasto_dao.get_gastos()
            if len(gastos) > 0:
                total = 0
                for gasto in gastos:
                    if gasto.morador.cpf == cpf:
                        total += gasto.valor
                self.__gastos_view.mostrar_gasto([
                    "---------------------",
                    f"Gastos totais: {total}"
                    "---------------------"
                ])
            else:
                self.__gastos_view.mostra_linhas([
                    f"\n{NenhumGastoException()}\n"
                ])
        except MoradorNaoEncontradoException as e:
            self.__gastos_view.mostra_linhas([
                f"\n{e}\n"
            ])

    def gerar_relatorio(self):
        try:
            gastos = self.__gasto_dao.get_gastos()
            if len(gastos) > 0:
                total_gastos = sum(gasto.valor for gasto in gastos)
                quantidade_gastos = len(gastos)
                quantidade_moradores = len(self.__master_controller.pessoa_controller.moradores)
                media_gastos = total_gastos / quantidade_moradores

                self.__gastos_view.mostrar_gasto([
                    "---------------------",
                    f"Total de gastos gerados no condomínio: R${total_gastos}",
                    f"Quantidade de gastos no condomínio: {quantidade_gastos}",
                    f"Média de gastos por morador: R${media_gastos:.2f}",
                    "---------------------"
                ])
            else:
                self.__gastos_view.mostra_linhas([
                    f"\n{NenhumGastoException}\n"
                ])
        except Exception as e:
            self.__gastos_view.mostra_linhas([
                f"\n{e}\n"
            ])

    def pagar_gasto(self):
        try:
            cpf = self.__master_controller.pessoa_controller.get_cpf()
            ids_validos = []
            gastos = self.__gasto_dao.get_gastos()
            for gasto in gastos:
                if cpf == gasto.morador.cpf and gasto.pago == False:
                    self.__gastos_view.mostrar_gasto([
                        "--------------------------",
                        f"ID: {gasto.id}", 
                        f"Valor: {gasto.valor}",
                        f"Tipo: {gasto.tipo_de_gasto}",
                        f"Pago? {'Sim' if gasto.pago else 'Não'}"
                    ])
                    ids_validos.append(gasto.id)
            gasto_id = self.__gastos_view.get_gasto_id()
            if gasto_id not in ids_validos:
                raise IDInvalidoException()
            else:
                gasto = self.__gasto_dao.buscar_gasto_por_id(gasto_id)
                gasto.pago = True
                self.__gasto_dao.pagar_gasto(gasto)
                self.__gastos_view.gasto_pago()
        except IDInvalidoException as e:
            self.__gastos_view.mostra_linhas([
                f"\n{e}\n"
            ])


