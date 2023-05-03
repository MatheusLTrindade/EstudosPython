# Try Except
    # Excelente para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizdas quando encontra um erro

try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Index não existe')
print()

# Em Inputs
try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números')
print()