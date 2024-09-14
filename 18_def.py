# def ism_sharifi(ism, familiya):
#     full_name = f"{ism.title()} {familiya.title()}"
#     return full_name

# print(ism_sharifi('abdulloh', 'ibragimov'))



# def name_last_name(ism, familiya, otasining_ismi=''):
#     if otasining_ismi:
#         full_name = f"{ism.title()} {familiya.title()} {otasining_ismi.capitalize()}"
#     else:
#         full_name = f"{ism.title()} {familiya.title()}"
#     return full_name

# student1 = name_last_name('UmAr', 'JaloloV', "SarDor o'g'li")

# print(student1)



def auto_info(made, model, color, engine, year, price=None):
    auto = {
        "Company": made,
        "Model": model,
        "Color": color,
        "Engine": engine,
        "Year": year,
        "Price": price
    }
    return auto


mashina1 = auto_info("Lamborghini", "Aventador", 'qora', 'automatic', 2025, 550_000)
mashina2 = auto_info("Rollse Royce", "Phantom", 'qora', 'automatic', 2025)
mashina3 = auto_info("Jetour", "X2", 'qora', 'automatic', 2025)
mashina4 = auto_info("Cadillac", "Escalade", 'qora', 'automatic', 2025)
mashina5 = auto_info("Tesla", "M3", 'qora', 'automatic', 2025, 550_000)

cars = [mashina1, mashina2, mashina3, mashina4, mashina5]
for i in cars:
    if i['Price']:
        price = f"{i['Price']} $"
    else:
        price = "Noma'lum"
    print(f"{i['Company']} {i['Model']}. Rangi: {i['Color']} {price}")

print(cars[3])


car = []
while True:
    made = input("Ishlab chiqargan kompaniya: ")
    model = input("Modeli: ")
    color = input("Color: ")
    price = input("Narxi: ")
    engine = input("Motori: ")
    year = input("Yili: ")
    
    car.append(auto_info(made, model, color, price, engine, year))
    answer = input("Yana mashina olasizmi? ")
    if answer == "stop":
        break
print(car)

# def masofa(min, max):
#     numbers = []
#     while min < max:
#         numbers.append(min)
#         min += 1 # min = min + 1
#     return numbers
# print(masofa(0, 10+1))


# def oraliq(min, max, step=1):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += step
#     return sonlar
# print(oraliq(0, 21, 5))

