# ona  - mother
# mother - ona
# mashina = {'nomi': 'Mercedes', 'model': input("Modeli: "), 'yili': 2024}
# print(mashina)

# print(mashina['nomi'])


# students = {'ism': 'Muhammadali',
#             'familiya': 'Abdullohov',
#             'yoshi': 20,
#             'tyil': 2000}

# print(f"{students['ism']} {students['familiya']} {students['yoshi']} yoshdaman.")
    #   f"{students['familiya']}. "
    #   f"{students['yoshi']} yoshdaman. "
    #   f"{students['tyil']}.")



# key: value - kalit: qiymat


# car = {
#     'nomi': 'Mercedes',
#     'model': 'X7 Drive',
#     'color': 'oq',
#     'yili': 2024
# }
# print(car)


# car['engine'] = 'automatic'
# car['price'] = 55_000
# # print(car)
# car['engine'] = 'mechanical'
# print(car)
# print(len(car))


car = {'ism': 'Alimjon', 'familiya': 'Alimjonov', 'tyil': 1998}
# print(car['ism'])
print(len(car))



# del car['nomi']
# print(car)


sweet = car.get('narx', "Bunday key mavjud emas")
print(sweet)
print(car.get('price'))


# phones = {
#     'muhammadali': 'iphone 16',
#     'abdulloh': 'iphone 15 pro max',
#     'jahongir': 'iphone 15',
#     'rahmatulla': 'redmagic', 
#     'galaxy': 'S24 Ultra',
#     'rahmatilla': 'iphone 15'
# }

# for kalit, qiymat in phones.items():
#     print(kalit, qiymat)


# for i in phones.keys():
# for i in phones:
#     print(i)

# for i in phones.values():
#     print(i)


# smartphones = {
#     'iphone 15': 1_500,
#     'iphone 14': 1_300,
#     'iphone 15': 1_000,
#     'galaxy': 1_200,
#     'redmi': 1_500
# }

# telefonlar = ['iphone 15', 'redmi', 'galaxy']

# for i in smartphones:
#     if i in telefonlar:
#         print(f"{i} --  {smartphones[i]}")

# for i in sorted(smartphones.values(), reverse=True):
#     print(i)