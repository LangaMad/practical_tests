class Airplane():
    def __init__(self) -> None:
        self.mark = "BMW"
        self.model = "y-183"
        self.year = 10
        self.max_speed = 0
        self.odmetr = 0
        self.is_flying = False

    def take_off(self):
        if self.is_flying == False:
            self.is_flying == True
            print("Саолет взлетает")
        else:
            print("Самолет уже в воздухе")
 
    def fly(self):

        if self.is_flying == True:
            print("Самолет летает")
            t = int(input("Введите премя полета: "))
            v = int(input("Введите скорость полета: "))
            s = v * t
            self.odmetr = s
            
        else:
            print("Самолет еще е взлетел")

    def land(self):
        if self.is_flying == True:
            self.is_flying == False
            print("Самолет приземлился")
        else:
            print("Самолет уже приземлился")


Fly = Airplane()

Fly.take_off()
Fly.fly()
Fly.land()