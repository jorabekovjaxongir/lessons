# 'w'
# 'a'
# pickle


# 'r+' fileni o'qish va yozish uchun ochish.
# 'a+' filega ma'lumot qo'shish va o'qish uchun ochish, file mavjud bo'lmasa yangi file ochadi.
# # 'a' filega ma'lumot qo'shish uchun ishlatiladi.
# tyil = 2000
# with open('teacher.txt', 'w') as f:
#     f.write("Tadashi Hamada"+'\n')
#     f.write('1999')
#     # f.write(str(tyil))
#     f.write(f"\nMening yoshim: {2024-tyil}")


# with open('teacher.txt', 'a') as f:
#     f.write(f"\nAbbosjon Bozorboyev")



# PICKLE
import pickle

student1 = {'ism': 'Abbos', 'familiya': 'Bozorov', 'tyil': 2002}
student2 = {'ism': 'Odiljon', 'familiya': 'Bozorov', 'tyil': 2001}

# with open('info', 'wb') as f:
with open('info.dat', 'wb') as f:
    pickle.dump(student1, f)
    pickle.dump(student2, f)

with open('info.dat', 'rb') as f:
    talaba1 = pickle.load(f)
    talaba2 = pickle.load(f)

print(talaba1)
print(talaba2)















