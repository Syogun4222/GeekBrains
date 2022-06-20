#1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.

def simple_calc(x, act, y):
    if act == '+':
        return x + y
    if act == '-':
        return x - y
    if act == '*':
        return x * y
    if act == '/':
        if y == 0:
            return f'Невозможно разделить {x} на {y}'
        return x / y
    return f'Неизвестная операция "{act}"'


print('Введите в одной строке через пробел первое число, операцию и второе число.')
print('Допустимые символы операций: +, -, *, /. Ноль вместо знака операции - завершить программу.')
print('Для завершения работы программы введите ноль вместо знака операции.')

operand = None
while True:
    a, operand, b = input('> ').split()
    if operand == '0':
        print('Работа завершена.')
        break
    print(simple_calc(int(a), operand, int(b)))