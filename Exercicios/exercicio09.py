# Crie um algoritmo que verifique se um número inserido pelo usuário é par ou ímpar.
 
def verificar_par_ou_impar():
    numero = int(input('digite um numero:'))

    if numero % 2 == 0:
        print(f'O numero {numero} e par')
    else:
        print(f'O numero {numero} é impar')

verificar_par_ou_impar()