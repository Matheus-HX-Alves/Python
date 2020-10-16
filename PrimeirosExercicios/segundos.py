ValorInicial = input("Por favor, entre com o número de segundos que deseja converter: ")
ValorInt = int(ValorInicial)
ValorDias = ValorInt // 86400
ValorHoras = (ValorInt % 86400) // 3600
ValorMinutos = (ValorInt % 3600) // 60
ValorSeg =  ValorInt % 60
print (F"{ValorDias} dias, {ValorHoras} horas, {ValorMinutos} minutos e {ValorSeg} segundos.")
