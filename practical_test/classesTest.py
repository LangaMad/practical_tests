class Human():
    def __init__(self,name,age,job,cash) -> None:
        self.name = name
        self.age = age
        self.job = job
        self.cash = cash
        self.__my_houses = []
        

    def earn_money(self,sum):
        self.cash += sum
        print(f"У вас теперь {self.cash} ")

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Job: {self.job}")
        print(f"Cash: {self.cash}")

    def pay(self,sum):
        if sum <= self.cash:
            self.cash -= sum 
            print(f"{self.cash} осталось ")
        else:
            print(f"У вас недостаточно денег, У вас только {self.cash}")

    def add_my_house(self,house):
        if isinstance(house,House):
            if house not in self.__my_houses:
                self.__my_houses.append(house)
                
            
        else:
            print('it is not house')

    def get_info_houses(self,house):
        s = []
        for house in self.__my_houses:
            if isinstance(house,House):
                s.append(house.sqare)
                s.append(house.rooms)
                print(self.__my_houses)
        else:
            print("Your houses")


class House():
    def __init__(self,price,sqare,rooms) -> None:
        self.price = price
        self.sqare = sqare
        self.rooms = rooms
        self._owner = None
        

    





    def new_owner(self,richman):
        if isinstance(richman,Human) and self.price <= richman.cash:
            
            self._owner = richman.name
            richman.add_my_house(self)
            print(self._owner)
        else:
            print("Its not owner")
    
    def dicacount_and_buy(self, client):
        if isinstance(client,Human):
            if client.age >= 60:
                new_price = (self.price*15)//100
                client.cash > new_price 
                
                print("Покупка заверщена")
            else:
                client.cash > self.price
                print("Покупка заверщена")
                client.pay(sum = self.price)
            
        else:
            print("Не хватет средст на счету")




    
h = Human("sfas",22,"dds",500000)
hh = House(30000,"100m**2",5)

# print(hh.new_owner(h))

h.get_info_houses(hh)
hh.dicacount_and_buy(h)






