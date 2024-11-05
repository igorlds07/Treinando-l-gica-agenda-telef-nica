Agenda de Contatos
Este é um programa simples em Python para gerenciar uma lista de contatos, onde o usuário pode adicionar, editar, visualizar e excluir contatos.

Funcionalidades
O programa possui um menu interativo que oferece as seguintes opções:

Exibir um contato: Permite que o usuário consulte um contato específico, fornecendo o nome do contato. Caso o contato não exista, o sistema irá informar ao usuário.
Adicionar um novo contato: O usuário pode adicionar um novo contato fornecendo o nome e número do telefone. O sistema irá verificar se o número já está registrado na lista e, se for o caso, não permitirá a adição.
Editar um contato existente: O usuário pode editar os dados de um contato já existente, alterando o nome e/ou o número de telefone. Se o contato não for encontrado, o sistema irá avisar o usuário.
Encerrar o programa: Permite que o usuário saia do programa.
Estrutura do Código
O código utiliza um dicionário (contatos) para armazenar os contatos, onde as chaves são os nomes dos contatos e os valores são os números de telefone.

Como funciona:
O programa exibe um menu interativo com as opções de visualização, adição, edição ou encerramento.
O usuário escolhe uma opção e o programa executa a ação correspondente.
O programa continua executando até que o usuário escolha a opção de encerrar o programa.
Código:
python
Copiar código
# Listas para adicionar os contatos
contatos = {}
nome_contato = 0
número_contato = 0

# Laço para o menu de interação
while True:
    # Pequeno menu para saber qual a interação do usuário
    print('-='*25)
    print('Menu de interação do usuário:')
    print('-=' * 25)
    ver_lista_e_numero = int(input(' [1] Exibir algum contato \n'
                                   ' [2] Adicionar um novo contato\n '
                                   '[3] Editar algum contato   \n '
                                   '[4] Encerrar programa      \n'
                                   '       '))

    # Condição para exibir o contato que o usuário deseja ver
    if ver_lista_e_numero == 1:
        visualizar = str(input('Qual contato você deseja visualizar? ')).title()
        print('_'*50)

        if visualizar not in contatos.keys():
            print('Este contato não existe na lista!')
        else:
            print(f'O número selecionado é: {contatos[visualizar]}')

    # Condição para o usuário adicionar um novo contato à lista
    if ver_lista_e_numero == 2:
        número_contato = int(input('Novo número: '))
        nome_contato = str(input('Nome : ')).title()

        # Se as variáveis forem preenchidas, são adicionados ao dicionário
        contatos[nome_contato] = número_contato

        # Condição para ver se o contato já existe na lista
        if número_contato not in contatos.values():
            print('Contato já existente!')
        else:
            pass

    # Condição para o usuário editar algum contato já existente na lista
    if ver_lista_e_numero == 3:
        editar = str(input('Qual contato você deseja editar? ')).title()
        if editar not in contatos.keys():
            print('Este contato não está na lista !')
        else:
            contatos.pop(editar)
            nome_contato = str(input('Nome : ')).title()
            número_contato = int(input('Novo número: '))
            contatos[nome_contato] = número_contato
            print(f'Contato {nome_contato} atualizado com sucesso!')

    # Condição para encerrar o programa
    if ver_lista_e_numero == 4:
        break

print('PROGRAMA ENCERRADO !')
Como Usar
Execute o script Python.
O programa exibirá um menu de interação com as opções:
Exibir um contato
Adicionar um novo contato
Editar um contato existente
Encerrar o programa
Escolha a opção desejada digitando o número correspondente.
Siga as instruções fornecidas pelo programa para realizar cada ação.
O programa continuará rodando até que você escolha a opção de encerrar.
