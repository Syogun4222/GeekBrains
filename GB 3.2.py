def personal_data (name = input("name: "),
                    surname = input("surname:  "),
                    year = int(input("year =  ")),
                    city = input("city:  "),
                    email = input("email:  "),
                    telephone = input("telephone:  ")):
    return [name, surname, year, city, email, telephone]
#    data_dickt = {name: name, surname: surname, year: year, city: city, email: email, telephone: telephone}
#    return {name: name, surname: surname, year: year, city: city, email: email, telephone: telephone}
# По заданию все сделал, но хотел перевести в словарь и получить значение "по ключу" но что-то не вышло, если возможно -объясните, пожалуста, как.




print(personal_data())
