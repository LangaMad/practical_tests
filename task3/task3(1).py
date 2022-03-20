print("Введите наименьшее время ")
hour = int(input("Введите часы: "))
minute = int(input("Введите минуты: "))
second = int(input("Введите секунды: "))


if hour > 24:
    print("impossible")
    exit()
elif minute > 60:
    print("impossible")
    exit()
elif second > 60:
    print("impossible")
    exit()
print(hour,':',minute,":",second)


print("Введите ниабольшее время ")
hour2 = int(input("Введите часы: "))
minute2 = int(input("Введите минуты: "))
second2 = int(input("Введите секунды: "))


if hour2 > 24:
    print("impossible")
    exit()
elif minute2 > 60:
    print("impossible")
    exit()
elif second2 > 60:
    print("impossible")
    exit()
print(hour2,':',minute2,":",second2)


n = hour*60*60
n2 = minute*60
a = hour2*60*60
a2 = minute*60
x = (a + a2 + second2) - (n + n2 + second)
print("Разница в секундах:" , x, 'Cекунд')