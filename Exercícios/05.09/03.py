print('-----Execício 3-----')
divisor = int(input('Informe um número, para um divisor: '))
dividendo = int(input('Informe outro número, para o dividendo: '))
if dividendo > 0:
    div = int(divisor/dividendo)
    print('O quociente de {} por {} é {}.'.format(divisor, dividendo, div))
elif dividendo <= 0:
    print('É impossivel fazer essa operção.')
