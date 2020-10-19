def VerificaNumeros(N1,N2):
    if N1 > N2:
        print(N1)
    elif N2 > N1:
        print(N2)
    else:
        print('São iguais.')

N1 = int(input('Digite um numero: '))
N2 = int(input('Digite outro numero: '))
VerificaNumeros(N1,N2)
