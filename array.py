import numpy as np

tuple_names = ('Chris', 'Alex', 'Racheal')
list_names = ['Chris', 'Alex', 'Racheal']
array_num = np.array( [1, 2, 3])


print(tuple_names)
print(list_names)
print(array_num)

#print(type(tuple_names))
#print(type(list_names))
#print(type(array_num))


#mutable/immutable
#tuple_names[0] = 'Sam'
#print(tuple_names)

#list_names[0] = 'Sam'
#print(list_names)

#Reuse/copy
#CopyTuple = tuple(tuple_names)
#print(id(tuple_names))
#print(id(CopyTuple))
#
#CopyList = list(list_names)
#print(id(list_names))
#print(id(CopyList))

#Size Different
#print(tuple_names.__sizeof__())
#print(list_names.__sizeof__())

#add element
#list_names.insert(2, "Mary")
#print(list_names)
