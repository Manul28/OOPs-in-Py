#this is base class
class animal:
    def editing(self)->None:
        print("Doing!!")
#this is derived class for class animal and this is base class for class cat        
class dog(animal):
    def printing(self)->None:
        print("Barking")
#this is the main derived class      
class cat(dog):
    def feeding(self)->None:
        print("leading") 
        
c=cat()
c.editing() 
c.printing()
c.feeding()                      