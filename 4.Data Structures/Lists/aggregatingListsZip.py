# Aggregating Lists
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável

var = list('comprar')
print(var)

cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]

duas_listas = zip(cores, valores)

print(list(duas_listas))