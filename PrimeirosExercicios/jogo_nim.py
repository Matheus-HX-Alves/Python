def computador_escolhe_jogada(n,m):
    CompRemove = 1
    while CompRemove != n:
        if (n - CompRemove) % (m+1) == 0:
            return CompRemove
        else:
            CompRemove += 1
    return CompRemove

def usuario_escolhe_jogada(n, m):
    JogadaValida = False
    
    while not JogadaValida:
        JogadorRemove = int(input('Quantas peças você ira tirar? '))
        if JogadorRemove < 1 or JogadorRemove > m:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()
        
        else:
            JogadaValida = True

    return JogadorRemove

def campeonato():
    NumeroRodada = 1
    while NumeroRodada <= 3:
        print()
        print('**** Rodada %i ****' % NumeroRodada)
        print()
        partida()
        NumeroRodada += 1
    print()
    print('Placar: Você 0 X 3 Computador')

def partida ():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    VezDoPC = False
    if n % (m + 1) == 0:
        print()
        print("Você começa!")
    else:
        print()
        print('Computador começa!')
        VezDoPC = True

    while n > 0:
        if VezDoPC:
            ComputadorRemove = computador_escolhe_jogada(n, m)
            n = n - ComputadorRemove
            if ComputadorRemove == 1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou', ComputadorRemove, 'peças')

            VezDoPC = False
        else:
            JogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - JogadorRemove
            if JogadorRemove == 1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', JogadorRemove, 'peças')
            VezDoPC = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()

    print('Fim do jogo! O computador ganhou!')

print('Bem-vindo ao jogo do NIM! Escolha:')
print()

print('1 - para jogar uma partida isolada')

tipoDePartida = int(input('2 - para jogar um campeonato '))

if tipoDePartida == 2:
    print()
    print('Voce escolheu um campeonato!')
    print()
    campeonato()
else:
    if tipoDePartida == 1:
        print()
        partida()