# Listas para adicionar os contatos
contatos = {}
nome_contato = 0
número_contato = 0

# Laço para o menu de interação
while True:
# Pequeno menu para saber se qual a  interação do usuário
    print('-='*25)
    print('Menu de interação do usuário:')
    print('-=' * 25)
    ver_lista_e_numero = int(input(' [1] Exibir algum contato \n'
                                   ' [2] Adicionar um novo contato\n '
                                   '[3] Editar algum contato   \n '
                                   '[4] Encerrar programa      \n'
                                   '       '))
# Condição para exibir o contato que usúario deseja ver
    if ver_lista_e_numero == 1:
        visualizar = str(input('Qual contato você deseja visualizar? ')).title()
        print('_'*50)

        if visualizar not in contatos.keys():
            print('Este contato não existe na lista!')


        else:
            print(f'O número selecionado é: {contatos[visualizar]}')

# Condição para o usuário adicinar um novo contato a lista

    if ver_lista_e_numero == 2:
        número_contato = int(input('Novo número: '))

        nome_contato = str(input('Nome : ')).title()

# Se as variáveis forem preenchidas, são adicionados ao dicionário
        contatos[nome_contato] = número_contato
# Pequena condição para ver se o contato já existe na lista

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
