import math

a = float(input("Qual o numero 1: "))
b = float(input("Qual o numero 2: "))
c = float(input("Qual o numero 3: "))
Delta = b**2-(4*a*c)
if Delta == 0:
    x = (-b + math.sqrt(Delta))/(2*a) 
    print("a raiz desta equação é", x)
else:
    if Delta < 0:
        print ("esta equação não possui raízes reais") 
    else: 
        x = (-b + math.sqrt(Delta))/(2*a) 
        y = (-b - math.sqrt(Delta))/(2*a) 
        if x < y:
            print ("as raízes da equação são", x ," e ", y)
        else: 
            print ("as raízes da equação são", y ,"e", x)