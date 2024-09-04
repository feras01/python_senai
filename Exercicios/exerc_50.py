numero = int(input('Informe o numero: '))

# while numero >= 1:
#     print(numero, end=' ')
#     numero -=1


for i in range(numero, 0, -1):
    print(i, end='')

texto1 = 'Flavio Marques'

def saudacao():    
    print(f'Olá {texto1} - esse texto veio da função')
    global  texto2
    texto2 = 'Tia Fran'
    print(f'Olá {texto2} - esse texto veio da função')

saudacao()
print(f'Ola {texto1} - esse texto veio de fora da função')
print(f'Ola {texto2} - esse texto veio de fora da função')
