nome=input('Digite o nome do produto: ')
preco=float(input('Digite o preço: '))
qtd=int(input('Digite a quantidade: '))

if qtd>0 and qtd<=10:
    #comentários indicam a forma como fizemos, que está incorreta
    #desconto=1.02
    desconto=0.98
elif qtd>=11 and qtd<=20:
    #desconto=1.07
    desconto=0.93
elif qtd>=21 and qtd<=50:
    #desconto=1.15
    desconto=0.85
elif qtd>50:
    #desconto=1.25
    desconto=0.75
else:
    print('Quantidade inválida!')
    
preco_final=round(preco*qtd*desconto,2)
print('Produto: ',nome)
print('Valor total a ser pago: R$ ',preco_final)
