class Student:

    def __init__(self, Name, Id):                   # Constructer

        self.name = Name
        self.StID = Id

    def info(self):

        print(f"Student ID: {self.StID}\nStudent Name: {self.name}")


student1 = Student("Saifullah", 1)                  #   These 
student2 = Student("Murtaza", 2)                    #   are
student3 = Student("Jawad", 3)                      #   instances and objects of class Student.

student1.info()
student2.info()
student3.info()
