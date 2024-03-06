def ficha(a ="misterioso", b = 0):
    print(f'\nO jogador {a} marcou {b} gols')

nome = str(input('\nDigite o nome do jogador: '))
gols = str(input('\nDigite quantos gols esse jogador fez: '))

if gols.isnumeric():
    gols = int(gols)

else:
    gols = 0

ficha(nome, gols)
