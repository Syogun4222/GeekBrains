# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.
#
#
# count = {}
# for i in range(2, 100):
#     for j in range(2, 10):
#         if i % j == 0:
#             count[j] = count.get(j, 0) + 1
#
# for k, v in count.items():
#     print(k, '-', v)


# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив
# надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается
# с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
#
# from random import randint
#
# source = [randint(0, randint(0, 10)) for _ in range(randint(2, 10))]
# even_indexes = [i for i, n in enumerate(source) if not n % 2]
#
# print(f'source list:\t\t\t\t{source}')
# print(f'indexes of even elements:\t{even_indexes}')

#
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
#
#
# from random import randint, shuffle
#
# source = [i for i in range(0, randint(2, 10))]
# shuffle(source)
# print(f'source list:\t{source}')
#
# max_i = min_i = 0
# max_n = min_n = source[0]
#
# for i, n in enumerate(source):
#     if n > max_n:
#         max_n = n
#         max_i = i
#     if n < min_n:
#         min_n = n
#         min_i = i
#
# source[max_i], source[min_i] = source[min_i], source[max_i]
# print(f'result list:\t{source}')

#
# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный»
# и «максимальный отрицательный». Это два абсолютно разных значения.
#
#
# from random import randint
#
# source = [randint(randint(-10, 0), randint(0, 10)) for _ in range(randint(5, 15))]
# print(f'source list: {source}')
#
# negatives = [s for s in source if s < 0]
# if not negatives:
#     print('There are no negative numbers in source list')
#
# else:
#     max_n = negatives[0]
#     max_i = source.index(max_n)
#
#     for i, n in enumerate(source):
#         if max_n < n < 0:
#             max_n = n
#             max_i = i
#
#     print(f'max negative = {max_n} with index = {max_i}')