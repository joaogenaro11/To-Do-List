tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa adicionada.")
    else:
        print("\nLista de Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

def remover_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa para remover: ")) - 1
        if 0 <= indice < len(tarefas):
            removida = tarefas.pop(indice)
            print(f"Tarefa '{removida}' removida!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")

while True:
    print("\nMenu:\n1. Adicionar Tarefa\n2. Listar Tarefas\n3. Remover Tarefa\n4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        break
    else:
        print("Opção inválida!")