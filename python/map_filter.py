kmh = [36, 40, 56, 64, 73, 79, 85, 96, 100, 120]

# mh = []
# for i in kmh:
#     mh.append(i/1.61)
# print(mh)

# A mesma coisa usando map
mh2 = list(map(lambda x: (x / 1.61), kmh)) # map recebe uma função e uma variável. Nesse caso, um array.
print(mh2)


# Filter, retira do processo tudo que é falso.
lista = [1, 2, 3, 4, 5]
def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

resultado = list(filter(par, lista))
print(resultado)

print("*"*20)
#Fazendo o mesmo que fez o filter de outra forma
resultado2 = [x for x in lista if x % 2 == 0]
print(resultado2)

