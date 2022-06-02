my_list = ["one", "two", "3"]
print(my_list)
with open("text.txt", "w+") as new_file:
    new_file.writelines(my_list)
    new_file.read(10)
    print(new_file.tell())
