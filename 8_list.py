# LISTLAR BILAN ISHLASH:
# meva = ['banan', 'ananas', 'anor', 'uzum', 'olma', 'kakos', 'mango']
# print(meva[1:6])
# print(meva[:5])

# sort()
# meva.sort()
# print(meva)


# meva.sort(reverse=True)
# print(meva)


# sorted()
# sinf = ['zulayho', 'muhammadali', 'abdulloh', 'jahongir', 'habib']
# print(sorted(sinf))

# print(sorted(sinf, reverse=True))

# numbers = [48,4885,2,6,84,48,484,9,4,23,1,15,45,4,542]

# print(numbers)
# numbers.sort()
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))


# meva = ['banan', 'ananas', 'anor', 'uzum', 'olma', 'kakos', 'mango']
# meva.reverse()
# print(meva)


# numbers = [48,4885,2,6,84,48,484,9,4,23,1,15,45,4,542]
# numbers.reverse()
# print(numbers)


# LIST UZUNLIGINI TOPISH:
# length (uzunlik) - len

# len()
# meva = ['banan', 'ananas', 'anor', 'uzum', 'olma', 'kakos', 'mango']
# print(len(meva))

# sabzavotlar = ['sabzi', 'gosht', 'sut', 'kartoshka', 'piyoz', 'karam']
# mening_royxatim = []
# mening_royxatim.append(sabzavotlar[2])
# mening_royxatim.extend(sabzavotlar[1])
# print(mening_royxatim)


# ism = ['habib', 'jahongir']
# ismlar = ism
# print(ism)
# print(id(ism))
# print(id(ismlar))

# ism = ismlar[:]
# print(id(ism))
# print(id(ismlar))



# range(,,)
# number = list(range(1, 10+1))
# number = list(range(1, 11))
# print(number)


# juf_tsonlar = list(range(0, 21, 2))
# toq_sonlar = list(range(1, 21+1, 2))
# print(juf_tsonlar)
# print(toq_sonlar)



# max(), min() va sum()

# sonlar = list(range(1, 10))
# print(sonlar)
# print(max(sonlar)) # Eng katta qiymatni olib beradi
# print(min(sonlar)) # Eng kichik qiymatni olib beradi
# print(sum(sonlar)) # Berilgan qiymatlarni qo'shib beradi
