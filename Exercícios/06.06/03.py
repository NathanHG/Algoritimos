num = int(input('Digite um número,para saber sua tabuada: '))
x = 1
for x in range (1, 11):
    print('{} x {} = {}'.format(x, num, num * x))
