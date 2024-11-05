from models.gasto import Gasto
from views.gasto_view import GastoView
from exceptions.dados_invalidos_exception import DadosInvalidosException
from exceptions.morador_nao_encontrado_exception import MoradorNaoEncontradoException
from exceptions.nenhum_gasto_pro_cpf_exception import NenhumGastoProCPFException
from exceptions.nenhum_gasto_exception import NenhumGastoException
from exceptions.id_invalido_exception import IDInvalidoException

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
            if len(self.__gastos) == 0:
                id = 1
            else:
                id = self.__gastos[-1].id + 1
            gasto = Gasto(id, dados.get("valor"), morador, False, dados.get("tipo"))
            self.__gastos.append(gasto)
        except MoradorNaoEncontradoException as e:
            print()
            print(e)
            print()

    def adicionar_gasto_reserva(self, valor, morador):
        if morador == None:
            raise MoradorNaoEncontradoException()
        if len(self.__gastos) == 0:
            id = 1
        else:
            id = self.__gastos[-1].id + 1
        gasto = Gasto(id, valor, morador, False, "reserva")
        self.__gastos.append(gasto)

    def listar_gasto_por_cpf(self):
        try:
            cpf = self.__master_controller.pessoa_controller.get_cpf()
            existe_morador = self.__master_controller.pessoa_controller.busca_morador_por_cpf(cpf)
            if existe_morador == None:
                raise MoradorNaoEncontradoException()
            if len(self.__gastos) > 0:
                existe_gasto = 0
                for gasto in self.__gastos:
                    if gasto.morador.cpf == cpf:
                        self.__gastos_view.mostrar_gastos([
                            "--------------------------",
                            f"ID: {gasto.id}", 
                            f"Valor: {gasto.valor}",
                            f"Tipo: {gasto.tipo_de_gasto}",
                            f"Pago? {"Sim" if gasto.pago else "Não"}"
                        ])
                        existe_gasto = 1
                if not existe_gasto:
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

    def gerar_relatorio(self):
        try:
            if len(self.__gastos) > 0:
                total_gastos = sum(gasto.valor for gasto in self.__gastos)
                quantidade_gastos = len(self.__gastos)
                quantidade_moradores = len(self.__master_controller.pessoa_controller.moradores)
                media_gastos = total_gastos / quantidade_moradores

                self.__gastos_view.mostrar_gastos([
                    "---------------------",
                    f"Total de gastos gerados no condomínio: R${total_gastos}",
                    f"Quantidade de gastos no condomínio: {quantidade_gastos}",
                    f"Média de gastos por morador: R${media_gastos:.2f}",
                    "---------------------"
                ])
            else:
                print()
                print(NenhumGastoException())
                print()
        except Exception as e:
            print()
            print(e)
            print()

    def pagar_gasto(self):
        try:
            cpf = self.__gastos_view.get_cpf()
            ids_validos = []
            for gasto in self.__gastos:
                if cpf == gasto.morador.cpf and gasto.pago == False:
                    self.__gastos_view.mostrar_gastos([
                        "--------------------------",
                        f"ID: {gasto.id}", 
                        f"Valor: {gasto.valor}",
                        f"Tipo: {gasto.tipo_de_gasto}",
                        f"Pago? {"Sim" if gasto.pago else "Não"}"
                    ])
                    ids_validos.append(gasto.id)
            gasto_id = self.__gastos_view.get_gasto_id()
            if gasto_id not in ids_validos:
                raise IDInvalidoException()
            else:
                self.__gastos[gasto_id - 1].pago = True
                self.__gastos_view.gasto_pago()
        except IDInvalidoException as e:
            print()
            print(e)
            print()


