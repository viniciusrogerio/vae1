def somalista(lista):
    lista_inicial=lista.copy()
    lista_final=[]
    soma=0
    
    for i in range(0,10):
        if i==0:
            lista_final.append(lista_inicial[0])
        else:
            for j in range(0,i):
                soma=soma+lista_final[j]
            lista_final.append(lista_inicial[i]+soma)
            soma=0
    return lista_final
