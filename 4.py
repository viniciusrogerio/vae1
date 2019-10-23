def media(lista):
    resultado=0
    for i in lista:
        resultado=resultado+i
    resultado=resultado/5
    return resultado

def variancia(lista):
    resultado=0
    for x in lista:
        resultado=resultado+(x-media(lista))**2
    resultado=resultado/5
    return resultado

def desv_padrao(lista):
    return(variancia(lista))**0.5

def mediana(lista):
    return lista[2]
