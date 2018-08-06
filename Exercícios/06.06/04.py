num = int(input('Digite um número: '))
div = 0
quo = 1
for quo in range (1, num + 1):
    if (num % quo == 0):
        div = div + 1
    quo = quo + 1
if (div == 2):
    print ('{}, é um número primo'.format(num))
else:
    print('{}, não é um número primo'.format(num))
  
