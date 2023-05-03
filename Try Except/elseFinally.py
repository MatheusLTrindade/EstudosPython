# Try Except
    # Excelente para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizdas quando encontra um erro

# Else
try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números')
else:
    print('Usuário digitou um valor correto')
    resultado = valor * 2
    print(resultado)
print()

# Finally
try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números')
finally:
    print('Código OK')
print()