def aumentar(a):   
    per = int(input('\nVocê quer aumentar quantos porcento do valor digitado?'))
    div = (a/100)*per
    res = a + div
    return res 

def diminuir(b):
    per = int(input('\nVocê quer diminuir quantos porcento do valor digitado?'))
    div = (b/100)*per
    res = b - div
    return res

def dobro(c):
    res = c *2
    return res

def metade(d):
    res = d/2
    return res
