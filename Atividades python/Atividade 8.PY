#Insira a altura de uma pessoa e o sexo desta pessoa(M ou F)
#M peso ideal (72.7*h) - 58
#F peso ideal (62.1*h) - 44.7

sexo = (input("Digite seu sexo")) 
altura = float (input("Digite a altura da pessoa: "))
if sexo == "M":
    peso = (72.7*altura) - 58
    print("Seu peso ideal é: ",peso)
if sexo == "F":
     peso = (62.1*altura) - 44.7
     print("Seu peso ideal é: ",peso)


     
