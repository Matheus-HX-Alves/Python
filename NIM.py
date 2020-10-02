def IniciaGame():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    opcao = int(input("2 - para jogar um campeonato "))
    if opcao == 1: 
        Modo(1)
        return "Voce escolheu uma partida isolada."
    elif opcao == 2:
        Modo(2)
        return "Voce escolheu um campeonato!"

def Modo (Escolha):
    if Escolha == 1:
        Partida()
    elif Escolha == 2:
        for x in range(3):
            Rodada += 1
            print("**** Rodada %i ****" % Rodada)
            Partida ()

def Partida ():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m + 1):
        ("Você começa!")


Computador começa!

O computador tirou uma peça.
Agora restam 2 peças no tabuleiro.

Quantas peças você vai tirar? 2

Oops! Jogada inválida! Tente de novo.

Quantas peças você vai tirar? 1

Você tirou uma peça.
Agora resta apenas uma peça no tabuleiro.

O computador tirou uma peça.
Fim do jogo! O computador ganhou!

**** Rodada 2 ****

Quantas peças? 3
Limite de peças por jogada? 2

Voce começa!

Quantas peças você vai tirar? 2 
Voce tirou 2 peças.
Agora resta apenas uma peça no tabuleiro.

O computador tirou uma peça.
Fim do jogo! O computador ganhou!

**** Rodada 3 ****

Quantas peças? 4
Limite de peças por jogada? 3

Voce começa!

Quantas peças você vai tirar? 2
Voce tirou 2 peças.
Agora restam 2 peças no tabuleiro.

O computador tirou 2 peças.
Fim do jogo! O computador ganhou!

**** Final do campeonato! ****

Placar: Você 0 X 3 Computador