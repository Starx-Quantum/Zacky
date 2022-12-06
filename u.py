class Student:
        def __init__(self, name, age, phone_no):
            self.name = name
            self.__age = age
            self.__phone_no = phone_no
            print(self.name,end=' ')
        def get_name(self):
            return self.__name
        def tell(self):
                print(self.name, self.age)
class Teacher(Student):
        def __init__(self, name, age, id):
                Student.__init__(self, name, age,id)
                super().__init__(name,age, phone_no)
                self.id = id
                print('9HQNIVJ',end=' ')
                print (self.name,end=' ')
        def details(self):
            Student.name(self)
            self.id(self)
            self.age(Student)
            print('Bob',end=' ')
        def tell(self):
                Student.tell(self)
                print (self.id,end=' ')
                print('Bob',end=' ')
                self.details(Student)
        def details(self):
            pass
class HeadMaster(Student):
        def __init__(self, name, age, marks):
                Student.__init__(self, name, age)
                self.marks = marks
                print (self.name,end=' ')
        def details(self):
            Student.name(self)
            pass
        def tell(self):
                Student.tell(self)
                print (self.marks,end=' ')
        def Student(self):
            pass
class Teacher(Student):
    pass
t=Teacher('Alice',45,'QAO86W2H')