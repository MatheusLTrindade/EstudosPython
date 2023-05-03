# Desafio com If, Elif, Else

'''
Criar um programa que dependendo da temperatura (em celsius) 
do steak ele retorna ponto de cozimento em portugues. 
O usuário deverá fornecer a temperatura.

Temperaturas - Cozimento
120°F ou 48°C - Rare (Selada)
130°F ou 54°C - Medium rare (Ao ponto para mal)
140°F ou 60°C - Medium (Ao ponto)
150°F ou 65°C - Medium well (Ao ponto para bem)
160°F ou 71°C - Well done (Bem passada)
'''

print('Challenge 1\n')

active = True

while active:
    print(
        '1.Testar temperatura\n'
        '0.Sair\n'
    )
    option = int(input('Selecione uma opção: '))

    if option == 1:
        temp = int(input('\nQual a temperatura da carne? '))

        if temp < 48:
            print('Cozinhar por mais alguns minutos\n')
        elif 48 <= temp < 54:
            print('Selada\n')
        elif 54 <= temp < 60:
            print('Ao ponto para mal\n')
        elif temp == 60:
            print('Ao ponto\n')
        elif 60 < temp <= 65 :
            print('Ao ponto para bem\n')
        elif 65 < temp <= 71:
            print('Bem passada\n')
        else:
            print('Queimou\n')
    elif option == 0:
        print('Programa finalizado!')
        active = False
    else:
        print('Opção inválida!\nTente Novamente.\n')
