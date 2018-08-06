print("Exercício Extra 07")
nc = 0
nb = 0
x = 0
sc = 0
sb = 0
for x in range(1, 11, 1):
    nc = nc + 1
    nb = nc * nc
    sc = sc + nc
    sb = sb + nb
    print("{}/{}".format(nc, nb))
print("A soma é {}/{}.".format(sc, sb))
