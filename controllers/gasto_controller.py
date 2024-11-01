from models.gasto import Gasto
from views.gasto_view import GastoView

class GastoController():
    def __init__(self, master_controller) -> None:
        self.__master_controller = master_controller
        self.__gastos = []
        self.__gastos_view = GastoView()

    def adicionar_gasto(self):
        dados = self.__gastos_view.get_gasto()
        morador = self.__master_controller.pessoa_controller.busca_morador_por_cpf()
        gasto = Gasto(dados.get("valor"), morador, False, dados.get("tipo"))
        self.__gastos.append(gasto)

    def listar_gasto_por_cpf(self):
        cpf = self.__master_controller.pessoa_controller.get_cpf()
        for gasto in self.__gastos:
            if gasto.morador.cpf == cpf:
                self.__gastos_view.mostrar_gastos([
                    "---------------------",
                    f"Valor: {gasto.valor}",
                    f"Tipo: {gasto.tipo_de_gasto}",
                    f"Pago? {"Sim" if gasto.pago else "Não"}"
                ])

    def listar_gastos(self):
        for gasto in self.__gastos:
            self.__gastos_view.mostrar_gastos([
                "---------------------",
                f"CPF: {gasto.morador.cpf}",
                f"Valor: {gasto.valor}",
                f"Tipo: {gasto.tipo_de_gasto}",
                f"Pago? {"Sim" if gasto.pago else "Não"}"
            ])

    def total_de_gastos_do_morador(self, cpf) -> int:
        total = 0
        for gasto in self.__gastos:
            if gasto.morador.cpf == cpf:
                total += gasto.valor
        self.__gastos_view.mostrar_gastos([
            "---------------------",
            f"Gastos totais: {total}"
            "---------------------"
        ])