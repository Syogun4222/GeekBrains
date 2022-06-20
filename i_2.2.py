#2. Посчитать четные и нечетные цифры введенного натурального числа.

n = int(input('Введите натуральное число: '))
even = odd = 0

while True:
    dig = n % 10

    if dig % 2:
        odd += 1
    else:
        even += 1

    n //= 10
    if not n:
        break

print(f'В этом числе чётных цифр: {even}, нечётных: {odd}.')
