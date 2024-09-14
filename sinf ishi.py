
"""# 1. Foydalanuvchidan ismi va yoshini so'rab, uni tug'ilgan yilini hisoblaydigan funksiya yozing.

# def isim_yosh(name:str,tyil):
#     print(f" {name.title()}. Sizni tugilgan yilingiz {2024-tyil} ")

# isim_yosh(input("Ismingizni kiriting : "),int(input("yoshingizni kiriting : ")))


# 2. Foydalanuvchidan son olib, uni kvadrati va kubini ekranga matn ko'rinishida chiqaring.

# def son(x):
#     print(f" {x **2}-kvadrati.{x ** 3}-kubi")
# son(int(input("Sonni kiriting :")))

# 3. Foydalanuvchidan son olib, uni juft yoki toq son ekanligini aniqlovchi dastur yozing.

# def son(x):
#     if x % 2 == 0:
#      print('Juft son')
#     else:
#      print("Toq son")
# son(int(input("Son kiriting >>> ")))

# 4. Foydalanuvchidan a va b son olib, a ning b-darajasini hisoblovchi dastur yozing.

# def son():
#     a = float(input("a >>> "))
#     b = float(input("b >>>"))
#     c = a ** b
#     print(f"{a} ning {b} -darajasi {c} ga teng!")
# son()


# 5. Foydalanuvchidan ikkita son kiritishini so'rang. Ikkala sonlar ichidan eng kattasi matn ko'rinishida ekranga chiqsin.

# def son():
#     a = int(input(" a son kiriting >>>  "))
#     b = int (input(" b son kiriting >>> "))
#     if a > b :
#         print("a  katta b dan ")
#     else:
#         print("a kichik b dan ")
# son()

# 6. Foydalanuvchidan son qabul qilib, ushbu sonni 2 dan 10 gacha bo'lgan sonlar ichida qoldiqsiz bo'linuvchi sonlarni ekranga chiqaring.

# def son():
#     a = int(input("Son kiriting : "))
#     # b = 2,10
#     if a % 2 == 0:
#         print('Juft son')
#     else:
#         print("Toq son")
# while True:
#     son()




# def son():
#     a = int(input("a ga son kiriting >>> "))
#     b = int(input("b ga son kiriting >>> "))
#     c = int(input("c ga son kiriting >>> "))
#     if a > b > c :
#         print(f"{a}>{b}>{c}")
#     elif a > c > b:
#         print(f"{a}>{c}>{b}")
#     elif b > a > c:
#         print(f"{b}>{a}>{c}")
#     elif b > c > a:
#         print(f"{b}>{c}>{a}")
#     elif c > a > b:
#         print(f"{c}>{a}>{b}")
#     elif c > b > a:
#         print(f"{c}>{b}>{a}")

# son()
"""

"""# Sinf ishi/Uyga vazifa:
# 1. Userdan 3+ ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, elektron manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi dastur yozing. Ba'zi argumentlarni ixtiyoriy qilib qo'ying.

# def son():

#     malumot =[]
#     for i in range(3):
#         user1 = {
#     "Ism":input("Ismingizni kiriting >>>"),
#     "Familiya":input("Familiyangizni kiriting >>>"),
#     "Tug'ilgan yil":int(input("Tug'ilgan yilingizni kiriting >>>")),
#     "Tug'ilgan joy":input("Tug'ilgan joyingizni kiriting >>>"),
#     "Elektron manzili":input("Elektron manzilingizni kiriting >>>"),
#     "Telefon raqam":int(input("Telefon raqamingizni kiriting >>>"))}
    

#     malumot.append(user1)
#     print(malumot)
# son()



# 2. Userdan uchta son qabul qilib, ulardanr eng kattasini aniqlovchi funksiya yozing.

# def son():
#     a = int(input("Son kiriting >>> "))
#     b = int(input("Son kiriting >>> "))
#     c = int(input("Son kiriting >>> "))

#     if a > b > c :
#         print(f"{a}>{b}>{c}")
#     elif a > c > b:
#         print(f"{a}>{c}>{b}")
#     elif b > a > c:
#         print(f"{b}>{a}>{c}")
#     elif b > c > a:
#         print(f"{b}>{c}>{a}")
#     elif c > a > b:
#         print(f"{c}>{a}>{b}")
#     elif c > b > a:
#         print(f"{c}>{b}>{a}")
# son()


# 3. Userdan a va b sonlar kiritishini so'rang. 
# a sonining b-darajasini aniqlovchi funksiya yozing.


# def son():
#     a = int(input("a ga son kiriting: "))
#     b = int(input("b ga son kiriting: "))
#     c = a ** b
#     print(f"{a} ning {b} -darajasi {c} ga teng!")
# son()"""

