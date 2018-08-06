a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
soma = 0
for x in range (a, b + 1):
    if (x % 2 == 0):
        print('O número {} é par.'.format(x))
    else:
        print('O nímero {} é impar, portanto entra na soma. '.format(x))
        soma = soma + x
print('A soma dos número impares é {}'.format(soma))
