import random
import time
números = []
def sorteio():
    print('\nOs números sorteados foram: ')    
    for a in range(5):
        b = random.randint(1,10)
        print(b, end=' ', flush=True)
        números.append(b)
        time.sleep(0.5)

def somaPar():
    soma = 0
    print('\n\nOs números pares sorteados foram: ')
    for c in números:
        if c % 2 == 0:
            print(c, end=' ', flush=True)
            time.sleep(0.5)
            soma += c
    if soma == 0:
        print('Nenhum')

    print(f'\n\nA soma dos números pares digitados é {soma}\n')

sorteio()
somaPar()