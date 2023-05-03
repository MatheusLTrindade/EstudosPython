# Lists
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiânia']
# INDEX          0                1           2           3
 
#  Altera item
cidades[0] = 'Brasilia'

# Adiciona item ao final
cidades.append('Santa Catarina')

# Remove item
cidades.remove('Salvador')

# Insere item na posição escolhida
cidades.insert(1,'Fortaleza')

# Retira item na posição escolhida
cidades.pop(0)

# Organizar em ordem alfabética
cidades.sort()

print(cidades)
