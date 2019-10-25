def updateList(numList):
    numList += [10] #add a new element to the list
    
def updateNum(n):
    print("update Num {:d}".format(id(n)))
    n += 10
     
n = [1, 2]
print(id(n))

                 
updateList(n)
print(n)
print(id(n))

b = 5
print(id(b))
updateNum(b)
print(b)

