#5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

my_list = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п",
           "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
a = int(input("Введите номер буквы:  "))
a = a + 1
print(my_list[a])

