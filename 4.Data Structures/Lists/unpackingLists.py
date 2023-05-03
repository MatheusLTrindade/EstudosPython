# Unpacking Lists
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável

produtos = ['arroz', 'feijão', 'laranja', 'banana','maçã']

item1, item2, *outros, item5 = produtos

print(item1)
print(item2)
print(outros)
print(item5)