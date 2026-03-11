import array
arr = array.array('i', [])
print(arr, type(arr))
arr.append(10)
arr.append(20)
arr.append(30)
print(arr)
arr.append(12.45)

li = [12,25.4,6+5j,"Hello"]
print(li[::-1])
print(len(li))
li.append(100)
print(li)
print(li.count(25.4))
li.insert(2,"World")
print(li)
li.insert(-20,"python")
print(li)


"""read a number and count the no of digits from a number using array input : 1234 , output : 4"""

