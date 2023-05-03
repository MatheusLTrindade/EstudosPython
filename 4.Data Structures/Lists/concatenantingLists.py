# Lists
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável

numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

final = numeros + letras
print(final)

numeros.extend(letras)
print(numeros)
print()

itens = [['item1', 'item2'], ['item3', 'item4']]
print(itens[0][1])
print(itens[1][1])