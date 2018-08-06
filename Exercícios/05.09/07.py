print('-----Exercício 7-----')
gasto = float(input('Qual foi o gasto na loja? '))
if gasto <= 100 :
    d5 = float(((gasto * 5 / 100) - gasto) * (-1))
    print('Você pagará {}.'.format(d5))
elif gasto >100 and gasto < 200 :
   d10 = float(((gasto * 10 / 100) - gasto) * (-1))
   print('Você pagará {}.'.format(d10))
elif gasto > 200 :
    d20 = float(((gasto * 20 / 100) - gasto) * (-1))
    print('Você pagará {}.'.format(d20))
