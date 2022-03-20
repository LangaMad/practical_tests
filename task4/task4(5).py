


name = input("Здравствуйте , если хотите отправить жалобу напишите *жалоба*  : ")
if name == "жалоба":
    print("Выберите город : Москва,Париж,Сан-Франциско,Торонто")
    city = input("Введите город с заглавной буквы: ")
    if city == "Москва":
        complaint1 = input("Введите жалобу: ")
        with open('get_moscow.txt',"a", encoding ="utf-8" ) as file:
            file.write(f" Ваша жалоба : {complaint1} \n")
    elif city == "Париж":
        complaint1 = input("Введите жалобу: ")
        with open('get_paris.txt',"a", encoding ="utf-8" ) as file:
            file.write(f" Ваша жалоба : {complaint1} \n")
    elif city == "Сан-Франциско":
        complaint1 = input("Введите жалобу: ")
        with open('get_san-francisco.txt',"a", encoding ="utf-8" ) as file:
            file.write(f" Ваша жалоба : {complaint1} \n")
    elif city == "Торонто":
        complaint1 = input("Введите жалобу: ")
        with open('get_toronto.txt',"a", encoding ="utf-8" ) as file:
            file.write(f" Ваша жалоба : {complaint1} \n")
    else:
        print("Вы не правльно ввели город")
else:
    print("Спасибо что не жалуетесь))")