#Polymorphism: different type respond to the same function

#Static method: a function that not depends on the class instance but related to the class

class Animal: #abstract class
    
    def name(self):
        self.name = 'hi'
        
    def sound(self): #abstract method must be implemented by child class
        raise NotImplemetedError('Subclass must implement abstract method')
        #or pass

class Bear(Animal):
    def sound(self):
        print('Groarrr')

class Wolf(Animal):
    def sound(self):
        print('Woof woof!')
        
class Sheep(Animal):
    sheepName = 'Alice'

    def sound(self):
        print('Baa')
        
    @staticmethod #just indication, not much useful
    def sheepAddition(x,y):
        return x + y
    
    @classmethod #class method use instance in the class as parameter
    def sheepName(cls):
        print(cls.sheepName)
        
#    @staticmethod
#    def sheepName()
#        print(cls.sheepName)
        
        
#animals = [Bear(), Wolf(), Sheep()]
#
#for animal in animals:
#    animal.sound()
#
sheep = Sheep()

print(sheep.sheepAddition(10, 11))


#What is the difference between interface and abstract class?
#Abstract class: inheritance, define behaviour
#interface: also abstract but looks like shell/scope

