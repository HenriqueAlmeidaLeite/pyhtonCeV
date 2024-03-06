def leiaInt():
    tes = False
    while tes == False:
        try:
            num = int(input('\nDigite um número inteiro: '))
        except:
            print('\nValor inválido, tente novamente.')
        else:
            tes = True
            return num
def leiaFloat():
    while True:
        try:
            nu = float(input('\nDigite um número real: '))
        except:
            print('\nValor inválido, tente novamente.')
        else:
            test = True
            return nu
        
inte = leiaInt()
floa = leiaFloat()

print(f'\n\nO valor inteiro digitado foi {inte} e o valor real foi {floa}')
