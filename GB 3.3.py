def s_two_numbers (numbers_1, numbers_2, numbers_3):
   a = [numbers_1, numbers_2, numbers_3]
   a.remove(min(a))
   return sum(a)




numbers_1 = int(input("1"))
numbers_2 = int(input("2"))
numbers_3 = int(input("3"))
print(s_two_numbers(numbers_1, numbers_2, numbers_3))