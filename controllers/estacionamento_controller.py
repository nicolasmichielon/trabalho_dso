from models.estacionamento import Estacionamento
from views.estacionamento_view import EstacionamentoView
from exceptions.tipo_vaga_incompativel_exception import TipoVagaIncompativelException
from daos.estacionamento_dao import EstacionamentoDAO

class EstacionamentoController():
    def __init__(self, master_controller) -> None:
        self.__master_controller = master_controller
        self.__estacionamento_view = EstacionamentoView()

        self.__estacionamento = Estacionamento(11, 3)
        # self.__vagas = self.__estacionamento.vagas
        
        self.__estacionamento_dao = EstacionamentoDAO()
        self.__estacionamento_dao.initialize_vagas(self.__estacionamento)

    def display_vagas(self):
        numeros = []
        estado = []
        linhas = []
        linhaNum = ""
        linhaEst = ""
        for vaga in self.__estacionamento_dao.get_vagas():
            if vaga.numero < 10:
                linhaNum += f" {vaga.numero} {vaga.tipo_de_vaga[0]}  "
            else:
                linhaNum += f"{vaga.numero} {vaga.tipo_de_vaga[0]}  "

            if vaga.ocupado:
                linhaEst += f"  O      "
            else:
                linhaEst += f"  -      "

            if vaga.numero % 3 == 0:
                linhas.append(linhaNum)
                linhas.append(linhaEst)
                linhaNum = ""
                linhaEst = ""

        self.__estacionamento_view.mostrar_vagas(linhas)

    def ocupar_vaga(self):
        try:
            cpf_pessoa = self.__master_controller.pessoa_controller.get_cpf()
            pessoa = self.__master_controller.pessoa_controller.busca_morador_por_cpf(cpf_pessoa)
            num_vaga = self.__estacionamento_view.get_vaga()
            tipo_da_pessoa = self.__master_controller.pessoa_controller.get_tipo_de_pessoa(pessoa.cpf)
            for v in self.__estacionamento_dao.get_vagas():
                tv = v.tipo_de_vaga
                if tv == tipo_da_pessoa:
                    if v.numero == num_vaga:
                        if v.ocupado:
                            raise ValueError("Esta vaga já está ocupada.")
                        else:
                            self.__estacionamento_dao.ocupar_vaga(v, pessoa)
                            self.__estacionamento_view.mostra_linhas([
                                "Vaga ocupada."
                            ])
                            return
                        raise TipoVagaIncompativelException(cpf_pessoa)
            raise TipoVagaIncompativelException(cpf_pessoa)
        except ValueError as e:
            self.__estacionamento_view.mostra_linhas([
                f"\n{e}\n"
            ])
        except TipoVagaIncompativelException as e:
            self.__estacionamento_view.mostra_linhas([
                f"\n{e}\n"
            ])

    def desocupar_vaga(self):
        try:
            cpf_pessoa = self.__master_controller.pessoa_controller.get_cpf()
            num_vaga = self.__estacionamento_view.get_vaga()
            for v in self.__estacionamento_dao.get_vagas():
                if v.numero == num_vaga and cpf_pessoa == v.pessoa.cpf:
                    if v.ocupado:
                        self.__estacionamento_dao.desocupar_vaga(v)
                        self.__estacionamento_view.mostra_linhas([
                            "Vaga desocupada."
                        ])

                        return
                    else:
                        raise ValueError
            raise ValueError
        except ValueError:
            self.__estacionamento_view.mostra_linhas([
                "Essa vaga não está ocupada."
            ])

    def display_vaga(self):
        try:
            num_vaga = self.__estacionamento_view.get_vaga()
            for v in self.__estacionamento_dao.get_vagas():
                if v.numero == num_vaga:
                    if v.ocupado:
                        pessoa_to_display = v.pessoa.nome
                    else:
                        pessoa_to_display = "Ninguém"
                    self.__estacionamento_view.mostrar_vagas([
                        "------------------------------------",
                        f"Vaga {v.numero}",
                        f"Ocupado: {'sim' if v.ocupado else 'não'}",
                        f"Vaga de {v.tipo_de_vaga}",
                        f"Ocupado por {pessoa_to_display}",
                        "-------------------------------------"
                    ])
        except:
            self.__estacionamento_view.mostra_linhas([
                "Essa vaga não existe."
            ])
