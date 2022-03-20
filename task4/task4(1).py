
with open('class.txt',"r", encoding ="utf-8" ) as file:
    three_less = list()
    result = 0
    for students in  file:
        if "1" in students:
            three_less.append(students) 
            result +=1   
        elif "2" in students:
            three_less.append(students)
            result +=2
        elif "3" in students:
            three_less.append(students)
            result +=3 
        elif "5" in students:
            result+=5
        elif "4" in students:
            result+=4
        print(result)
        # if (1,2,3,4,5,6,7,8,9,0) in students:
get_result = result/11
print(three_less)
print(get_result)
            