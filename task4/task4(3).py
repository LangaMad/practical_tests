from os import name



    
active = True 
while active:
    with open('book1.txt',"a", encoding ="utf-8" ) as file:
        # file.writelines("Здравствуйте , как поживаете? ")
        name2 = input("Введите совое имя и фамилие: ")
        if name2 == "exit":
            active = False
        else:
            print(f"Для выxода введите exit ")
            
            file.write(f"Здравствуйте {name2}, как поживаете? \n")




            
            
