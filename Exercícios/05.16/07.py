x = 1
y = 1
mul = 0
while (x <= 10):
    while (y <= 10):
        mul = x * y
        print('{}x{}={}'.format(x, y, mul))
        y = y + 1
    x = x + 1
    y = 1
    print('\n')
