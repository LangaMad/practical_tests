age = int(input("Введите ваш возраст: "))

for num in range(age):
    if age % 2 == 0:
        numbers = list(range(0,age+2,2))
    elif age % 2 != 0:
        numbers = list(range(1,age+2,2))

# for number in numbers:
#     print(number)

    

print([0]+numbers)     #.join