import velha_funcoes as jv

jogador = 'X'
vencedor = False

while vencedor == False:
    jv.desenhar_tabuleiro()

    jogada = int(input('Onde deseja jogar?'))

    jv.jogar(jogada, jogador)

    jv.desenhar_tabuleiro()
    jv.troca_jogador(jogador)

    jv.verifica_vitoria()
    vencedor = jv.troca_jogador()

print(f'O jogador "{jogador}" venceu!')