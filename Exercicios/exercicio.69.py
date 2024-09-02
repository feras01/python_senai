def inicializar_tabuleiro():
    return [[' ' for _ in range(3)] for _ in range(3)]

def imprimir_tabuleiro(tabuleiro):
    print("\n")
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 5)
    print("\n")

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas, colunas e diagonais
    linhas = [tabuleiro[i] for i in range(3)]
    colunas = [[tabuleiro[i][j] for i in range(3)] for j in range(3)]
    diagonais = [[tabuleiro[i][i] for i in range(3)], [tabuleiro[i][2-i] for i in range(3)]]
    
    for conjunto in linhas + colunas + diagonais:
        if all([celula == jogador for celula in conjunto]):
            return True
    return False

def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if ' ' in linha:
            return False
    return True

def solicitar_posicao(tabuleiro, jogador):
    while True:
        try:
            linha = int(input(f"Jogador {jogador}, digite a linha (1, 2 ou 3): ")) - 1
            coluna = int(input(f"Jogador {jogador}, digite a coluna (1, 2 ou 3): ")) - 1
            
            if tabuleiro[linha][coluna] != ' ':
                print("Posição já ocupada! Tente novamente.")
            else:
                return linha, coluna
        except (ValueError, IndexError):
            print("Entrada inválida! Tente novamente.")

def jogar():
    tabuleiro = inicializar_tabuleiro()
    jogador_atual = 'X'
    
    while True:
        imprimir_tabuleiro(tabuleiro)
        
        linha, coluna = solicitar_posicao(tabuleiro, jogador_atual)
        tabuleiro[linha][coluna] = jogador_atual
        
        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns, jogador {jogador_atual}! Você venceu!")
            break
        
        if verificar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break
        
        # Alterna o jogador
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

def main():
    while True:
        jogar()
        nova_partida = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if nova_partida != 's':
            print("Obrigado por jogar! Até a próxima.")
            break

if __name__ == "__main__":
    main()
