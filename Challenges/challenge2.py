# Desafio com Funções

'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede.
O usuário deverá fornecer as seguintes informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tintas'.
'''

rendimento = float(input('Qual é o rendimento da lata em m²? '))
altura = float(input('Qual é a altura da parede em metros? '))
largura = float(input('Qual é a largura da parede em metros? '))

def calculo_tinta():
    area = altura * largura
    total = area / rendimento
    print(f'Você necessita de {total} latas de tinta.')

calculo_tinta()