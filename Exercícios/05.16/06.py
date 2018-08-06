div = 1
while (div > 0):
    div = int(input('Digite um número: '))
    sao = int(input('Digite outro número: '))
    if (div < 0 or sao < 0):
        print('Algum dos números é negativo. \nFIM DA OPERAÇÃO')
        break
    elif (sao == 0):
        print('Não existe divisão por 0')
    else:
        print('O resultado da divisão é: {}'.format(div / sao))
