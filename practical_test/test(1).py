
def get_long_line():
    with open("HelloWorld.txt", "r", encoding="utf-8" ) as file:
        for long in file.readlines():
            # print(long)
            line = long
            i = len(line)
            print(max(i))
            #с помошью len найти самый большую строку и вывести ее на экран 
            


get_long_line()