"""# Sinf ishi/Uyga vazifa: 
# 1. Darsda o'tilgan narxini_kirit funksiyasiga o'xshash funksiya yarating. Yaratgan funksiyangizdagi ro'yxat ichidagi ma'lumotlar saqlanib qolsin.

# def narxini_kirit(nomi):
#     narxlari = {}
#     while nomi:
#         nom = nomi.pop()
#         summa = float(input(f"{nom.title()}ning narxini kiriting: "))
#         narxlari[nom] = summa
#     return narxlari
# sabzavotlar = ["zaytun","kartoshka","piyoz","pamidor","bodiring","baqlajon"]
# narxlari = narxini_kirit(sabzavotlar[:])
# print(narxlari)
# print(sabzavotlar)
# a = sabzavotlar[:]
# print(id(sabzavotlar))
# print(id(a))



# 2. User kiritgan istalgancha sonlarni qabul qiluvchi va ularni yig'indisini hisoblab qaytaruvchi funksiya yarating. 


# 3. Matnlardan iborat ro'yxat qabul qilib, ro'yxat ichidagi har bir matnning birinchi harfini bosh harfga o'zgartiruvchi funksiya yozing.

# 4. Davlatlar haqidagi ma'lumotlarni qaytaruvchi funksiya yarating. Ushbu funksiya ichidagi ma'lumotlarni user kiritisin. 

# 5. talaba_info nomli funksiya yarating. Ushbu funksiya user kiritadigan talabalar ma'lumotlarini lug'at ko'rinishida qaytaradigan funksiya bo'lsin. 

# 6. worker_info nomli ishchilar ma'lumotlarini lug'at ko'rinishida qaytaruvchi funksiya yarating. Ushbu funksiyada keylarni ham, ularning qiymatlarini ham user kiritsin. 
"""


