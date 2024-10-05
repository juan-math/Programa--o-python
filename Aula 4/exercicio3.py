# Faça um programa que calculee o IMC do usuário e de a classificação conforme a tabala 
print("óla, boa noite")
altura=float(input("Qual sua altura"))
peso= float(input("Qual seu  peso "))
imc = peso / (altura * altura)
print(f"o seu imc é {imc} ")
if(imc < 18.5):
    print(" Magreza")
    print("0")
    print('Você precisa engordar ')
elif(imc >= 18.5 and imc <=24.9 ):
    print("Normal")
    print("0")
    print('Você está ótimo ')
elif(imc>=25 and imc<=29.9 ):
    print("Sobrepeso")   
    print("1")
    print('Você está acima do peso ') 
elif(imc>=30 and imc<=39.9 ):
    print("Obesidade")  
    print("2") 
    print(" você está muito acima do peso ")
elif(imc>=40 ):
    print("Obesidade Grave")  
    print("2") 
    print("Você esta muito acima do peso") 


else:
    print("Vamos malhar seu merda")