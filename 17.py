a = float(input("Area em metros quadrados a serem pintados"))
b = (a / 6) * 0.10
litrosNecessarios = (a / 6) + b
resposta = input("Qual seria sua opçao de compra? A)apenas latas de 18L B)apenas latas de 3,6L C) LAtas misturadas")
if (resposta == "a"):
    latas = litrosNecessarios // 18
    precoTotal = latas * 80
    print ("Latas Necessarias", latas)
    print ("total a pagar", precoTotal)
elif(resposta == "b"):
     latas = litrosNecessarios // 3.6 
     precoTotal = latas * 25
     print("total a pagar", precoTotal)
     print("total de latas", latas)
else:
    latasg = litrosNecessarios // 18
    resto = litrosNecessarios % 18
    latasp = resto // 3.6
    precoTotal = latasg * 80 + latasp * 25
    print ("Latas de 18L:", latasg)
    print ("latas de 3,6L ", latasp)
    print ("preço total", precoTotal)

