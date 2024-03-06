import time 
def maioral(num):
    maior = 0
    menor = 0
    tam = len(num)

    maior = num[0]
    menor = num[0]   

    for ele in num:
        if ele > maior:
            maior = ele
        if ele < menor:
            menor = ele
    print('\nAnalisando os valores passados...\n')
    for elem in num:
        print(elem, end = ' ', flush = True)
        time.sleep(0.5)
    print(f'\n\nForam registrados {tam} números')
    print(f'\nO maior número digitado foi {maior} e o menor foi {menor}')

nume = 0
teste = False
lista = []
te = False

while te == False:
    while teste == False:
        
        soma = int(input('\nDigite um número inteiro: '))
        test = int(input('\nQuer adicionar mais algum número?\n1 = sim\n2 = não\n'))
        
        if test > 2 or test < 1:
            print('Valor invalido. Tente novamente.')
        else:
            lista.append(soma)
            if test == 2:
                maioral(lista)
                teste = True

    tes = int(input('\nQuer fazer um novo teste numérico?\n1 = sim\n2 = não\n'))
    if tes == 2:
        print('\n+Obrigado por usar meu programa!')
        te = True
    else:
        lista.clear()
        teste = False



