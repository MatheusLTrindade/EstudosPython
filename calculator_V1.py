'''
Autor: Matheus
Data:29/04/2023
Versão: 1.0
'''
# Soma
def add(x,y):
    return x + y

# Subtração
def subtract(x, y):
    return x - y

# Multiplicação
def multiply(x, y):
    return x * y

# Divisão
def divide(x, y):
    return x / y

print("CALCULADORA")
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

select = True

while select:

    print("\nSelecione a operação")
    print("1.Somar")
    print("2.Subtrair")
    print("3.Multiplicar")
    print("4.Dividir")
    print("0.Sair\n")

    def option_1():
        print(f'O resultado de {x} + {y} é igual a {add(x,y)}')
    def option_2():
        print(f'O resultado de {x} - {y} é igual a {subtract(x,y)}')
    def option_3():
        print(f'O resultado de {x} X {y} é igual a {multiply(x,y)}')
    def option_4():
        print(f'O resultado de {x} / {y} é igual a {divide(x,y)}')
    def option_0():
        global select
        select = False

    options = {
        1: option_1,
        2: option_2,
        3: option_3,
        4: option_4,
        0: option_0,
    }

    option = int(input())

    if option in options:
        options[option]()
    else:
        print("\nOpção inválida!")
