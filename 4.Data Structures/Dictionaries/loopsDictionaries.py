# Loops Dictionaries
    # Utiliza index no formato keys e Values
    # Aceita string, integer, float, boolean...

aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

for keys in aluno:
    print(keys)
print()

for values in aluno.values():
    print(values)
print()

for itens in aluno.items(): # Retorna Tubles
    print(itens)
print()

for keys, values in aluno.items():
    print(keys, values)