quantidade1 = float(input("Digite a quantidade de moedas de 1"))
quantidade2 = float(input("Digite a quantidade de moedas de 5"))
quantidade3 = float(input("Digite a quantidade de moedas de 10"))
quantidade4 = float(input("Digite a quantidade de moedas de 25"))
quantidade5 = float(input("Digite a quantidade de moedas de 50"))

g1 = 1 * quantidade1
g2 = 5 * quantidade2
g3 = 10 * quantidade3
g4 = 25 * quantidade4
g5 = 50 * quantidade5

soma = (g1 + g2) + (g3 + g4) + g5
print("O valor total em moedas é: ",soma)
