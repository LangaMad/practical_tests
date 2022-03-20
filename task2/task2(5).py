# numbers=[1,45,65,34,1,23,99]
# print(min(numbers))
# print(max(numbers))
# sorted(numbers)
# numbers[0]=max(numbers)
# numbers[-1]=min(numbers)
# print(numbers)
#Решение №2
numbers=[2,45,65,34,1,23,99]
max_num=numbers.index(max(numbers))
min_num=numbers.index(min(numbers))
numbers[min_num],numbers[max_num]=numbers[max_num],numbers[min_num]
print(numbers)


