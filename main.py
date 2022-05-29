# 1 Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

# list = [1, 2, 3, 4, 5, 2]
# print(list)
# print(sum(list[1::2]))


# 2 Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

# list = [2, 3, 4, 5, 6]
# def mult_numbes(numbers):
#     results = []
#     while len(numbers) >1:
#         results.append(numbers[0] * numbers[-1])
#         del  numbers[0]
#         del numbers[-1]
#     if len(numbers) == 1: results.append(numbers[0]**2)
#     return results
# print(mult_numbes(list))

# 3 В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [1.1, 1.2, 3.1, 5, 10.01]
# list1 = []
#
# for i in list:
#     if i % 1:
#         remainder = round(i - int(i), 2)
#         list1.append(remainder)
# print(list)
# for j in list1:
#     max_elem = max(list1)
#     min_elem = min(list1)
# print(max_elem - min_elem)

# 4 Написать программу преобразования десятичного числа в двоичное

# number = int(input('Enter number: '))
# number = bin(number)
# print(number)

