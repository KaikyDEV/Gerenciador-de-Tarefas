from metodos import GerenciadorDeTarefas

gerenciador = GerenciadorDeTarefas()

nome = input('Qual o seu nome? ')

menu = f'''\nOlá {nome}. Como irá organizar o seu dia hoje?

[1] - Aplicar tarefa
[2] - Remover tarefa
[3] - Modificar tarefa
[4] - Mostrar lista de tarefas
[5] - Sair

'''

while True:
    opcao = int(input(menu))

    if opcao == 1:
        tarefa = input("Aplique a Tarefa: ")
        gerenciador.aplicar_tarefa(tarefa)

    elif opcao == 2:
        tarefa = input("Tarefa á ser removida")
        gerenciador.remover_tarefa(tarefa)

    elif opcao == 3:
        tarefa_antiga = input("Digite a tarefa a ser modificada: ")
        tarefa_nova = input("Digite a tarefa nova: ")
        gerenciador.modificar_tarefa(tarefa_antiga, tarefa_nova)

    elif opcao == 4:
        gerenciador.mostrar_tarefas();

    elif opcao == 5:
        print(f'{nome}, obrigado por usar o programa.')
        break
    else:
        print("Opção inválida!")