print("-=" * 30)
print("        BEM-VINDOS A EMPRESA DO LUAN FERREIRA LIMA")
print("-=" * 30)
lista_funcionarios = list()
id_global = 4758415


def cadastrar_funcionario(id):
    # Pergunta e já armazena os dados no dicionário.
    funcionario = dict()
    print(f"Id: {id}")
    funcionario['id'] = id
    funcionario['nome'] = str(input("Por favor entre com o nome do funcionário: ")).upper()
    funcionario['setor'] = str(input("Por favor entre com o setor do funcionário: ")).upper()
    funcionario['salario'] = float(input("Por favor entre com o salário do funcionário: "))
    # Copia o dicionário para a lista.
    lista_funcionarios.append(funcionario.copy())


def consultar_funcionarios():
    while True:
        print("_______________MENU CONSULTAR FUNCIONÁRIO_______________")
        print("""Escolha a opção desejada:
1.Consultar Todos os Funcionários
2.Consultar Funcionários por Id
3.Consultar Funcionário(s) por Setor 
4.Retornar ao menu""")
        try:
            opcao = int(input(">>"))
            print("-=" * 30)
            if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
                print('Opção inválida.')
        except ValueError:
            print("Digite somente números inteiros.")
        else:
            # Consulta todos os funcionários e lista por ordem de cadastramento.
            if opcao == 1:
                print("Lista com todos os funcionários:")
                for pessoa in lista_funcionarios:
                    print(f"ID: {pessoa['id']}\nNOME: {pessoa['nome']}")
                    print(f"SETOR: {pessoa['setor']}\nSALÁRIO: {pessoa['salario']}")
                    print()
                print("-=" * 30)

            # Consulta por ID uma única pessoa.
            elif opcao == 2:
                id_encontrado = False
                id_opcao2 = int(input("Digite o id do funcionário: "))
                for index, pessoa in enumerate(lista_funcionarios):
                    if id_opcao2 == pessoa['id']:
                        print(f"ID: {pessoa['id']}\nNOME: {pessoa['nome']}")
                        print(f"SETOR: {pessoa['setor']}\nSALÁRIO: {pessoa['salario']}")
                        print()
                        print("-=" * 30)
                        id_encontrado = True
                        break
                if not id_encontrado:
                    print(f"Funcionário com Id: {id_opcao2} não encontrado.")

            # Consulta todas as pessoas do setor
            elif opcao == 3:
                setor_encontrado = False
                setor_opcao3 = str(input("Digite o seu setor do(s) funcionário(s): ")).upper()
                for index, pessoa in enumerate(lista_funcionarios):
                    if setor_opcao3 in pessoa['setor']:
                        print(f"ID: {pessoa['id']}\nNOME: {pessoa['nome']}")
                        print(f"SETOR: {pessoa['setor']}\nSALÁRIO: {pessoa['salario']}")
                        print()
                        setor_encontrado = True
                    print("-=" * 30)
                if not setor_encontrado:
                    print(f"Funcionário no setor de: {setor_opcao3} não encontrado.")

            # Retorna ao menu principal
            elif opcao == 4:
                return


def remover_funcionario():
    id_remover = False
    id_funcionario = int(input("Digite o ID do funcionário a ser removido: "))
    # Procura o ID digitado e remove da lista.
    for pessoa in lista_funcionarios:
        if id_funcionario == pessoa['id']:
            lista_funcionarios.remove(pessoa)
            print(f"Funcionário com Id {id_funcionario} removido com sucesso.")
            id_remover = True
    if not id_remover:
        print(f"Id inválido. Funcionário não existe no sistema.")


# Código principal que chama todas as funções de acordo com a opção.
while True:
    try:
        print("_______________MENU PRINCIPAL_______________")
        print("""1 - Cadastrar Funcionário
2 - Consultar Funcionário
3 - Remover Funcionário
4 - Encerrar programa""")
        print("-=" * 30)
        opcao = int(input(">>"))
        print("-=" * 30)
        if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
            print('Opção inválida.')
    except ValueError:
        print("Digite somente números inteiros.")
    else:
        if opcao == 1:
            id_global += 1
            cadastrar_funcionario(id_global)
        elif opcao == 2:
            consultar_funcionarios()
        elif opcao == 3:
            remover_funcionario()
        elif opcao == 4:
            print("Encerrando o sistema...")
            break
