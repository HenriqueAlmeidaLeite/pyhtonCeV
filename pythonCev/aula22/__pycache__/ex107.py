from ex107 import moeda

val = float(input('\n\nDigite o valor que você quer manipular: '))

e = moeda.aumentar(val)
print(f'\nO valor que foi digitado aumentado é {e}')

f = moeda.diminuir(val)
print(f'\nO valor que foi digitado diminuído é {f}')

g = moeda.dobro(val)
print(f'\nO valor que foi digitado dobrado é {g}')

h = moeda.metade(val)
print(f'\nO valor que foi digitado dividido pela metade é {h} ')