
nomes = ['Luciano', 'Flavio', 'Adrina']

operacao = 'sim'

while operacao == 'sim':
    print('1 Cadastre Nome')
    print('2 Atualize Nome')
    print('3 Exlua Nome')
    print('4 Listar Nomes')
    opcao = int(input('Informe a ação desejada: '))


match opcao:
    case 1:
        nome = input('que nome deseja cadastrar: ')
        nomes.append(nome)
    case 2:
        nome = input('que nome deseja atualizar')
        novo_nome = input('Qual será o novo nome?')
        
        nomes[nomes.index(nome)] = novo_nome
    case 3:
       nome = input('Que nome deseja resolver:')
       nome.remove(nome) 
    case 4:
        for indice ,nome in enumerate(nomes):
            print(f'{indice} - {nome}')
    case _:
        print('opção invalida')

operacao = input('Deseja realizar outra operação? ').lower()

if operacao != 'nao':
    'break'