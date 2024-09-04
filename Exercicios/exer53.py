from os import system
import time # importar da biblioteca
numero = int(input('Informe o numero: '))

while numero >= 1:
    system('clear')
    print(numero)
    numero -= 1
    time.sleep(1)
