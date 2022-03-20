class Student():
    def __init__(self) -> None:
        self.name = "Ivan"
        self.age = 18
        self.groupNum = "10A"

    def get_name(self):
         return self.name

    def get_age(self):
        return self.age

    def get_group(self):
        if self.name == "Ivan":
            return self.groupNum

    def info1(self):
        print(self.name)
        print(self.age)
        print(self.groupNum)

    def set_name_age(self):
        new_name = input("Введите новое имя: ")
        new_age = input("Введите новый возраст: ")
        self.name = new_name
        self.age = new_age
        return self.name, self.age
        
    def set_group(self):
        new_group = input("Введите новую группу: ")
        self.groupNum = new_group
        return self.groupNum

    def info2(self):
        print(self.name)
        print(self.age)
        print(self.groupNum)
        

new_student = Student()
new_student2 = Student()
new_student.info1()
new_student.set_name_age()
new_student.set_group()
new_student.info2()
new_student2.info1()
new_student2.set_name_age()
new_student2.set_group()
new_student2.info2()


