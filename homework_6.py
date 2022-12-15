# 1- Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3


# test_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# print(f"список: {test_list}")
# test_item = input("Введите искомую строку: ")


# def check_list(test_list, test_item):
#     count = 0
#     for i in range(len(test_list)):
#         if test_list[i] == test_item:
#             count += 1
#             if count == 2:
#                 return i
#     else:
#         return -1


# print(f"ответ: {check_list(test_list, test_item)}")

# 2- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from random import randint

# number = int(input('Введите размер списка '))
# list = []
# list2 = []

# for i in range(number):
#     list.append(randint(0, 9))

# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1

# print(list)
# print(list2)

# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# from random import randint

# def get_degree(n):
#     return [((-3)**i) for i in range(n)]

# n = randint(1, 10)

# print (get_degree(n))