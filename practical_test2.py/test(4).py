class Product():
    def __init__(self,name,price,sat_count) -> None:
        self.name = name
        self.price = price
        self.sat_count = sat_count

product = Product("Суп",300,50)



class Person():
    def __init__(self,name,cash) -> None:
        self.name  = name
        self.__cash = cash
        self._debt = 0
        self.satiety = 200
        self.salary = 1000

    def work(self):
        self.__cash += self.salary
        self.satiety -= 40
        print(f"У вас теперь {self.__cash} ")
       

    def get_cash_status(self):
        return self.__cash

    def get_debt(self,sum):
        self._debt +=sum
        self.__cash +=sum
        

    def get_debt_status(self):
        print(f"У вас долг в {self._debt} сом")
        if self._debt > self.__cash:
            print("Банкрот")

    def get_sariety(self):
        print(f"У вас теперь {self.satiety} сытости ")
        if self.satiety <= 20:
            print("Если голод упадет ниже 0 вы умрете ")
        elif self.satiety <= 0 :
            print("Вы умерли")
   
   
   
    def buy_and_eat(self,product):
        if isinstance(product,Product):
            if self.__cash < product.price:
                print("у вас недостатчно средств")
            else:
                self.__cash -= product.price
                self.satiety += product.sat_count

person = Person("Den",10000)

person.buy_and_eat(product)
    


