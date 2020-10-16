n = int(input('Digite um número inteiro: '))


#def n_primos(n)

y = n - 1
o = None

while n > 1:

    while y <= n :
        o = n % y

        if y == 1 and o != 0: 
            print('primo')
            contador =+ 1

        else:
            y -= 1

    n -= 1

print(contador)




#pl=preco/lucro
#p/pv