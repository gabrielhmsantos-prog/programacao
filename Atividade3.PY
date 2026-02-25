#Atividade sobre pães e broas
conta = float
total = float
paes = float(input("Insira o número de paes"))
broas = float(input("Insira o número de broas"))
paes = paes * 0.12
broas = broas * 1.50
total = paes + broas
print("O total no dia é: ",total)
conta = total * 0.1
print("O Total que vai ser direcionado a sua conta é: ",conta)