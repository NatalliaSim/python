# # стол
# class Table:
#     __mass = 0
#
#     def __init__(self, mass0):
#         self.__mass = mass0
#
#     # чтение инкапсулированной массы
#     def get_mass(self):
#         return self.__mass
#
# #журнальный стол
# class JournalTable(Table):
#     storage = 0
#
#
# # обеденный стол
# class DinnerTable(Table):
#     __places = 0
#
#     def __init__(self, mass0):
#         Table.__init__(self, mass0)
#         self.__places = mass0//5
#
#     # чтение инкапсулированного числа мест
#     def get_places(self):
#         return self.__places
#
#
# class Truck:
#     __maxMass = 0
#     __tables = []
#
#     def __init__(self, max_mass):
#         self.__maxMass = max_mass
#
# #расчет всех погруженных столов
#     def __current_mass(self):
#         s = 0
#         for i in self.__tables:
#             s += i.get_mass()
#         return s
#
# #расчет оставшейся доступности массы для погрузки столов
#     def reserved_mass(self):
#         return self.__maxMass - self.__current_mass()
#
#     def add_table(self, new_table):
#         if new_table.get_mass() < self.reserved_mass():
#             self.__tables.append(new_table)
#             print("Стол массой  " +
#                   str(new_table.get_mass()) +
#                   " загружен!")
#         else:
#             print("Стол массой " +
#                   str(new_table.get_mass()) +
#                   " Не влазит!\nОсталось только " +
#                   str(self.reserved_mass()) + " кг!")
#
#
# newTable = [
#     DinnerTable(10),
#     DinnerTable(20),
#     DinnerTable(30)]
#
# newTruck = Truck(50)
# newTruck.add_table(newTable[0])
# newTruck.add_table(newTable[1])
# newTruck.add_table(newTable[2])



# Вариант 5
# Kласс Car: id, Марка, Модель, Год выпуска, Цвет, Цена, Регистрационный номер
# Функции-члены реализуют запись и считывание полей (проверка корректности), вывода возраста машины.
# Создать список объектов. Вывести:
# a) список автомобилей заданной марки;
# б) список автомобилей заданной модели, которые эксплуатируются больше n лет;


from datetime import datetime
class Car:
    _id__autoincrement = 1
    def __init__(self, brand, model, year, color, price, regist_number):
        self.__id = Car._id__autoincrement
        Car._id__autoincrement += 1
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__color = color
        self.__price = price
        self.__regist_number = regist_number

    # Методы set
    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_color(self, color):
        self.__color = color

    def set_price(self, price):
        self.__price = price

    def set_regist_number(self, regist_number):
        self.__regist_number = regist_number

    # Методы get

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price

    def get_regist_number(self):
        return self.__regist_number

    def check_age(self, current_year):
        return current_year - self.__year

    # Метод для вывода списка авто
    @staticmethod
    def print_car_info(car):
        print (f"ID: {car.__id}, "
                f"{car.__brand} "
                f"{car.__model} "
                f"({car.__year}), "
                f"Цвет: {car.__color}, "
                f"Цена: {car.__price}, "
                f"Регистрационный номер: {car.__regist_number}")

    # Метод для вывода списка автомобилей заданной марки
    @classmethod
    def print_cars_by_brand(cls, car_list, brand_input):
        brand_search = [car for car in car_list if car.__brand == brand_input]
        if brand_search:
            for car in brand_search:
                Car.print_car_info(car)
        else:
            print(f"Автомобилей марки {brand_input} в списке нет.")

    # Метод для поиска автомобилей заданной модели, которые эксплуатируются больше n лет
    @classmethod
    def print_cars_by_model_and_age(cls, car_list, model_input, age_input):
        current_year = datetime.now().year
        model_search = [car for car in car_list if car.__model == model_input and car.check_age(current_year) >= age_input]
        if model_search:
            for car in model_search:
                Car.print_car_info(car)
        else:
            print(f"Нет автомобилей модели ({model_input}), которые эксплуатируются больше ({age_input}) лет.")

car_list = []
n = int(input("Введите количество автомобилей для ввода: "))
for _ in range(n):
    brand = input("Введите марку автомобиля: ")
    model = input("Введите модель автомобиля: ")
    year = int(input("Введите год выпуска автомобиля: "))
    color = input("Введите цвет автомобиля: ")
    price = int(input("Введите цену автомобиля (Пример: 10000): "))
    regist_number = input("Введите регистрационный номер автомобиля: ")

    car = Car(brand, model, year, color, price, regist_number)
    car_list.append(car)

print("\n*********************************************************************************************\n")
# Ввод списка автомобилей заданной марки
brand_input = input("Введите марку автомобиля для поиска: ")

print(f"\nСписок автомобилей введеной марки {brand_input}:")
Car.print_cars_by_brand(car_list, brand_input)

print("\n*********************************************************************************************\n")

# Ввод списка автомобилей заданной модели, которые эксплуатируются больше n лет
model_input = input("Введите модель автомобиля для поиска: ")
age_input = int(input("Введите возраст авто: "))

print(f"\nСписок автомобилей введеной модели ({model_input}), эксплуатирующихся более ({age_input}) лет:")
Car.print_cars_by_model_and_age(car_list, model_input, age_input)

print("\n*********************************************************************************************\n")