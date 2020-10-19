def VerificaNumero(Lista, numeroTentaiva):
    if numeroTentaiva in Lista:
        print(True)
    else:
        print(False)

Lista = []

while len(Lista) < 10:
    x = int(input("Escreva um numero para a lista: "))
    Lista.append(x)
numeroTentaiva = int(input("Digite o numero para consultar na lista: "))
VerificaNumero(Lista, numeroTentaiva)



