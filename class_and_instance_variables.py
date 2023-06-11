# Their are two types of variable 
#-> Instance variable
#-> class variable
class student:
    college='xyz' # class variable
    #this is the initial function
    def __init__(self,rollno,name) -> None:
        self.rollno=rollno
        self.name=name
    # this is the display function
    def display(self):
           print("Student name:",self.name)
           print("Student rollno:",self.rollno)
           print("College ID:",student.college)
student1=student('xyz001',"manul")
student1.display()

class person:
    # we can avoid this myself parameter by using staticmethod
    @staticmethod
    # def display(myself):
    def display():
           print("Hello")
p=person()
p.display()           
           