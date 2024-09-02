def classificar_nota(nota):
    match nota:
        case 0 | 1 | 2 | 3:
            return "Baixa"
        case 4 | 5 | 6 | 7:
            return "Média"
        case 8 | 9 | 10:
            return "Alta"
        case _:
            return "Nota inválida"

def main():
    try:
        nota = int(input("Digite uma nota de 0 a 10: "))
        if 0 <= nota <= 10:
            classificacao = classificar_nota(nota)
            print(f"A nota {nota} é classificada como: {classificacao}")
        else:
            print("Nota fora do intervalo permitido!")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()
