from os import system
import operacoes as op
# from operacoes import menu , lista_nomes
# import operacoes

operacao = 'sim'

while operacao == 'sim':
    op.menu()
    opcao = int(input('Informe a ação desejada: '))

    match opcao:
        case 1:
            nome = input('que nome deseja cadastrar: ')
            email = input('Qual e o mail do aluno:')
            data_nascimento = input('Informe a data de nascimento do aluno:')
            op.cadastrar_nome(nome)
        case 2:
            nome = input('que nome deseja atualizar')
            novo_nome = input('Qual será o novo nome?')
            
            op.atualiza_nome(nome,novo_nome )
        case 3:
            nome = input('Que nome deseja resolver:')
            op.excluir_nome(nome)

        case 4:
            op.listar_nomes()
        case _:
            print('opção invalida')

    operacao = input('Deseja realizar outra operação? ').lower()
    system('clear')

    if operacao != 'sim':
        break