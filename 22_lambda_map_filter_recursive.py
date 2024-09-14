# lambda argument: ifoda


# def daraja(a, b):
#     return a ** b
# daraja(2, 3)


# daraja = lambda a, b : a ** b
# print(daraja(int(input("A: ")), int(input("B: "))))


# def daraja(n):
#     return lambda x : x ** n

# kvadrat = daraja(2)
# kubi = daraja(3)

# print(f"2-ning kvadarati: {kvadrat(2)}")
# print(f"3-ning kubi: {kubi(3)}")


# map() va filter()

# from math import sqrt
# numbers = list(range(11))
# ildizlar = list(map(sqrt, numbers))
# print(ildizlar)


# a, b = int(input("A: ")), int(input("B: "))
# a, b = map(int, input(">>> ").split())
# print(a + b)
# print(a ** b)



# number = list(range(11))

# def daraja(n):
#     '''Darajaga ko'tarib beruvchi function'''
#     return n * n

# print(list(map(daraja, number)))


# numbers = list(range(11))
# kv = list(map(lambda a: a*a, numbers))
# print(kv)


# numbers = list(range(11))
# kvadratlar = []
# for i in numbers:
#     # kvadratlar.append(i*i)
#     kvadratlar.append(i ** 2)
# print(kvadratlar)



# bir = [1,2,3]
# ikki = [4,5,6]
# uch = list(map(lambda i, o : i + o, bir, ikki))
# print(uch)


# names = ['muhammadali', 'jaxongir', 'abdulloh', 'raxmatulla']
# print(list(map(lambda i: i.upper(), names)))




# filter()
# import random as r

# sonlar = r.sample(range(100), 10)
# def juft(x):
#     return x % 2 == 0

# juft_sonlar = list(filter(juft, sonlar))
# print(sonlar)
# print(juft_sonlar)



# ismlar = ['muhammadali', 'jaxongir', 'abdulloh', 'raxmatulla', 'abu bakir']
# ism = list(filter(lambda x: x.startswith('ab'),ismlar))
# print(ism)



# ismlar = ['muhammadali', 'jaxongir', 'abdulloh', 'raxmatulla', 'abu bakir']
# name = list(filter(lambda x: len(x) <= 9, ismlar))
# print(name)


# recursive
def teskari(son):
    if son == 0:
        return
    print(son, end=" ")
    teskari(son-1)

def togri(son):
    if son == 0:
        return
    togri(son-1)
    print(son, end=" ")


teskari(5)
print()
togri(5)





