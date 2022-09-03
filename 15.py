a = float(input("quanto voce ganha por hora?"))
b = float (input("horas trabalhadas no mes"))
salarioBruto = a * b
descontoINSS = salarioBruto * 0.11
descontoSindicato = salarioBruto * 0.08
descontoTotal = descontoINSS + descontoSindicato
salarioLiquido = salarioBruto - descontoTotal
print("Seu salario bruto é:", salarioBruto)
print("Foram descontados pelo INSS:", descontoINSS)
print("Foram descontados pelo Sindicato", descontoSindicato)
print("Foram descontados no total:", descontoTotal)
print("Seu salario liquido foi:", salarioLiquido)