"""# Sinf ishi/Uyga vazifa: 
# 1. Talabalar haqidagi ma'lumotlarni userdan kiritishini so'rang. Ushbu ishni boshqa fayl orqali, boshqa bir fayl ichidagi funksiyalarni chaqirgan holda amalga oshiring.
# P.s.: Darsda ko'rsatilgan dastur kabi bo'lishi kerak.

# 2. Davlatlar haqidagi ma'lumotlarni user orqali yig'ib boshqa fayl orqali chaqirib, ekranga chiqaring.


# def davlat_info(davlat,capital,official_languages,demonym,government,bosh_vazir,mustaqilik,maydon,aholi):
#     davlat ={
#         "davlat": davlat,
#         "poytaxti": capital,
#         "rasmiy tilli": official_languages,
#         "hukumat" : demonym,
#         "prezident" : government,
#         "bosh vazir": bosh_vazir,
#         "mustaqilik": mustaqilik,
#         "maydoni": maydon,
#         "aholi": aholi,
#          }
#     return davlat


# def davlat_kirit():
#     davlatlar = []
#     while True:
#         davlat = input("Davlatni nomini kiriting: ")
#         poytaxti = input("Poytaxtini kiriting: ")
#         rasmiy_tilli = input("Rasmiy tillini kirting: ")
#         hukumat = input("Huktumatini kiriting: ")
#         prezidenti = input("Prezidentini  kiriting: ")
#         bosh_vazir = input("Bosh vazirini kiriting: ")
#         mustaqilik = int(input("Qachon mustaqilika erishgan: "))
#         maydoni = int(input("Maydonini kiriting: "))
#         aholi = int(input("Aholisini kiriting: "))
#         davlatlar.append(davlat_info(davlat, poytaxti, rasmiy_tilli, hukumat, prezidenti, bosh_vazir, mustaqilik, maydoni, aholi))
#         javob = input("Yana malumot kiritasizmi? (ha/yoq) ".lower())
#         if javob == 'yoq':
#             break
#     return davlatlar



# def info_davlat(davlat_info):
#     print(f"{davlat_info['Davlatni nomini kiriting: '].title()}, "
#     f"{davlat_info['Poytaxtini kiriting: '].title()}, "
#     f"{davlat_info['Rasmiy tillini kirting: '].title()}, "
#     f"{davlat_info['Huktumatini kiriting: ']}, "
#     f"{davlat_info['Prezidentini  kiriting: ']}, "
#     f"{davlat_info['Bosh vazirini kiriting: '].title()}, "
#     f"{davlat_info['Qachon mustaqilika erishgan: '].title()}, "
#     f"{davlat_info['Maydonini kiriting: '].title()}, "
#     f"{davlat_info['Aholisini kiriting:'].title()}, ")
#     return davlat_info

# 3. User kiritgan sonni kvadratidan to 10-darajasigacha matn ko'rinishida ekranga chiqaring. Ushbu dasturni boshqa fayl ichidagi funksiyani chaqirish orqali amalga oshiring.
# P.s.: 
# 2 ning darajasi 4,
# 3 ning darajasi 9 va h.k.

# def son():
#     a = int(input("son kiriting >>> "))
#     for i in range(2, 11):
#           print(f"{a} ning {i} darajasi {a ** i} - ga teng")
# son()



# 4. User kiritgan a va b sonlarni a ning b-darajasini ekranga chiqaring. Ushbu dasturni boshqa fayl ichidagi funksiyani chaqirish orqali amalga oshiring.

# def son():
#     a = int(input("a >>> "))
#     b = int(input("b >>>"))
#     c = a ** b
#     print(f"{a} ning {b} -darajasi {c} ga teng!")
# son()"""


"""# game

# import random as r

# def game():
#     name = ['muhamadali','abdulloh', 'rahmatilla', 'jaxongir']
#     dars = ['premetiv','no_premetiv','list','tuple', 'dictionar','while','def']
#     darses = r.choice(dars)
#     names = r.choice(name)
#     names.pop(names.index(name))
#     darses.pop(darses.index(dars))
# print(game())


# import random as r
# def game():
#     name = ['muhamadali', 'abdulloh', 'rahmatilla', 'jaxongir']
#     dars = ['premetiv', 'no_premetiv', 'list', 'tuple', 'dictionar', 'while', 'def']

#     # Choose a random name and dars, and remove them from their lists
#     names = r.choice(name)
#     name.pop(name.index(names))  # Remove the selected name from the list

#     darses = r.choice(dars)
#     dars.pop(dars.index(darses))  # Remove the selected dars from the list

#     # Return the selected names and darses
#     return names, darses

# Test the game function
# print(game())"""

"""# Sinf ishi/Uyga vazifa: 
# 1. User kiritgan sonning kvadrat ildizini boshqa faylda chaqirib math modulidan foydalangan holda ekranga chiqaring.

# import math
# user = int(input("son kiriting >>> "))
# print(f"- sonni kvadrati: {int(math.pow(user, 2))}")
# print(f"- sonni ildizi: {math.sqrt(user) }")

# 2. 0-dan 100-gacha bo'lgan sonlar oralig'idagi  random moduli tasodifiy tanlash orqali boshqa modul ichida o'sha sonning kvadrati va kubini ekranga chiqaring.

# import random as r
# import math
# number = r.randint(0, 10)
# print(f"{number} sonni kvadrati: {int(math.pow(number, 2))} ; sonni kubi: {int(math.pow(number, 3))}")

# 3. ismlar saqlangan list ichidan random moduli orqali tasodifiy ismni birinchi harfini katta harf qilib boshqa fayl ichida ekranga chiqaring.

# import random as r

# ismlar = ["raxmatilla".title(),
#           "abdulloh".title(),
#           "muhamadali".title(),
#           ]
# ism =r.choice(ismlar)
# ismlar.pop(ismlar.index(ism))
# print(ism)
# print(ismlar)

# P.s.: Yuqoridagi sinf/uyga vazifalarni boshqa fayl ichida tayyorlab main.py nomli fayl ichida chaqiring.
"""


