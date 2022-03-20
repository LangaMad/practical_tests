from math import ceil
a_class = int(input("Введите а класс: "))
b_class = int(input("Введите b класс: "))
c_class = int(input("Введите с класс: "))

for_a_class = a_class/2
for_b_class = b_class/2
for_c_class = c_class/2
result = ceil(for_c_class) + ceil(for_b_class) + ceil(for_a_class)

def get_for_class(num,class_):

    print(f"{ceil(num)} Нужно стульев для {class_} класса")


get_for_class(for_a_class,"a")
get_for_class(for_b_class,"b")
get_for_class(for_c_class,"c")
print(result)
