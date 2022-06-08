firm = {"Ivanov" : 23543.12, "Petrov" : 13749.32}
try:
    file_obj = open("text.txt", "w")
    for last_name, salary in firm.items():
        file_obj.write(last_name + ":" + str(salary) + "\n")
except IOError:
    print("Error")
finally:
    file_obj.close()
summa = 0
count = 0
persans = []
with open("text.txt", 'r') as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(":")
        if int(tokens[1]) <= 20000:
            persans.append(tokens[0])
        summa += int(tokens[1])
        count += 1
reslt = summa/count
print(f"persons {persans}")
print(f"averate: {reslt}")