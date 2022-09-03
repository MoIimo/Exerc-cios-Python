a = float(input("metros quadrados da area a ser pintada"))
litrosNecessarios = a / 3
if (litrosNecessarios > 18 ):
    latas = int(litrosNecessarios / 18)
    precoTotal = latas * 80
    print ("Latas Necessarias", latas)
    print ("total a pagar", precoTotal)
else :
    print ("Será necessario apenas 1 Lata, saindo a 80 reais")