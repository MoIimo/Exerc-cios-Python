peso = float(input("qual o quilo de pescado de hoje?"))
if (peso > 50):
    excesso = peso - 50
    multa = excesso * 4
    print("Multa a ser paga:", multa)
else:
    print ("nenhuma multa a pagar")    