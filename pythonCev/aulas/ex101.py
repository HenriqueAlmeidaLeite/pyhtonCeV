from datetime import datetime
def voto(a):
    if (datetime.now().year - a) < 16:
        return 1
    elif (datetime.now().year - a) > 15 and (datetime.now().year - a) < 19 or (datetime.now().year - a) > 65:
        return 2
    else:
        return 3


teste = False
while teste == False:
    ano = int(input('\nEm que ano você nasceu? '))
    idade = (datetime.now().year - ano)
    if ano > datetime.now().year:
        print('\nValor inválido. Tente novamente')
    else:
        teste = True
        res = voto(ano)
        if res == 1:
            print(f'\nVocê tem {idade} anos de idade e não pode votar')
        elif res == 2:
            print(F'\nVocê tem {idade} anos de idade e só vota se você quiser')
        else: 
            print(f'\nVocê tem {idade} anos de idade e é obrigado a votar')
    
