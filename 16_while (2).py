# kinolar = []
# print("Yoqtirgan filmlaringiz ro'yxatini tuzamiz!")
# k = 1

# while True:
#     savol = f"{k}-yoqtirgan filmingizni kiriting: "
#     kino = input(savol)
#     kinolar.append(kino)
#     javob = input("Yana kino qo'shasizmi? (yes/no): ") 

#     if javob == "yes":
#         k += 1
#         continue
#     else:
#         break
# son = 1
# print("\nRo'yxat tuzildi!")
# for i in kinolar:
#     print(f"{kinolar.index(i)+1}. {i.title()}")
#     print(f"{son}. {i.title()}")
#     son += 1




# filmlar = {}
# ishora = True
# while ishora:
#     nomi = input("Rejissiyorni kiriting: ")
#     film = input(f"{nomi.title()}ning filmini kiriting: ")
#     filmlar[nomi] = film
    
#     answer = input("Yana ma'lumot qo'shasizmi? (ha/yoq)")

#     if answer == 'yoq':
#         ishora = False


# for ism, film in filmlar.items():
#     print(f"{ism.title()}: {film}")



# odamlar = ['muhammad','jahongir', 'rahmatilla', 'rahmatilla', 
#         'abdulloh', 'rahmatilla', 'akobir', 'jahongir', 'zubayir']

# while 'rahmatilla' in odamlar:
#     odamlar.remove('rahmatilla')
# print(odamlar)


students = ['muhammad','jahongir', 'rahmatilla', 'jahongir', 'zubayir']
baholanganlar = {}
while students:
    student = students.pop()
    baho = int(input(f"{student.title()}ning bahosini kiriting: "))
    # print(f"{student.title()}: {baho}")
    print(f"{student.title()} baholandi!")

    baholanganlar[student] = baho
print(baholanganlar)










