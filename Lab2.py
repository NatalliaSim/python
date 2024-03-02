# 1.	Используя функцию map() переписать функцию
# items = [1, 2, 3, 4, 5]
# squared = []
# for i in items:
#     squared.append(i**2)

# Решение:
def squared(i):
    squared = i ** 2
    return squared

numbers = [1, 2, 3, 4, 5]
new_numbers = list(map(squared, numbers))
print("Cписок - ", numbers)
print("Cписок после возведения в квадрат - ", new_numbers)


# 2.	Используйте функцию reduce() и перепишите код

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

# Решение:
from functools import reduce

product = 1
list = [1, 2, 3, 4]
new_list = reduce(lambda x, y: x * y, list)
print(new_list)

# 3.	Используйте функцию map() и перепишите код

numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
       squared.append(num ** 2)
print(squared)

# Решение:
numbers = [1, 2, 3, 4, 5]
new_numbers = list(map(lambda x: x ** 2, numbers))
print("Cписок - ", numbers)
print("Cписок после возведения в квадрат - ", new_numbers)

# 4.	Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip()
# Решение:
x = [1, 2, 3]
y = [4, 5, 6]

union = list(zip(x, y))
print(union)

# 5.	Используйте функцию zip() чтобы преобразовать код:

name_hero = [
    'Hulk',
    'Mr. Fantastic',
    'Invisible Woman',
    'Doctor Strange',
    'Doctor Octopus',
    'Spider-Man',
]

name_real = [
    'Bruce Banner',
    'Reed Richards',
    'Sue Storm',
    'Stephen Strange',
    'Otto Octavius',
    'Peter Parker',
]

# for i in range(len(name_hero)):
#     print(name_hero[i], '-', name_real[i])

# Решение:
hero = list(zip(name_hero, name_real))

print(hero)
# 6.	С помощью функции filter() переместите из списка numbers = [1, 2, 4, 5, 7, 8, 10, 11]
# нечетные элементы в новый список.

# Решение:
numbers = [1, 2, 4, 5, 7, 8, 10, 11]

print(numbers)

new_numbers = list (filter(lambda number: number % 2 == 1, numbers))

print(new_numbers)