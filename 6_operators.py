# ______SHART OPERATORLARI:______
# Shart operatorlari quyidagicha:
# 1. Arifmetik operatorlar;
# 2. Belgilash operatorlar;
# 3. Taqqoslash operatorlar;
# 4. Mantiqiy operatorlar;
# 5. Identifikatsiya operatorlar;
# 6. A'zolik operatorlar.


# 1. Arifmetik operatorlar:
#  + - * ** / // % 
# a = 50
# b = 4
# c = a % b
# print(c)
# print(5 % 2)


# 2. Belgilash operatorlar;
#  = (x = 5)
# += (x+=5) (x = x + 5)
# x = 1
# print(x)
# x += 5 # x = x + 5
# print(x)

# -= (x=x-5)
# *= (x=x*5)
# /= (x=x/5)
# %= (x=x%5)
# //= (x=x//5)
# print(5/2) # 2.5
# print(5//2) # 2
# **= (x=x**5)

# 3. Taqqoslash operatorlar;
# ==
# !=
# > (x>y)
# < (x<y)
# >= (x>=y)
# <= (x<=y)


# 4. Mantiqiy operatorlar;
# and - & (x<y and/* x<10)
# or - | (x<y or/+ x<10)
# not - not(x<y or/+ x<10)


# 5. Identifikatsiya operatorlar;
# is - ==
# x = ['apple', 'banana']
# y = ['apple', 'banana']
# z = x
# print(x is z)
# print(x is y)


# is not - !=

# 6. A'zolik operatorlar.
# in - ning ichida mavjudmi

# print('abs' in "ecfrvdfbgtreasdcvbabssfasdf")
# print('abs' not in "ecfrvdfbgtreasdcvbabssfasdf")




# 1. _____ARIFMETIK OPERATORLAR quyidagicha:______
# + - * / bularni barchasini bilasiz.
# % - foizli bo'lish:
# a = 50
# b = 4
# d = a % b
# print(d) # Ushbu operatorda har doim .dan keyingi qiymatni olib beradi. 
# // - Ushbu bo'luv uchun ishlatiladigan operator .keyingi sonlarni ko'rsatmaydi. 
# c = a // b
# print(c)

# ________________________________________________________

# 2. _____BELGILASH OPERATORLAR quyidagicha:_____

# = (x=5) Bu teng belgisi bo'lib shu narsa ushbu narsaga teng degan ma'noda keladi. 
# += (x+=3) Bu x=x+3 ning qisqartirib yozilgan ko'rinishi. Har ikkalasi ham to'g'ri.
# -= (x-=3) Bu Bu x=x-3 ning qisqartirib yozilgan ko'rinishi. Har ikkalasi ham to'g'ri.
# *= (x*=3) Bu Bu x=x*3 ning qisqartirib yozilgan ko'rinishi. Har ikkalasi ham to'g'ri.
# /= (x/=3) Bu Bu x=x/3 ning qisqartirib yozilgan ko'rinishi. Har ikkalasi ham to'g'ri.
# %= (x%=3) Bu Bu x=x%3 ning qisqartirib yozilgan ko'rinishi. Har ikkalasi ham to'g'ri.
# //= (x//=3) Bu Bu x=x//3 ning qisqartirib yozilgan ko'rinishi. Har ikkalasi ham to'g'ri.
# **= (x**=3) Bu Bu x=x**3 ning qisqartirib yozilgan ko'rinishi. Har ikkalasi ham to'g'ri.

# ____________________________________________________________________

# 3. _____TAQQOSLASH/SOLISHTIRISH OPERATORLAR quyidagicha:_____
# ==  Teng belgisi (x==y) shu narsa ushbu narsaga teng
# != Teng emas belgisi (x!=y) shu narsa ushbu narsaga ten emas degan ma'noni beradi.
# > (x>y) dan katta degan ma'noni beradi.
# < (x<y) dan kichik degan ma'noni beradi.
# >= (x>=y) dan katta yoki teng degan ma'noni beradi.
# <= (x<=y) dan kichik yoki teng degan ma'noni beradi.

# _____________________________________________________________________

# 4. _____MANTIQIY OPERATORLAR quyidagicha:_____
# and - &  (x<y and/* x<10) ushbu belgi va/ko'paytirish ma'noni beradi. Bunda barcha kelgan shartlardan o'tsagina TRUE beradi.
# or - | (x<5 or x<4) ushbu belgi yoki degan ma'noni beradi. Bunda qatnashgan shartlarning bittasi ham to'g'ri kelsa natija TRUE beradi.
# not - not(5>3 and 5>10) Ushbu belgi False qaytaradi. Chunki bitta shartdan o'tdi lekin qolganidan emas. Katta emasmi degan ma'noni beradi.

# ___________________________________________________________________________

# 5. _____IDENTIFIKATSIYA OPERATORLAR quyidagicha:_____

# is - (==) Tengmi degan ma'noni beradi.
# x = ['apple', 'banana']
# y = ['apple', 'banana'] 
# z = x
# print(x is z) 

# print(x is y)

# print(x == y)

# is not - (!=) Teng emasmi degan ma'noni beradi
# __________________________________________________________________

# 6. ______A'ZOLIK OPERATORLAR quyidagicha:_____
# in - ning ichida mavjudmi degan ma'ninu beradi.
# print("banana" in x)

# not in - ning ichida mavjud emasmi degan ma'noni beradi.
# print("lemon" not in x)

# _________________________________________________________________

# print((5+5)*(10//5)) # 20
# print(55+10-20//2) # 55

print(int((4*4)**(0.5))) # 4
print((True+True)**2) # 4


