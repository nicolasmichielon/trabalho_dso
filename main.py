from master_controller import MasterController

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
    print("7: Visualizar todas as ocorrências")
    print("8: Cadastrar gasto")
    print("9: Visualizar todos os gastos")
    print("10: Visualizar gasto por morador")
    print("===========================================")
    try:
        entrada = int(input("Escolha: "))
    except:
        print("Entrada inválida!")
        continue
    if entrada == 0:
        exit()
    elif entrada == 1:
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
    elif entrada == 7:
        master_controller.ocorrencia_controller.busca_ocorrencias()
    elif entrada == 8:
        master_controller.gasto_controller.adicionar_gasto()
    elif entrada == 9:
        master_controller.gasto_controller.listar_gastos()
    elif entrada == 10:
        master_controller.gasto_controller.listar_gasto_por_cpf()
    else: 
        print("Entrada inválida!")
