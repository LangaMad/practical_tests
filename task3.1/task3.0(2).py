kids = int(input("Введите количество детей: "))
apples = int(input("Введите количество яблок: "))
for_kids = apples//kids
for_appeles = apples%kids
print(f"Каждый стдент получит {for_kids} яблок(о)")
print(f"Осталось яблок в корзине {for_appeles}")

