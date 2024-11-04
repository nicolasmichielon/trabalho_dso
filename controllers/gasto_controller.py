from models.gasto import Gasto
from views.gasto_view import GastoView
from exceptions.dados_invalidos_exception import DadosInvalidosException
from exceptions.morador_nao_encontrado_exception import MoradorNaoEncontradoException
from exceptions.nenhum_gasto_pro_cpf_exception import NenhumGastoProCPFException
from exceptions.nenhum_gasto_exception import NenhumGastoException

class GastoController():
    def __init__(self, master_controller) -> None:
        self.__master_controller = master_controller
        self.__gastos = []
        self.__gastos_view = GastoView()

    def adicionar_gasto(self):
        try:
            dados = self.__gastos_view.get_gasto()
            morador = self.__master_controller.pessoa_controller.busca_morador_por_cpf(self.__gastos_view.get_cpf())
            if morador == None:
                raise MoradorNaoEncontradoException()
            gasto = Gasto(dados.get("valor"), morador, False, dados.get("tipo"))
            self.__gastos.append(gasto)
        except MoradorNaoEncontradoException as e:
            print()
            print(e)
            print()
        except:
            print()
            print(DadosInvalidosException())
            print()


    def listar_gasto_por_cpf(self):
        try:
            cpf = self.__master_controller.pessoa_controller.get_cpf()
            existe_morador = self.__master_controller.pessoa_controller.busca_morador_por_cpf(cpf)
            if existe_morador == None:
                raise MoradorNaoEncontradoException()
            if len(self.__gastos) > 0:
                for gasto in self.__gastos:
                    if gasto.morador.cpf == cpf:
                        self.__gastos_view.mostrar_gastos([
                            "---------------------",
                            f"Valor: {gasto.valor}",
                            f"Tipo: {gasto.tipo_de_gasto}",
                            f"Pago? {"Sim" if gasto.pago else "Não"}"
                        ])
                print()
                print(NenhumGastoProCPFException())
                print()
            else:
                print()
                print(NenhumGastoException())
                print()
        except MoradorNaoEncontradoException as e:
            print()
            print(e)
            print()

    def listar_gastos(self):
        try:
            if len(self.__gastos) > 0:
                for gasto in self.__gastos:
                    self.__gastos_view.mostrar_gastos([
                        "---------------------",
                        f"CPF: {gasto.morador.cpf}",
                        f"Valor: {gasto.valor}",
                        f"Tipo: {gasto.tipo_de_gasto}",
                        f"Pago? {"Sim" if gasto.pago else "Não"}"
                    ])
            else:
                raise NenhumGastoException()
        except NenhumGastoException as e:
            print()
            print(e)
            print()

    def total_de_gastos_do_morador(self, cpf) -> int:
        try:
            existe_morador = self.__master_controller.pessoa_controller.busca_morador_por_cpf(cpf)
            if existe_morador == None:
                raise MoradorNaoEncontradoException()
            if len(self.__gastos) > 0:
                total = 0
                for gasto in self.__gastos:
                    if gasto.morador.cpf == cpf:
                        total += gasto.valor
                self.__gastos_view.mostrar_gastos([
                    "---------------------",
                    f"Gastos totais: {total}"
                    "---------------------"
                ])
            else:
                print()
                print(NenhumGastoException())
                print()
        except MoradorNaoEncontradoException as e:
            print()
            print(e)
            print()



