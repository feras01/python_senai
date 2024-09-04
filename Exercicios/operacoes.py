import email


nomes = []


def menu():
    opcao = ['Cadastrar none', 'Atualizar nome', 'Excluir nome', 'Lista nomes']

    for indice ,opcao in enumerate(opcao):
        print(f'{indice +1} - {opcao}')

def lista_nomes():
    for indice ,nome in enumerate(nomes):
            print(f'{indice} - {nome}')

def cadastrar_nome(nome, email, data_nascimento, matricula):

    aluno = {
    'nome': nome, 
    'email': email, 
    'data_nascimento':data_nascimento,
    'data_nascimento'
    'matricula': matricula}
    }

    nomes.append(nome)

def atualiza_nome(nome, novo_nome):
    nomes[nomes.index(nome)] = novo_nome

def excluir_nome(nome):
    nomes.remove(nome)