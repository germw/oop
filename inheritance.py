#Encapsulation: restrict access to methods and variable to prevent being modified by accident

class Father(object):  #superclass
    surname = 'Wong'
    location = 'Sai Ying Pun'
    
    #protected variable  single underscore, available to subclass
    _property = 500;
    
    #private varaible of this class, double underscore, only accessible in this class
    __wife = 'Mary'
    
    def __init__(self, name):
        self.name = name
    
    def printProfile(self):
        print('My name is {} {}.\nMy wife is {}.\nI live in {}.\nI got {:d} dollar.\n'.format(self.name, self.surname, self.__wife, self.location, self._property))
        
    def printIntro(self):
        print('I am father')
        
    def __printHobby(self):
        print('I like swimming')
        

#the class inside () define which class is this class inherit from
class Son(Father):  #subclass
    __wife = 'Rose'
    
    def __init__(self, name):
        self.name = name
#method overriding
    def printIntro(self):
        print('I am son')



myFather = Father('Steven')
Me = Son('Stevenson')
#
#
#myFather.printProfile()
#Me.printProfile()

#but you can still access and modify protected instance, programmer responsibility not to change it outside its class
#print(myFather._property)
#myFather._property = 1000
#print(myFather._property)

#myFather.__printHobby()
#print(myFather._wife)
#retrieve private data in a class
#print(myFather._Father__wife)

#myFather.printIntro()
#Me.printIntro()

#isinstance vs type
#isinstance(object, type) return True if the specified object is of the specified type, otherwise, False

print(type(myFather) == Father) #t
print(type(Me) == Father) #f
print(type(myFather) == Son) #f
print(type(Me) == Son) #t
print()
print(isinstance(myFather,Father)) #t
print(isinstance(Me,Father)) #f
print(isinstance(myFather,Son)) #f
print(isinstance(Me,Son)) #t
