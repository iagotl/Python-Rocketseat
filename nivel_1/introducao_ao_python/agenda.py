"""
📱 Agenda de Contatos - Python

Um sistema de gerenciamento de contatos desenvolvido em Python puro, 
projeto prático do curso de introdução ao Python da Rocketseat.

🚀 Funcionalidades:
- ✅ Adicionar novos contatos (nome, telefone, email)
- 👀 Visualizar lista completa de contatos
- ✏️  Editar informações de contatos existentes
- ⭐ Marcar/desmarcar contatos como favoritos
- 🌟 Visualizar apenas contatos favoritos
- 🗑️  Deletar contatos com confirmação

📋 Estrutura:
- Menu principal com 6 opções
- Validação de entrada do usuário
- Tratamento de erros e índices inválidos
- Armazenamento em memória (lista de dicionários)

🎯 Objetivo:
Demonstrar conceitos fundamentais do Python como:
- Estruturas de dados (listas, dicionários)
- Funções e documentação
- Estruturas de controle (if/else, loops)
- Tratamento de exceções
- Validação de entrada do usuário

Desenvolvido por: Iago Talamoni
Curso: Python - Rocketseat
Versão: 1.0.0
"""

# Criarmos abaixo as funções que utilizaremos ao longo do programa
def exibir_menu() -> None:
    """
    Função utilizada para exibir o menu da agenda de contatos
    
    Args:
        None
    Return:
        None
    """
    print('\nMenu da Agenda de contatos: ')
    print('1. Salvar novo contato')
    print('2. Visualizar os contatos')
    print('3. Editar um contato')
    print('4. Visualizar os contatos favoritos')
    print('5. Deletar um contato')
    print('6. Fechar a agenda')
    print() # Pula uma linha
    return

def validacao_escolha(escolha_usuario: str, etapa_verificacao: str) -> bool:
    """
    Essa função é responsável por validar se o usuário colocou uma entrada válida do menu
    Verificações:
        - Verifica se a entrada do usuário é numérica
        - Verifica se o número está dentro das opções disponíveis
    Args:
        escolha_usuario(string): Escolha do usuário
        etapa_verificacao(string): É a etapa da verificação que o usuário está
    Return:
        Booleano
    """
    escolha_usuario = escolha_usuario.strip() # Retirando espaços em branco potencialmente colocados pelo usuário
    
    if etapa_verificacao == 'menu':
        if escolha_usuario.isdigit() and escolha_usuario in ['1', '2', '3', '4', '5', '6']:
            return True
        else:
            return False
    elif etapa_verificacao == 'editar contato':
        if escolha_usuario.isdigit() and escolha_usuario in ['1', '2', '3', '4']:
            return True
        else:
            return False

def salvar_contatos(nome: str, telefone: str, email: str, favorito: bool) -> None:
    """
    Essa função é responsável por garantir que é possível salvar um novo contato na agenda

    Args:
        Nome (String): Nome do contatao
        Telefone (string): Número de telefone do contato
        Email (string): E-mail do contato
        Favorito (booleano): Indica se um contato é favorito ou não
    Return:
        None
    """
    contato = {}
    contato['nome'] = nome
    contato['telefone'] = telefone
    contato['email'] = email
    if favorito.lower() == 'sim':
        favorito_conversao = True
    else:
        favorito_conversao = False
    contato['favorito'] = favorito_conversao

    contatos.append(contato)
    return None

def exibir_contatos(contatos: list) -> None:
    """
    Essa função é responsável por exibir todos os contatos da agenda

    Args:
        contatos(list): É a lista de contatos
    Return:
        None
    """
    if len(contatos) == 0:
        print('Sua lista de contatos está vazia!')
    else:
        i = 1 # Contador para colocarmos nos  (Coloca em 1 para exibir ao usuário)
        for contato in contatos:
            print(f'{i}. Nome: {contato["nome"]}, Telefone: {contato["telefone"]}, Email: {contato["email"]}, Favorito: {contato["favorito"]}')
            i += 1

def editar_contato(contatos:list, index_contato: int, index_opcao: int) -> None:
    """
    Essa função tem como objetivo fazer edições em um contato específico, inclusive alterar se é favoreito ou não
    
    Args:
        contatos(list): É a lista de contatos
        index_contato(int): É o índice do contato que o usuário deseja alterar
        index_opcao(int): É o índice da informação que o usuário deseja editar
    Return:
        None
    """
    try:
        if index_opcao == 1:
            antigo_nome = contatos[index_contato - 1]['nome']
            novo_nome = input('Digite o novo nome do contato: ')
            contatos[index_contato - 1]['nome'] = novo_nome
            print(f'O nome foi alterado {antigo_nome} ➡️ {novo_nome}')
        elif index_opcao == 2:
            antigo_telefone = contatos[index_contato - 1]['telefone']
            novo_telefone = input('Digite o novo telefone do contato: ')
            contatos[index_contato - 1]['telefone'] = novo_telefone
            print(f'O telefone foi alterado {antigo_telefone} ➡️ {novo_telefone}')
        elif index_opcao == 3:
            antigo_email = contatos[index_contato - 1]['email']
            novo_email = input('Digite o novo e-mail do contato: ')
            contatos[index_contato - 1]['email'] = novo_email
            print(f'O e-mail foi alterado {antigo_email} ➡️ {novo_email}')
        else:
            if contatos[index_contato - 1]['favorito'] == True:
                contatos[index_contato - 1]['favorito'] = False
                print('O contato foi desmarcado como favorito')
            else:
                contatos[index_contato - 1]['favorito'] = True
                print('O contato foi marcado como favorito')
    except Exception as e:
        print(f'O índice digitado não existe na lista de contatos, vamos voltar ao menu inicial!')

