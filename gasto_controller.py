from gasto import Gasto
from gasto_view import GastoView

class GastoController():
    def __init__(self, master_controller) -> None:
        self.__master_controller = master_controller
        self.__gastos = []
        self.__gastos_view = GastoView()

    def adicionar_gasto(self):
        dados = self.__gastos_view.get_gasto()
        gasto = Gasto(dados.get("valor"), dados.get("cpf"), False, dados.get("tipo"))
        self.__gastos.append(gasto)

    def listar_gasto_por_cpf(self):
        cpf = self.__gastos_view.get_cpf()
        for gasto in self.__gastos:
            if gasto.cpf == cpf:
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
                f"CPF: {gasto.cpf}",
                f"Valor: {gasto.valor}",
                f"Tipo: {gasto.tipo_de_gasto}",
                f"Pago? {"Sim" if gasto.pago else "Não"}"
            ])

    def total_de_gastos_do_morador(self, cpf) -> int:
        total = 0
        for gasto in self.__gastos:
            if gasto.cpf == cpf:
                total += gasto.valor
        self.__gastos_view.mostrar_gastos([
            "---------------------",
            f"Gastos totais: {total}"
            "---------------------"
        ])