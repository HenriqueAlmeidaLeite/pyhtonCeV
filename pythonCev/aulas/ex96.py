def printar():
    print('\n\nControle de terrenos')
    print('-' *20)
    larg = float(input('Digite a largura do terreno em metros: \n'))
    prof = float(input('Digite a profundidade do terreno em metros: \n'))
    area = float(larg * prof)
    print(f'\nUm terreno com {larg} M de largura e {prof} M de profundidade tem uma área de {area}M² \n')

printar()
cont = bool(False)
while cont == False:
    val = str(input(('Quer calcular uma nova área?\nS = sim\nN = não\n'))).lower()
    if val == 's':
        printar()
    else:
        print('Obrigado por usar o programa!')
        cont = True