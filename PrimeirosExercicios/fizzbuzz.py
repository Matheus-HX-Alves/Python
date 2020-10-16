NumDiv = int(input("Digite um número: "))
if (NumDiv % 3) == 0:
    print ("FizzBuzz")
else:
    if (NumDiv % 5) == 0:
        print ("FizzBuzz")
    else:
        print (NumDiv)