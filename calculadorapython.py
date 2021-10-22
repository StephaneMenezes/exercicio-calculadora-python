import math

print('*'*11, "Bem-vindo a calculadora Python",'*'*11)
def adicionar(x,y):
    return x + y 
def subtrair(x,y):
    return x - y 
def multiplicar(x,y):
    return x * y 
def dividir(x,y):
    return x / y 
def raiz(x,y):
    return math.sqrt(x), math.sqrt(y)

print(" Escolha a função que deseja utilizar: ")
print("1 - Soma ")
print("2 - Subtração ")
print("3 - Multiplicação ")
print("4 - Divisão ")
print("5 - Raíz quadrada")
escolha = input("Digite a operação que deseja executar: ")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if escolha == "1": 
    print(num1, "+", num2, "=", adicionar(num1,num2))
elif escolha == "2": 
    print(num1,"-", num2, "=", subtrair(num1,num2))
elif escolha == "3": 
    print(num1,"*", num2, "=", multiplicar(num1,num2))
elif escolha == "4": 
    (num1,"/", num2, "=", dividir(num1,num2))
elif escolha == "5":
    print("Raiz quadrada de: ", num1, "e", num2, "é: ", raiz(num1,num2))
else: 
    print("Opção inválida, por favor escolha uma operação válida. ")

print("Obrigada por calcular comigo!")
