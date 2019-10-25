class Rectangle(object):
    name = 'rectangle'   #instance/attribute: values of given class ot type
                         #class/static variable
    #parameterized constructor, only one constructor in a class
    #method overloading: multiple ways to call the method
    def __init__(self, w=None, l=None):
        if w is not None:
            self.width = w  #instance
        else:
            self.width = 20
        if l is not None:
            self.length = l
        else:
            self.length = 20
        
    
    #methods inside a class/type
    def setLength(self, length):
        self.length = length
    
    def printLengthWidth(self):
        print('Width = {:d} Length = {:d}'.format(self.width,self.length))
    
    

def main():
    print("Hello World!")
    #create object/instance
    r1 = Rectangle(10,20)
    r2 = Rectangle(20,30)
    r3 = Rectangle()
    
    r3.name = 'rect'
    print(r3.name)

    #run the method inside the class
    r1.printLengthWidth()
    r2.printLengthWidth()
    r3.printLengthWidth()

if __name__ == "__main__":
    main()
