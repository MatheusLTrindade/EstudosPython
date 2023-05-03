# Set (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

list1= [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

# Union = junta as listas sem duplicar os itens
print(num1 | num2)

# Difference = retira os itens que se repetem nas listas sem junta-las
print(num1 - num2)

# Symmetric Difference = junta as listas somente com os itens que não se repetem
print(num1 ^ num2)

# And = Mostra somente com os itens duplicados
print(num1 & num2)

# Mostra a quantidade de itens da lista
print(len(num1))

print()

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2)
set5 = set1.difference(set3)
set6 = set1.intersection(set2)
set7 = set1.symmetric_difference(set3)

print(set4)
print(set5)
print(set6)
print(set7)