"""# Sinf ishi/Uyga vazifa:
# 1. Berilgan sonni 10 ga ko'paytiruvchi lambda funksiya yozing

# son = lambda a, b : a * b
# print(son(int(input("Son kiriting >>> ")), int(10)))

# 2. Ikki son qabul qilib, ularning yig'indisini qaytaruvchi lambda funksiya yozing.

# son1 = lambda a, b : a + b 
# son2 = lambda a, b : a - b
# son3 = lambda a, b : a * b
# son4 = lambda a, b : a / b
# print(son3(int(input("son kiriting: ")), int(input("son kiriting: "))))


# 3. random moduli ichidagi sample funksiyasi yordamida 0 dan 100 gacha sonlar oralig'idagi tasodifiy  10 yoki 20 ta sonlar ro'yxatini tuzing.


# import random as a

# sonlar = a.sample(range(100), 10)


# print(sonlar)


# 4. Yuqoridagi dasturdan foydalanib map() va lambda funksiyalari orqali tasodifiy tanlangan 10 yoki 20 ta sonlar kvadratlarini chiqaruvchi ro'yxat tuzing.

# import random as s

# sonlar = s.sample(range(100), 20)
# son = list(map(lambda son: son ** 2, sonlar))

# print(f"{sonlar} kvadrati: {son}")

# 5. 3-masaladan foydalanib filter() va lambda funksiyalari orqali tasodifiy tanlangan 10 yoki 20 ta faqat juft sonlar ro'yxatini ajratib oluvchi ro'yxat tuzing.

# filter()
# import random as r

# sonlar = r.sample(range(100), 20)
# def juft(x):
#     return x % 2 == 0

# juft_sonlar = list(filter(juft, sonlar))
# print(sonlar)
# print(juft_sonlar)"""


"""# 1. Maxsus Kalitga Qiymat Qo'shish
# Vazifa: Sizga bitta lug'at beriladi, unda har xil turdagi ma'lumotlar saqlanadi. Masalan, {1: 'apple', 2: 'banana', 'x': 100}. Funksiya yozing, u kiritilgan lug'atda 'x' kalitini tekshirsin va agar mavjud bo'lsa, uning qiymatini 10 ga oshirsin. Agar 'x' kaliti mavjud bo'lmasa, x: 10 juftligini lug'atga qo'shsin.
# Kiruvchi ma'lumot: {'a': 5, 'x': 50}
# Natija: {'a': 5, 'x': 60}



# 2. Qiymatlarni Tartiblash
# Vazifa: Sizga lug'at beriladi, uning kalitlari butun sonlar, qiymatlari esa butun sonlar bo'ladi. Funksiya yozing, u lug'atdagi qiymatlarni ortib borish tartibida tartiblasin va tartiblangan qiymatlar bilan yangi lug'at hosil qilsin.
# Kiruvchi ma'lumot: {3: 20, 1: 40, 2: 10}
# Natija: {2: 10, 3: 20, 1: 40}

# 3. Kalitlar Hisobi
# Vazifa: Funksiya yozing, u berilgan lug'atning kalitlari sonini hisoblasin va natijani qaytarsin.
# Kiruvchi ma'lumot: {'name': 'John', 'age': 25, 'city': 'New York'}
# Natija: 3

# 4. Lug'atlarni Birlashtirish
# Vazifa: Sizga ikkita lug'at beriladi. Funksiya yozing, u ikkala lug'atni birlashtirib, yangi lug'at hosil qilsin. Agar bir xil kalit ikkala lug'atda ham mavjud bo'lsa, qiymatlar o'rtacha qiymat sifatida olinadi (ikki qiymat yig'indisini ikkiga bo'ling).
# Kiruvchi ma'lumot: {1: 100, 2: 200} va {2: 300, 3: 400}
# Natija: {1: 100, 2: 250, 3: 400}

# 5. Qiymatlarni Filtrlash
# Vazifa: Funksiya yozing, u lug'atdan faqat qiymati musbat bo'lgan elementlarni olib qoladi va qaytaradi.
# Kiruvchi ma'lumot: {1: -5, 2: 3, 3: -2, 4: 10}
# Natija: {2: 3, 4: 10}"""

