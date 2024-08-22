# Faça um programa que solicite ao usuário dois números e verifique se ambos são pares.


numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Ambos os numeros são pares.")
else:
    print("Pelo menos um dos numeros não e par.")