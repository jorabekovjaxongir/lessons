# RollceRoyce = []
# for i in range(20):
#     newCar = {
#         'made': 'Rollse Royce',
#         'model': "Phantom",
#         'color': None,
#         'year': None,
#         'price': None,
#         'engine': None,
#         'km': None,
#     }
#     RollceRoyce.append(newCar)
# # print(RollceRoyce)


# for i in RollceRoyce[:3]:
#     i['color'] = 'silver'
#     i['year'] = 2000
#     i['price'] = 650_000
#     i['engine'] = 'automatic'

# for i in RollceRoyce[3:6]:
#     i['color'] = 'blue'
#     i['year'] = 2024
#     i['made'] = 'Bentley'
#     i['model'] = 'Mulsan'
#     i['price'] = 550_000
#     i['engine'] = 'mechanic'

# for i in RollceRoyce:
#     if i['engine'] == 'automatic':
#         i['price'] = 800_000
#     elif i['engine'] == 'mechanic':
#         i['price'] = 700_000
#     else:
#         i['price'] = 500_000

# for i in RollceRoyce:
#     print(i.values())




# developers = {
#     'muhammadali': ('python', 'java', 'c#'),
#     'abdulloh': ('python', 'java'),
#     'jahongir': ('javascript', 'html', 'css', 'typescript', 'react', 'nodejs'),
#     'rahmatulla1': ('python', 'c++'),
#     'alimojon': ('java',),
#     'rahmatulla2': ('mojo', 'python')
# }
# for names, languages in developers.items():
#     print(f"\n{names.capitalize()}:", end=" ")
#     for i in languages:
#         if i == languages[-1]:
#             print(f"{i.upper()}", end=".")
#         else:
#             print(f"{i.upper()}", end=", ")


talabalar = {
    'muhammadali': {
        'familiya': 'abdullohov',
        'ism': 'muhammadali',
        'tyil': 2005,
        'tillar': ['python', 'java', 'c#']
    },
    'jahongir': {
        'familiya': 'alimjonov',
        'ism': 'jahongir',
        'tyil': 2002,
        'tillar': ['javascript', 'html', 'css', 'typescript', 'react', 'nodejs']
    },
    'rahmatulla': {
        'familiya': 'rahmullayev',
        'ism': 'rahmatulla',
        'tyil': 2000,
        'tillar': ['mojo', 'python', 'c++']
    }
}

for names, info in talabalar.items():
    print(names)
    for j in info['tillar']:
        print(j)
    









