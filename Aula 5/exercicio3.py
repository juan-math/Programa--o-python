# Faça um programa para um lava rapido onde :
# 1 - Lavagem completa a R$ 50.00
# 2 - Lavagem Básica a R$ 35.00

print("Boa noite , seja bem vido ao Lava jato do Juan ")

print(" Escolhas as opções abaixo")

Lavagem = int(input('Digite 1 para Lavagem completa - R$50,00\nDigite 2 para Lavagem Básica R$35.00\n'))

Lava1 = "Lavagem completa"
Lava2 = "Lavagem básica"

if(Lavagem == 1):
    print("voce escolheu Lavagem completa ")
    valortotal = 50
elif(Lavagem == 2):
    print("Voce escolheu lavagem básica")
    valortotal = 35
extra = input(" voce gostaria de adicionar o pretinho (sim ou nao) ")
if(extra == "sim" ):
    print("voce adicionou Pretinho")
    valortotal += 5

print(f"O valor total do produtor é :{valortotal}")
