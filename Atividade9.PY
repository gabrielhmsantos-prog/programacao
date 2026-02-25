#Atividade com escolha de tamanho de
escolha = int(input("Digite quantas camisas você quer(P,M,G): "))
camisaP= 0 
camisaM= 0 
camisaG= 0 
for i in range(escolha):
    tamanho = (input("Digite o tamanho da camisa"))
    tamanho.upper() 
    if tamanho == "P":
        camisaP += 1
        print ("Quantidade de camisa", camisaP)
    if tamanho == "M":
        camisaM += 1
        print ("Quantidade de camisa", camisaM)
    if tamanho == "G":
        camisaG += 1
        print ("Quantidade de camisa", camisaG)

 
G = camisaG * 15
M = camisaM * 12
P = camisaP * 10

soma = P + M + G

print("O valor total é: ",soma)











   