num1 = float(input("Digite o tamanho de um arquivo para download (em MB) "))
num2 = float(input("Digite a velocidade de um link de Internet (em Mbps) "))
R = (num1/(num2/8))

print ("o tempo aproximado de download do arquivo usando este link (em minutos) é igual a : ",R/60)