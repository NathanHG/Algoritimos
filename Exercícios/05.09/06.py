print('-----Execício 6-----')
a = int(input('Digite um número: '))
b = int(input('Digite um novo número: '))
c = int(input('Digite outro número: '))
delta = (b) ** 2 - 4 *  a * c 
if delta < 0:
    print('Não existe raiz real!')
elif delta == 0:
    x = (-b) / (2 * a)
    print('Existe uma raiz real, que é {}.'.format(x))
elif delta > 0 :
    x1 = (- b + delta**(0.5)) / (2 * a)
    x2 = (- b - delta**(0.5)) / (2 * a)
    print('x1= {} e x2= {}'.format(x1, x2))
