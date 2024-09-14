# try except

# age = input("Yoshingizni kiriting: ")
# age = int(age)
# print(f"Siz {2024-age}-yilda  tug'ilgansiz!")


# age = input("Yoshingizni kiriting: ")
# try:
#     age = int(age)
#     print(f"Siz {2024-age}-yilda  tug'ilgansiz!")
# except:
#     print("Dastur tugadi!")



# age = input("Yoshingizni kiriting: ")
# try:
#     age = int(age)
# except:
#     print("Butun son kiritmadingiz!")
# else:
#     print(f"Siz {2024-age}-yilda tug'ilgansiz!")



# ValueError
# age = input("Yoshingizni kiriting: ")
# try:
#     age = int(age)
# except ValueError:
#     print("Butun son kiritmadingiz!")
# else:
#     print(f"Siz {2024-age}-yilda tug'ilgansiz!")



# ZeroDivisionError
# a, b = 5, 10
# try:
#     b/(a-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi!")


# IndexError
# fruit = ['banana', 'orange', 'kiwi', 'lemon']
# try:
#     print(fruit[5])
# except IndexError:
#     print(f"fruit o'zgaruvchisi {len(fruit)}ta qiymatdan iborat")



# KeyError
# user = {'username': 'otajonbozorboev',
#         'status': 'CEO',
#         'gmail': 'otajonbozorboev571@gmail.com',
#         'phone': '998912345678'}
# try:
#     print(f"Foydalanuvchi: {user['name']}")
#     # print(f"Foydalanuvchi: {user['gmail']}")
# except KeyError:
#     print("Bunday kalit mavjud emas!")


# FileNotFoundError
# file = 'data.txt'
# try:
#     f = open(file)
# except FileNotFoundError:
#     print(f"\"{file}\" fayli mavjud emas!")


# a = input("Butun son kiriting: ")
# try:
#     a = int(a)
#     b = 20 / a
# except ValueError:
#     print("Butun son kiritmadingiz!")
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi!")
# else:
#     print(f"a = {a}")


# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
#     print(f"Siz {2024-yosh}-yilda tug'ilgansiz!")
# except:
#     print("Butun son kiritmadingiz!")


# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break
# print(f"Siz {2024-yosh}-yilda tug'ilgansiz!")


