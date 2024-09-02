#  Escreva um programa que peça ao usuário para escolher um modo de transporte  (carro, bicicleta, a pé) e exiba uma mensagem com a velocidade média correspondente.

def main():
    print("Escolha um modo de transporte:")
    print("1. Carro")
    print("2. Bicicleta")
    print("3. A pé")
    
    escolha = input("Digite o número correspondente à sua escolha: ")

    match escolha:
        case "1":
            print("Você escolheu Carro. A velocidade média é de 60-100 km/h.")
        case "2":
            print("Você escolheu Bicicleta. A velocidade média é de 15-25 km/h.")
        case "3":
            print("Você escolheu A pé. A velocidade média é de 5-6 km/h.")
        case _:
            print("Opção inválida! Por favor, escolha uma das opções listadas.")

if __name__ == "__main__":
    main()
