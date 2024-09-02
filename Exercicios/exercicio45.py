def main():
    numeros = []

    print("Por favor, insira 5 números:")

    for i in range(5):
        while True:
            try:
                numero = float(input(f"Digite o número {i+1}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Entrada inválida! Por favor, insira um número.")

    maior_numero = max(numeros)
    print(f'O maior número inserido foi': {maior_numero})