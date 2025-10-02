"""
Gerenciador de Lista de Tarefas - Projeto Prático das aulas doMódulo 1

Este programa é um sistema de gerenciamento de tarefas interativo que permite ao usuário:
- Adicionar novas tarefas à lista
- Visualizar todas as tarefas com status de conclusão
- Atualizar o nome de tarefas existentes
- Marcar tarefas como completadas
- Deletar tarefas que foram completadas
- Sair do programa

O programa utiliza um menu interativo onde o usuário pode selecionar opções numeradas
de 1 a 6. As tarefas são armazenadas em uma lista de dicionários, onde cada tarefa
possui um nome e um status de conclusão (True/False).

Funcionalidades:
1. Adicionar tarefa - Cria uma nova tarefa com status "não completada"
2. Verificar Tarefas - Exibe todas as tarefas com indicadores visuais de status
3. Atualizar Tarefa - Modifica o nome de uma tarefa existente
4. Completar Tarefa - Marca uma tarefa como concluída
5. Deletar Tarefas Completadas - Remove todas as tarefas já concluídas
6. Sair - Encerra o programa

O programa roda em loop contínuo até que o usuário escolha a opção de sair.
"""

print("\nMenu do Gerenciador de Lista de Tarefas:")
print("1. Adicionar tarefa")
print("2. Verificar Tarefas")
print("3. Atualizar Tarefa")
print("4. Completar Tarefa")
print("5. Deletar Tarefas Completadas")
print("6. Sair")

# Funções que utilizaremos no programa
def adicionar_tarefa(tarefa, lista_tarefas) -> None:
    """
    Adiciona uma tarefa na nossa lista de tarefas
    Args:
        tarefa(str): A tarefa que desejamos adicionar
        lista_tarefas(list): A lista que armazena as tarefas
    Return:
        None
    """
    tarefa_dict = {"Tarefa": tarefa, "Completada": False}
    lista_tarefas = lista_tarefas.append(tarefa_dict)
    print(f'A Tarefa "{tarefa}" foi adicionada com sucesso!')
    print() # Pula uma linha
    return

def verificar_tarefas(lista_tarefas) -> None:
    """
    Visualizar as tarefas
    Args:
        lista_tarefas(list): Lista que armazena as tarefas
    Return:
        None
    """
    for indice, tarefa in enumerate(lista_tarefas, start=1):
        status = '✅' if tarefa['Completada'] == True else '❌'
        print(f'\n{indice}. [{status}] {tarefa["Tarefa"]} ')
        print('--------------------------------------------') # Separação visual entre as tarefas

def atualizar_tarefas(lista_tarefas, indice_tarefa, novo_nome) -> None:
    """
    Atualiza o nome de uma tarefa
    Args:
        lista_tarefas(list): Lista que armazena as tarefas
        indice_tarefa(int): Índice da tarefa para o usuário
        novo_nome(str): Novo nome da tarefa
    Return:
        None
    """
    tarefa_inicial = lista_tarefas[indice_tarefa - 1]["Tarefa"]
    lista_tarefas[indice_tarefa - 1]["Tarefa"] = novo_nome 
    print(f'Tarefa {indice_tarefa} atualizada com sucesso ("{tarefa_inicial}"➡️  "{novo_nome}")')

def completar_tarefas(lista_tarefas, indice_tarefa):
    """
    Permite ao usuário completar uma tarefa específica
    Args:
        lista_tarefas(list): Lista que armazena as tarefas
        indice_tarefas(int): Índice da tarefa para o usuário
    Return:
        None
    """
    tarefa_completada_nome = lista_tarefas[indice_tarefa - 1]['Tarefa']
    lista_tarefas[indice_tarefa - 1]['Completada'] = True
    print(f'Tarefa {tarefa_completada_nome} marcada como completada!')
    return

def deletar_tarefas_completas(lista_tarefas):
    """
    Permite ao usuário deletar todas as tarefas que foram completadas
    Args:
        lista_tarefas(list): Lista que armazena as tarefas
        indice_tarefas(int): Índice da tarefa para o usuário
    Return:
        None
    """
    for tarefa in lista_tarefas:
        if tarefa['Completada'] == True:
            lista_tarefas.remove(tarefa)
        else:
            pass
    print('As tarefas completadas foram deletadas!')
    return


# Lista em que vamos armazenar as tarefas
lista_tarefas = []

while True:
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        nome_tarefa = input('Digite o nome da tarefa que deseja adicionar: ')
        adicionar_tarefa(nome_tarefa, lista_tarefas)

    elif escolha == '2':
        verificar_tarefas(lista_tarefas)

    elif escolha == '3':
        indice_tarefa = int(input('Digite o índice da tarefa que deseja atualizar: '))
        novo_nome_tarefa = input('Digite o novo nome da tarefa: ')
        atualizar_tarefas(lista_tarefas, indice_tarefa, novo_nome_tarefa)

    elif escolha == '4':
        verificar_tarefas(lista_tarefas)
        indice_tarefa = int(input('Digite o número da tarefa que deseja completar: '))
        completar_tarefas(lista_tarefas, indice_tarefa)

    elif escolha == '5':
        deletar_tarefas_completas(lista_tarefas)
        verificar_tarefas(lista_tarefas)

    elif escolha == '6':
        break
        