# Faça um programa que valide se um aluno pode fazer o curso de python, onde o unico critério é  ele ter idade maior ou igual a 16 anos 
print("Óla , seja bem-vindo ao Senac")
print("Qual seu nome")
input()
print("Qual curso você deseja ?")
input()
idade = int(input("Qual sua idade"))

if(idade>=16):
    print("Sim, voce pode fazer o curso ")
else:
    print("Não , você não pode fazer o curso ")