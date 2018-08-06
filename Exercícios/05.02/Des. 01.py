o = float(4500) # Ovelhas
l = float(2) # Lã em Kilos
m = float(7.00) # Quanto o mercado paga
g = float(15)
r= float(2.41)
tl = o*l # Total de lã
tm = tl*m # Total que o mercado pagará
dg = (tm*g)/100 # Dinheiro do governo
dp = tm-dg # Dinheiro do Pastor
dr = dp*r # Dinheiro em reais
print('O pastor receberá {} reais.'.format(dr))
