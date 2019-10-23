# ->>> QUESTÃO FEITA INCORRETAMENTE. NÃO ESTÁ EM CONFORMIDADE COM O ENUNCIADO.

def imprime_multiplos(n,i,j):
    if i <=0 or j<=0:
        return 'i e j inválidos!'
    else:
        multiplos_ambos=[]
        multiplos_i=[]
        multiplos_j=[]
        multiplos_final=[]
        for x in range (1,n+1):
            multiplos_i.append(i*x)
            multiplos_j.append(j*x)
        for y in multiplos_i:
            multiplos_ambos.append(y)
        for z in multiplos_i:
            if z not in multiplos_ambos:
                multiplos_final.append(z)
        for w in multiplos_j:
            if w not in multiplos_ambos:
                multiplos_final.append(w)
        multiplos_final.sort()
        print(multiplos_final)
        
