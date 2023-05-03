# List Comprehension
    # Mais simples de se escrever
    # Utilizado quando você precisa criar uma nova lista a partir de uma existente
    # [expressao for item in itens]


# Com Strings

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
    # frutas2 = []
    # for iten in frutas1:
    #     if 'n' in iten:
    #         frutas2.append(iten)
frutas2 = [iten for iten in frutas1 if 'n' in iten]
print(frutas2)
print()


# Com Integer

    # valores = []
    # for x in range(1, 6):
    #     valores.append(x * 10)
valores = [x * 10 for x in range(1,6)]
print(valores)
