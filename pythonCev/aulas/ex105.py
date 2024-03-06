def notas(*num, sit = None):
    
    """
    Calcula a média, a maior, e a menor nota da turma.
    Opcionalmente passa a situação da turma.
    """

    dic = {
        "Maior" : None,
        "Menor" : None,
        "Média" : None,
        "Total" : None,  
    }

    mai = 0
    men = float('inf')
    tot = 0
    cont = 0

    for n in num:
        if n > mai:
            mai = n
        if n < men:
            men = n
        tot += n
        cont += 1
    
    med = tot/cont

    if sit is not None:
        if med < 6:
            sit = "Ruim"
        elif med >= 6 and med <8:
            sit = "Mais ou menos"
        else:
            sit = "Boa"

        dic ["Situação"] = sit
    
    dic["Maior"] = mai
    dic["Menor"] = men
    dic ["Média"] = med
    dic["Total"] = tot

    return dic

resp = notas(9.3, 8.2, 3.5, 5.6, 9.4, 7.8, sit = True)
print ('\n\n', resp, '\n\n')
