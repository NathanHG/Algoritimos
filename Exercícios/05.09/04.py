print('-----Execício 4-----')
idade = int(input('Digite sua idade: '))
if idade <16:
    print('Você não pode votar!')
    print('Volte quando for maior de 16.')
elif idade == 16 or idade == 17:
    print('Seu voto é facultativo')
    print('Vote!')
elif idade <= 65:
    print('Seu voto é obrigatório!')
    print('VOTE !!!')
else :
    print('Você esta dispensado do voto.')
    print('Vá para casa.')
