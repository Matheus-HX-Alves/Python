Paes = 0
PrecoPao = 0.0
print("Panificadora Pão de Ontem - Tabela de preços")
for TabelaPaes in range(50):
    Paes += 1
    PrecoPao += 0.18
    print(f"{Paes} - R${round(PrecoPao, 2)}")