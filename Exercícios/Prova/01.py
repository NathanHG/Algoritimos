print('-----Exercício 1-----')
base = int(input('Digite um número: '))
expo = int(input('Digite outro número: ')) #Expoente
r = base
while (expo > 1):
    r = r * base
    expo = expo - 1
print('Resposta: {}'.format(r))
