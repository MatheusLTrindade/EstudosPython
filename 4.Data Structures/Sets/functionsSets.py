# Functions Sets (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

list1= [1, 2, 3, 4, 5, 6]
s1 = {1, 2, 3, 4, 5, 6}

print(type(list1))
print(type(s1))
print()

s1.add(7)
s1.update([2, 7, 8, 9, 10])
s1.remove(10)
s1.discard(9) # descarta um número mesmo que ainda não esteja no Set

print(s1)
