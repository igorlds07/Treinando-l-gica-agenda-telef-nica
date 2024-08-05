#Agenda de contatos
#Desenvolva um programa que permita ao usuário adicionar,\n
#visualizar e editar contatos em uma agenda virtual.
contatos = []
número = []
número_contato = int(input('Novo número: '))
if número_contato > 13 :
    print('\033[31mERROR. Número de caracter excedido! Digite novamente. ')
    número_contato = int(input('\033[0mNovo número: '))
nome_contato = str(input('Nome : ')).title()
número.append(número_contato)
contatos.append(nome_contato)
ver_lista_e_numero = int(input('Você deseja ver o contato ou edita-lo?\n '
                               '[1] Exibir \n'
                               ' [2] Não exibir\n '
                               '[3] Editar '))
if ver_lista_e_numero == 1:
    número.append(número_contato)
    contatos.append(nome_contato)
    print(contatos[0])
    print(número[0])
elif ver_lista_e_numero == 2:
    número.append(número_contato)
    contatos.append(nome_contato)
elif ver_lista_e_numero == 3:
    edit_contato = int(input('Edite o número:'))
    número.append(edit_contato)
    print(contatos[-1],'\n', número[-1])
novo = int(input('Deseja adicionar um novo contato? \n'
                           '[1] Sim \n'
                           '[2] Não '))

while novo == 1:
    número_contato = int(input('Novo número:'))
    if número_contato > 13:
        print('\033[31mERROR. Número de caracter excedido! Digite novamente. ')
        número_contato = int(input('\033[0mNovo número: '))
    nome_contato = str(input('Nome :')).title()
    ver_lista_e_numero = int(input('Você deseja ver o contato adicinado ou edit-lo?'
                                   '[1] Exibir \n '
                                   '[2] Não exibir\n  '
                                   '[3] Editar  '))
    if ver_lista_e_numero == 1:
        número.append(número_contato)
        contatos.append(nome_contato)
        print(contatos[-1])
        print(número[-1])
    elif ver_lista_e_numero == 2:
        número.append(número_contato)
        contatos.append(nome_contato)
        novo = int(input('Deseja adicionar um novo contato? \n'
                           '[1] Exibir'
                           ' [2] Não exibir '))
    elif ver_lista_e_numero == 3:
        edit_contato = int(input('Edite o número:'))
        número.append(edit_contato)
if novo == 2:
  print('PROGRAMA ENCERRADO')



