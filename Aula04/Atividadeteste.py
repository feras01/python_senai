
import math #Vamos precisar de math
a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
c = int(input("Digite um valor para C: "))

delta = b*b - 4 * a * c

if delta < 0:
    print("A equação não possui raizes reais.")
elif delta == 0:
    raiz = (-1*b + math.sqrt(delta))/(2 * a)
    print("A equacao possui apenas uma raiz que e ",raiz)
elif delta > 0:
    raiz1 =(-1*b + math.sqrt(delta))/(2 * a)
    raiz2 =(-1*b + math.sqrt(delta))/(2 * a)
    print("As raizes da equacao sao ",raiz1, "e",raiz2)
    