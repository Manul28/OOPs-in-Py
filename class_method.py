class person:
    def display(self):
        print("hello")
person1=person()
person1.display()        
        
        
class student:
    # syntax of initial function
    # __init__ to initial a method
    #here self refer to the current object
    def __init__(self,name):
        self.name=name
        name="john"
        print(name)
    def display(self):
        print("hello",self.name) 

student1=student("MANUL")
student1.display()              
# instead of the above two lines we can write
student("manul").display()        
