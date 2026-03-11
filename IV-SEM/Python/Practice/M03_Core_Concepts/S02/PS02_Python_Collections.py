'''
Sets:

a = set([10,20,30,40,50]) #hash(value%5)
print(a)
a.add(78)
a.add(50)
print(a)
a.remove(20)
print(a)
a.discard(30)
print(a)
b = set([20,30,40,70,80])
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
'''

#Accessing of tuple:
t = (1,2,3,45,50)
t[0] = 10 
print(t[0])

#Concatination of tuple:
t = (1,2,3,45,50)
t2 = (2,3,547,8)       
print(t+t2)    
#Repetition of tuples
t = (1,2,3,45,50) 
print(t*3)

#Creation ({},dict())
d = {"name":"spoo",'age':23}