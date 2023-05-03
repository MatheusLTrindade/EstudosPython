# Lambda In Function
    # É uma função (pequena) sem nome
    # Pode ter vários argumentos mas somente 1 expressão
    # Muito utilizada dentro dde outras funções
    # Código mais 'clean'

def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4

print(somar(2))