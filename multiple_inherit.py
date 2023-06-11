#this is the base class
class father:
    def office(self):
        print("Office")
        
class mother:
    def home(self):
        print("Home")

class child(father,mother):
    pass

c=child()
c.office()
c.home()               