"""# my=['ona','ota',[15,56,'matn',[25,'opa','uka'],['aka']],2,5,8,'akam']
# for i in my:
#     if type(i) != list:
#         if isinstance (i, int):
#             print(i, end=" ")
#         else:
#             print(i.upper(), end=" ")
#     elif type(i) == list:
#         for j in i:
#             if type(a) == list:
#                 for o in j:
#                     if isinstance(o, int):
#                         print(b, end=" ")
#                     else:
#                         print(o.upper(), end=" ")
#             elif type(a) != list:
#                 if isinstance(a, int):
#                     print(a, end=" ")
#                 else:
#                     print(a.upper(), end=" ")



# def j(x):
#     for i in x:
#         if type(i) != list:
#             if isinstance (i, int):
#                 print(i, end=" ")
#             else:
#                 print(i.upper(), end=" ")
#         else:
#             j(i)
# j(my)"""

"""# Sinf ishi/Uyga vazifa:
# 1. Userdan biror harf kiritishini so'rang va uni ekranga chiqaring. Agar u harf bo'lsa ekranga chiqsin, Aks holda "Siz harf kiritmadingiz" degan yozuv chiqsin va user to'g'ri qiymat kiritmaguncha dastur tugamasin.

# while True:
#     user = input("harf kiriting: ")
#     try:
#         user = int(user)
#         print("Siz harf kiritmadingiz!")
#     except:
#     # user =int(user)
#         print(user)
#         break

# 2. Yuqoridagi dastur bo'yicha songa nisbatan ham qiling.


# while True:
#     user = input("son kiriting: ")
#     try:
#         user = int(user)
#         print(user)
#         break
#     except:
#         print("Siz son kiritmadingiz!")"""


    # print((int(input(">>>: ")[::-1])))


"""# def reverse_digits(num: int) -> None:
#     result=0
#     while num !=0:
#         result *=10
#         digit =num %10
#         result += digit
#         num //=10
#     return result
# print(reverse_digits(int(input("son kiriting: "))))"""

"""# Sinf ishi/Uyga vazifa:
# 1. txt formatda file ochib uning ichini 10+ ism-familiyalar bilan to'ldiring va dasturlash muhiti orqali kiritilgan ma'lumotlarni ekranga chiqaring.

# with open('ism.txt', 'r') as f:
#     pi = f.read()
#     pi = pi.replace('\n', '')
#     print(pi)


# 2. txt formatda file ochib uning ichini turli sonlar bilan to'ldiring va dasturlash muhiti orqali ular ustida matematik amallar bajaring.
"""


"""# user = int(input("Bitta son kiriting: "))
# for i in range(user,0 , -1):
#     if i % 2 == 0:
#         print(i, end=" ")"""

