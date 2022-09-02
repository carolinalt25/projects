#Autor: Ana Carolina Lopes Teixeira
#Santiago, 02 de abril de 2022
#criar uma calculadora em Python

print("********************** Python Calculator ********************** ")

def soma (x,y):
    return x + y

def subtração (x,y):
    return x - y

def multiplica (x,y):
    return x * y

def divisão (x,y):
    return x / y

def raiz (x):
    return x * x

print("\n Escolha a operação matemática desejada: ")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Raiz Quadrada")

Operação = int(input("\nDigite qual a operação desejada (1/2/3/4/5): "))
if Operação == 5:
    num3 = int(input("Insira o número que deseja saber a raiz quadrada: "))

else:

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

if Operação == 1:
    print("\nResultado:",num1,"+",num2, "=",soma(num1,num2))
    print("\n")

elif Operação == 2:
    print("\nResultado:",num1, "-", num2, "=", subtração(num1, num2))
    print("\n")

elif Operação ==3:
    print("\nResultado:",num1, "*", num2, "=", multiplica(num1, num2))
    print("\n")

elif Operação == 4:
    print("\nResultado:",num1, "/", num2, "=", divisão(num1, num2))
    print("\n")

elif Operação == 5:
    print("\nResultado: A raiz quadrada de ", num3, "=", raiz(num3))
    print("\n")

else:
    print("\nOpção inválida")