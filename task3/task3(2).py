n = [1,2,3,4,5,67,89,90,98,76]
n2 = [1,2,3,4,5,12,34,56,54,32]
for num in n:
    if not num in n2:
        print(num)
