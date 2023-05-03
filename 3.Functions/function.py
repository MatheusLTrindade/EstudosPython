# Introdução a Funções
quantity = 10

def boas_vindas(nome, produto, quantidade=quantity):
    print(f'Olá {nome}!')
    print(f'Temos {quantidade} {produto} em estoque')


name = input('Digite seu nome: ')
product = input('Digite o seu produto: ')
boas_vindas(name, product)
print()

# Print(tarefa) / Return(calculo)
def cliente1(nome):
    print(f'Olá {nome}')


def cliente2(nome):
    return f'Olá {nome}'


x = cliente1('Maria')
y = cliente2('Jose')

print(x)
print(y)
print()

# Vários argumentos (xargs)
    # Criar uma função que soma vários números
def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x = soma(2,3,4,7)
print(x)
print()


# Vários argumentos (xargs) identificando o Parametro.
    # Criar uma função que armazena números e strings (dados)
def agencia(**carro):
    return carro

print(agencia(marca='Volkswagen', modelo='Gol', cor='Branco', motor=1.0, placa=1234))
print(agencia(marca='Honda', modelo='City', cor='Cinza', motor=1.5))
print(agencia(marca='Hyunday', modelo='Elantra', cor='preto'))
print()