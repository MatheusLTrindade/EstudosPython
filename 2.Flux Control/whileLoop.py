# Aplicar desconto de 5 reais ao produto a cada dia, mas sem exceder o valor minimo
valor = float(50)
dia = 1
while valor > 20:
    print(f'No dia {dia} o produto vai ser vendido por R${valor}')
    dia += 1
    valor -= 5

print()

# Publicar um produto com comissão de 10% se for acima de R$20,00
valor = float(input('Digite o valor do seu produto em reais: '))

while valor > 20:
    valor += (valor * 0.10)
    print(f'O valor final do seu produto será de R${valor}')
    break