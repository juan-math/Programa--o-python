#Faça um programa que pergunte quantas rodas tem um veiculo, se tiver 4 diga é um carro ou van 
# Quando temos masi de uma condicional , usamos o "elif"    sintaxe
# "if" 1° Condicional 
# "elif" Dmais condicões condicional 

carro = int(input("Quantas rodas tem um veiculo ?"))

if(carro==4):
    print("Sim, é um carro ou uma van ")
elif(carro==2):
    print("Não ,não é um carro ou uma van , e sim uma moto ")
elif(carro==6):
    print("Não ,não é um carro ou uma van , e sim um ônibus ")
elif(carro>= 8 and carro <=20):
    print("Não , Provavlemente é um caminhão ")

else:
    print("Não foi econtrado um veiculo correspondenteao numeros de rodas ")

