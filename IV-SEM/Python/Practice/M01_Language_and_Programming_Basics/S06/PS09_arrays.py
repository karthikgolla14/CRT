'''
Numpy-->Numerical Python

'''
import numpy as np 
arr = np.array([1,2,3,4,5])
print("Array elements are:", arr)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.sum(arr))
print(np.zeros(5))
print(np.ones(9))
print("Even numbers are:",np.arange(2,10,2))
print("Odd numbers are:",np.arange(1,10,2))

n = int(input("enter the size:"))
ele = list(map(int,input("Enter the elements:").split()))
print("Array elements are:", np.array(ele))