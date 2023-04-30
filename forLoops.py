# Imprimir de 0 a 5
for numero in range(6):
    print(numero)

print()

# Imprimir de 1 a 10
for numero in range(1, 11):
    print(numero, end='')

print()

# Imprimir letra por letra
palavra = 'Honda'
for letra in palavra:
    print(f'{letra} está dentro da palavra {palavra}')

print()

# For Loops - Utilizando If e Else
compra_confirmada = True
valor_compra = 12.50
dados_compra = f'Compra no valor de R${valor_compra} e entrega confirmada.'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviado para o seu e-mail')
        break
    else:
        print('Falha na compra')

print()

# For Loops - Nested loops
    # Outer loop
     # Inner loop
for numero1 in range(1,6):
    print(f'Produto {numero1}')
    for numero2 in range(11):
        print(numero1, numero2)

print()

# For Loops - Separando Strings
    # Modificar de FANTASTICO para F A N T A S T I C O
palavra = 'FANTASTICO'

for spaco in palavra:
    print(f'{spaco} ', end='')

print()

'''
For Loops - Criando um retangulo de 6x6
    @@@@@@
    @@@@@@
    @@@@@@
    @@@@@@
    @@@@@@
    @@@@@@
'''
linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()

