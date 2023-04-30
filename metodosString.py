mensagem = ' eu amo carro JDM'
# index.    0123456789...

print(mensagem)

# Tudo em minúscula 
print(f'\n {mensagem.lower()}')

# Tudo em maiúscula 
print(f'\n {mensagem.upper()}')

# Letra maiúscula no começo
print(f'\n {mensagem.capitalize()}')

# Procura a posição de inicio da letra/palavra no index
print(f'\n {mensagem.find("m")}')
print(f'\n {mensagem.find("M")}')
print(f'\n {mensagem.find("carro")}')

# Procura a letra/palavra antiga e altera para a nova
print(f'\n {mensagem.replace("a", "e")}')
print(f'\n {mensagem.replace("JDM", "Japonês")}')

# Retira os espaços do início
print(f'\n {mensagem.strip()}')