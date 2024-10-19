from master_controller import MasterController
from ocorrencia_controller import OcorrenciaController
from pessoa_controller import PessoaController




master_controller = MasterController()

entrada = None
while entrada != 0:
    print("================== MENU ==================")
    print("1: Adicionar Morador")
    print("2: Adicionar Sindico")
    print("3: Criar Ocorrencia")
    print("4: Buscar Ocorrencia por CPF de morador")
    print("5: Visualizar todos os moradores")
    print("6: Visualizar sindico")
    print("===========================================")
    try:
        entrada = int(input("Escolha: "))
        if entrada == 1:
            master_controller.pessoa_controller.adicionar_morador()
        elif entrada == 2:
            master_controller.pessoa_controller.adicionar_sindico()
        elif entrada == 3:
            master_controller.ocorrencia_controller.adicionar_ocorrencia()
        elif entrada == 4:
            master_controller.ocorrencia_controller.busca_ocorrencias_por_cpf_de_morador()
        elif entrada == 5:
            master_controller.pessoa_controller.display_moradores()
        elif entrada == 6:
            master_controller.pessoa_controller.display_sindico()
        else: 
            raise Exception
    except:
        print("Opção inválida! Digite uma das opções do menu.")