"""# SInf ishi / Uyga vazifa: 
# 1. File ochib guruhdagi o'quvchilar ma'lumotlari bilan to'ldiring va uni o'qing(Ekranga chiqaring.)  

# import pickle

# student1 = {'ism': 'Abdulloh', 'familiya': 'Baxtiyorov', 'tyil': 2010}
# student2 = {'ism': 'Raxmatilla', 'familiya': 'Isroilov', 'tyil': 2006}
# student3 = {'ism': 'Muxamadali', 'familiya': 'Saidaxmedov', 'tyil': 2007}
# student4 = {'ism': 'Otajon', 'familiya': 'Bozozrboyev', 'tyil': 1999}
# student5 = {'ism': 'Jaxongir', 'familiya': "Jo'rabekov", 'tyil': 2005}

# with open('info.dat', 'wb') as f:
#     pickle.dump(student1, f)
#     pickle.dump(student2, f)
#     pickle.dump(student3, f)
#     pickle.dump(student4, f)
#     pickle.dump(student5, f)

# with open('info.dat', 'rb') as f:
#     talaba1 = pickle.load(f)
#     talaba2 = pickle.load(f)
#     talaba3 = pickle.load(f)
#     talaba4 = pickle.load(f)
#     talaba5 = pickle.load(f)


# print(talaba1)
# print(talaba2)
# print(talaba3)
# print(talaba4)
# print(talaba5)

# 2. Darsda o'rgangan pickle metodi orqali file ochib Pythonda uni o'qing.

# 3. Sizning tug'ilgan kuningiz pi soni tarkibida mavjud yoki mavjud emasligini aniqlovchi dastur yozing.

# with open('pi (2).txt','r') as f:
#     if input() in f.read().replace('\n',''):
#         print("mavjud")


# 4. Foydalanuvchidan turli xil ma'lumotlar so'rab, har bir kiritilgan ma'lumot yangi qatordan filega yozib boruvchi dastur yozing. Dastur qayta chaqirilganida yangi ma'lumotlar file oxiridan qo'shilsin (Yangi filega emas).

# def info_data():
#     with open("sonlar.txt", "a") as f:
#         while True:
#             user =input("Ma'lumot kiriting (yoki 'stop' bilan tugating): )")
#             if user.lower() == 'stop':
#                 break
#             f.write(user + '\n')
# info_data()"""

# Sinf ishi/Uyga vazifa:
# 1. Ustoz nomli class tuzing. Ushbu classning ichida argumentlar sifatida ism, familiya, yosh, tyil bering va 5+ obyektlar berib ko'ring.

# class Ustoz:
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.son = 1
#         self.ustozlar = []

#     def info(self):
#         return f"{self.ism} {self.familiya} {self.tyil}"
    
#     def update_son(self):
#         self.son += 1

# user = Ustoz((input("Ismingizni kiriting: ")), input("familiyangizni kiriting: "), 2024 - int(input("yoshingizni kiriting: ")))
# print(user.info())

# 2. Talaba nomli class ochib, uning ichida talabalar ma'lumotlarini qaytaruvchi metod yozing. 5+ obyekt tuzish orqali ma'lumot beruvchi metodni chaqiring.

# class Talaba:
#     def __init__(self, name, familiya, tyil):
#         self.name = name
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1

#     def set_kurs(self, kurs):
#         self.bosqich = kurs 

#     def update_kurs(self):
#         self.bosqich += 1

#     def get_info(self):
#         return f"{self.name} {self.familiya} {self.tyil} {self.bosqich}-bosqich talabasi."

#     def get_name(self):
#         return self.name
    
#     def get_familiya(self):
#         return self.familiya
# a = int(input("nechi talaba  kiritasiz: "))
# for i in range(a):
#     user = Talaba((input("Ismingizni kiriting: ")),input("Familliyangizni kiriting: "),int(input("Tug'ilgan yilingizni kiriting: ")))
#     print(user.get_info())


# Sinf ishi/Uyga vazifa:
# 1. Auto nomli class oching. Uning argumentlar sifatida model, rangi, nomi, narxi va h.k.larni kiriting va ekranga chiqaring.

# class Auto:
#     def __init__(self, model, nomi, rangi, narxi):
#         self.model = model
#         self.nomi = nomi
#         self.rangi = rangi
#         self.narxi = f'{narxi:,.0f}'

#     def get_info(self):
#         return f"{self.model} : {self.nomi} : {self.rangi} : {self.narxi}.UZS"

# a = int(input("nechta mashina kiritasiz: "))
# for i in range(a):
#     user = Auto((input("Modelini kiriting: ")),input("Nomini kiriting: "),int(input("Rangini kiriting: ")), int(input("Narxini kirting: ")))
#     print(user.get_info())

# # 2. Avtosalon nomli class oching va uning ichini bir nechta argumentlar bilan to'ldiring. Uning ichida avtomabillar ma'lumotini qaytaruvchi metod tuzing. Obyektga qiymatni foydalanuvchidan oling.


# git init
# git add .
# git commit -m "first commit"
# git branch -M main
# git remote add origin git@github.com:otajonbozorboyev/Weather-Bot.git
# git push -u origin main











































































































