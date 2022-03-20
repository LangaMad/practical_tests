

def get_colculator(num1,num2,element):
    if element == "+":
        x = num1 + num2
    elif element == "-":
        x = num1 - num2
    elif element == "*":
        x = num1 * num2
    elif num2 == 0:
        print("Это невозможно")
        exit()
    elif element == "/":
        x = num1 / num2
    return x

print(get_colculator(11,0,"/"))









