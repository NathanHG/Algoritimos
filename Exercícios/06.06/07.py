print('°°°°° Ex. 7 °°°°°')
numero = int(input('Digite um número não-negativo: '))
n_fatorial = 1
for x in range(2, numero + 1):
      n_fatorial = n_fatorial * x
print('{}! = {}'.format(numero, n_fatorial))
      
