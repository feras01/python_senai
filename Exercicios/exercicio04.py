# Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.


# cor = input('Digite uma cor (vermelho, verde, azul): ').lower()

# if cor == 'vermelho':
#     print('Você escolheu a cor vermelha')
# elif cor == 'verde':
#     print('Você escolheu a cor verde')
# elif cor == "azul":
#     print("Você escolheu a cor azul!")
# else:
#     print('Cor invalida! Por favor digite: vermelho, verde ou azul')




cor = input("Digite uma cor (vermelho, verde, azul): ").lower()


if cor == "vermelho":
    print("Você escolheu a cor vermelha!")
elif cor == "verde":
    print("Você escolheu a cor verde!")
elif cor == "azul":
    print("Você escolheu a cor azul!")
else:
    print("Cor inválida! Por favor, digite vermelho, verde ou azul.")
