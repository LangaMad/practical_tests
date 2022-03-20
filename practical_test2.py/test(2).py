class Math():
    def __init__(self) -> None:
        self.a = 0
        self.b = 0
        self.c = 0

    def addition(self,q,w):
        self.a = q
        self.b = w
        x = q + w 
        print("Результат: " ,x)

    def multi(self,a,b):
       self.a = a
       self.b = b
       x = a * b
       print("Результат: " ,x)

    def division(self,a,b):
        self.a = a
        self.b = b
        if b == 0:
            print("Eror")
            exit()
        else:
            x = a / b
            print("Результат: " ,x)
        
    def sub(self,q,w):
        self.a = q
        self.b = w
        x = q - w 
        print("Результат: " ,x)

math = Math()

math.addition(1,5)

