n1 = 0
n2 = 1
r = 0
print(n1)
while (r <= 8):
    r = n1 + n2
    n2 = n1
    n1 = r
    print(r)
