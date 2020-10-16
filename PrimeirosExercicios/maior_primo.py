
def maior_primo(x):
    for num in reversed(range(1,x+1)):
        if all(num%i!=0 for i in range(2,num)):
            return num
