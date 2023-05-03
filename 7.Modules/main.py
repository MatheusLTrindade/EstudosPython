# Importa tudo que contem no modulo
    # import funcoes 

# Importa somente a função 'somar()' e 'multi()'
    # from funcoes import somar, multi

# Importa modulo dentro de packages
    # from items.cadastro import client

from funcoes import find_index

list1 = ['a', 'b', 'c', 'd', 'e']

var1 = find_index(list1, 'b')

print(var1)
