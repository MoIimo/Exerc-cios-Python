b = float(input("qual sua altura?"))
a = input("voce é homem? s/n")
if (a == "s"):
   c = (b * 72.7) - 58
   print ("seu peso ideal é", c)
else:
   c = (b * 62.1) - 44.7
   print("seu peso ideal é", c)

