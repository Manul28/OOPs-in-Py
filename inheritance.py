#Fundamental features of oop:-
#-> Inheritance
#-> Polymorphism
#-> Encapsulation
#this is your base class
class animal:
    def eating(self)->None:
        print("eating")

#this is your derived class        
class dog(animal):
    def eating(self)->None:
        print("eating")
    def bark(self)->None:
        print("dog")
d=dog()        
d.eating()
d.bark()                 

