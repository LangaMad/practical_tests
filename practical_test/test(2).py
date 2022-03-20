


def get_seasons(m):
    if m in (12,1,2):
        print('Весна')
    elif m in (3,4,5):
        print("Лето")
    elif m in (6,7,8):
        print("Осень")
    elif m in (9,10,11):
        print("Зима")
    else:
        print("Такого месяца нет")
    return m

print(get_seasons(8))