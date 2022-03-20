weight = int(input("Введте свой вес: "))
moon_weight = weight * 0.165

n = 0.165
for n in range(15):
    weight +=1
    moon_weight = weight * 0.165
    x = range(15)
    print("Ваш вес на",x,"день",moon_weight)

