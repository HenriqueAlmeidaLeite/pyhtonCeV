import time
def contador(a, b, c):
    """
    Testa quais são os maiores números
    """
    print('\n')
    print('Contagem de 1 até 10 de 1 em 1:')
    for i in range(1, 11, 1):
        print(i, end = ' ', flush = True)
        time.sleep(0.5)
    
    print('\n')

    print('Contagem de 10 até 0 de 2 em dois:')
    for l in range (10, -1, -2):
        print(l, end = ' ', flush = True) 
        time.sleep(0.5) 
   
    print('\n')  

    if b < a:
        print(f'Contagem de {b} até {a} de {c} em {c}:')
        for d in range(a, b-1, -c):
            print(d, end = ' ', flush = True)
            time.sleep(0.5)

    else:
        print(f'Contagem de {a} até {b} de {c} em {c}:')
        for g in range(a, b+1, c):
            print(g, end=' ', flush = True)
            time.sleep(0.5)
help(contador)
ini = int(input('\n\nDigite o número em que a contagem vai se iniciar: '))
fim = int(input('\nDigite o número em que a contagem vai terminar: '))
pas = int(input('\nDigite o número do passo: '))
contador(ini, fim, pas)
