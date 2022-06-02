my_list = []
while True:
    add_lin = input("enter:  ")
    my_list.append(add_lin + "\n")
    if add_lin == "":
        exit()
    with open("text.txt", "w") as new_text:
       new_text.writelines(my_list)