def exibir_contatos_favoritos(contatos: list) -> None:
    """
    Essa função tem como objetivo exibir todos os contatos favoritos da agenda

    Args:
        contatos(list): É a lista de contatos
    Return:
        None
    """
    i = -1 # Índice do contato (Começa com -1 pois a primeira volta deve ter índice 0)
    index_contatos = [] # Lista que irá armazenar os índices dos contatos favoritos

    for contato in contatos:
      i += 1
      for info, valor in contato.items():
        if info == 'favorito' and valor == True:
            index_contatos.append(i)

    if len(index_contatos) == 0:
      print('Não existem contatos favoritos cadastrados na agenda!')
    else:
      for index in index_contatos:
        contato_dicionario = contatos[index]
        print(f'🌟 Nome: {contato_dicionario["nome"]}, Telefone: {contato_dicionario["telefone"]}, Email: {contato_dicionario["email"]}, Favorito: {contato_dicionario["favorito"]}')

def apagar_contato(contatos:list, index_contato:int) -> None:
    """
    Essa função é responsável por apagar um contato da agenda
    
    Args:
        contatos(list): É a lista de contatos
        index_contato(int): É o índice do conttao que o usuário deseja apagar
    Return:
        None
    """
    contatos.pop(index_contato)
    return None

# Programa principal

# Usaremos a lista para armazenar os contatos
contatos = []

# Iniciamos exibindo o menu
exibir_menu()

while True:
    escolha_usuario = input('Escolha uma opção do menu: ')
    if validacao_escolha(escolha_usuario, 'menu'):
        if escolha_usuario == '1':
            nome = input('Digite o nome do contato que deseja salvar:')
            telefone = input('Digite o telefone do contato que deseja salvar (Lembre de colocar o DDD):')
            email = input('Digite o e-mail do contato que deseja salvar:')
            favorito = input('Deseja marcar como favorito? (Sim / Não):')
            salvar_contatos(nome, telefone, email, favorito)
            print(f'O contato {nome} foi salvo com sucesso!')
            print(contatos)
        
        elif escolha_usuario == '2':
            print('Lista de contatos cadastrados:')
            exibir_contatos(contatos)
        
        elif escolha_usuario == '3':
            exibir_contatos(contatos)
            indice_contato = input('Digite o índice do contato que deseja alterar: ')
            print() # Espaço na saída do terminal
            # Verificando se o índice é válido
            if len(contatos) == 0:
                print('Não temos contatos para serem alterados!')
                continue

            elif len(contatos) == 1 and int(indice_contato) != 1:
                print('Índice inválido, vamos voltar ao menu inicial!')
                continue

            elif ((int(int(indice_contato)) <= 0) or (int(indice_contato) > (len(contatos) - 1)) and len(contatos) > 1):
                print('Índice inválido, vamos voltar ao menu inicial!')
                continue

            else:
                print('Qual informação deseja alterar?')
                print('1.Nome\n2.Telefone\n3.Email\n4.Favorito')
                escolha_usuario = input('Escolha a opção desejada: ')
                print() # Espaço na saída do terminal
                if validacao_escolha(escolha_usuario, 'editar contato'):
                    editar_contato(contatos, int(indice_contato), int(escolha_usuario))
                else:
                    print('Escolha inválida, vamos voltar ao menu inicial!')
                    continue

        elif escolha_usuario == '4':
            print('Exibindo sua lista de contatos favoritos...')
            exibir_contatos_favoritos(contatos)

        elif escolha_usuario == '5':
            exibir_contatos(contatos)
            indice = input('Digite o índice do contato que deseja apagar:')
            nome_contato_selecionado = contatos[int(indice) - 1]['nome']
            # Verificando se o índice é válido
            if len(contatos) == 0:
                print('Não temos contatos cadastrados para serem apagados!')
                continue
            
            elif len(contatos) == 1 and int(indice) != 1:
                print('Índice inválido, vamos voltar ao menu inicial!')
                continue
            
            elif ((int(int(indice)) <= 0) or (int(indice) > (len(contatos) - 1)) and len(contatos) > 1):
                print('Índice inválido, vamos voltar ao menu inicial!')
                continue
            else:
                confirmacao = input(f'Certeza que deseja apagar o contato {nome_contato_selecionado}? (Sim / Não): ')
                if confirmacao.lower() == 'sim':
                    apagar_contato(contatos, int(indice) - 1)
                    print('O contato foi apagado com sucesso')
                elif confirmacao.lower() == 'não':
                    print('Abortando o processo de exclusão do contato {nome_contato_selecionado}!')
                else:
                    print('Escolha inválida, vamos voltar ao menu inicial!')
                    continue
        elif escolha_usuario == '6':
            print('Finalizando o aplicativo agenda...')
            print('Até logo!')
            break
                
    else:
        print('Escolha uma opção válida!')
        continue