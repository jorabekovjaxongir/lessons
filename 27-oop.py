# OOP - Object Oriented Programming -> Obyektga yo'naltirilgan dasturlash

# OOP 4 ta tamoyili mavjud:
# 1. Vorisli
# 4. Polimorfizm.k - Inheritance;
# 2. Inkapsulatsiya;
# 3. Abstraksiya;

# son = 10
# matn = "so'z"
# print(type(son))
# print(type(matn))

# double underscore - dunder methods
# class Student:
#     def __init__(self, ismi, familiya, tyil):
#         self.ismi = ismi
#         self.familiya = familiya
#         self.tyil = tyil

#     def info(self):
#         return f"{self.ismi} {self.familiya} {self.tyil}"

# talaba1 = Student('muhammadali', 'rahmatullayev', 2005)

# print(talaba1.info())
# print(talaba1.ismi)
# print(talaba1.familiya)
# print(talaba1.tyil)



# class Car:
#     def __init__(self, made: str, model: str, year: int):
#         self.made = made
#         self.model = model
#         self.year = year

#     def info(self):
#         print(f"Men bugun {self.made.capitalize()} {self.model.upper()} sotib oldim! Yili: {self.year}")


# car1 = Car("mercedes", 'model 3', "2024")
# car1.info()




# class Talaba:
#     def __init__(self, name, familiya, tyil):
#         self.name = name
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1

#     def info(self):
#         return f"{self.name}, {self.familiya} {self.tyil}. {self.bosqich}-bosqich talabasi."

#     def update_bosqich(self):
#         self.bosqich += 1

# talaba1 = Talaba("xusan", "rustamov", 2024-30)
# print(talaba1.info())
# talaba1.update_bosqich()
# talaba1.update_bosqich()
# print(talaba1.info())



# class Lesson:
#     def __init__(self, nomi) -> None:
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []

#     def add_talabalar(self, talaba):
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1

#     def info_students(self):
#         return [talaba.info() for talaba in self.talabalar]


# astronomy = Lesson("Astronomiya")
# dasturlash = Lesson("Backend")

# talaba1 = Talaba("Muhammadali", 'Akobirov', 2005)
# talaba2 = Talaba("Rahmatulla", 'Ibragimov', 2007)
# talaba3 = Talaba("Jahongir", 'Alisherov', 1995)
# talaba4 = Talaba("Abdulloh", 'Muhammadov', 2010)

# astronomy.add_talabalar(talaba2)
# astronomy.add_talabalar(talaba3)

# dasturlash.add_talabalar(talaba1)
# dasturlash.add_talabalar(talaba4)

# print(astronomy.talabalar_soni)
# print(dasturlash.talabalar_soni)

# print(astronomy.info_students())
# print(dasturlash.info_students())


# set va get

class Talaba:
    def __init__(self, name, familiya, tyil):
        self.name = name
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def set_kurs(self, kurs):
        self.bosqich = kurs 

    def update_kurs(self):
        self.bosqich += 1

    def get_info(self):
        return f"{self.name} {self.familiya} {self.bosqich}-bosqich talabasi."

    def get_name(self):
        return self.name
    
    def get_familiya(self):
        return self.familiya

t1 = Talaba("Jahongir", 'Jahongirov', 1995)
t2 = Talaba("Muhammadali", 'Abullohov', 2005)


print(t1.get_info())
t1.update_kurs()
print(t1.get_info())
t2.set_kurs(4)
print(t2.get_info())










