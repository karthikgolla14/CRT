'''
Armstrong number:
input : 153 
output: Armstrong number 
input : 24 
output: not an Armstron number

'''
'''
n = int(input())
count = len(str(n))
s = 0 
for digit in str(n):
    s += int(digit) ** count 
    
print("Armstrong number" if s == n else "not an Armstrong number")
'''

'''
Perfect Number
input: 6
output: perfect number

n = int(input())
d_sum = 0 
for i in range(1,n):
    if n % i == 0:
        d_sum += i 
if d_sum == n:
    print("perfect number")
else:
    print("Not perfect number")
'''
'''
Strong Number
input : 123 
output: not a strog number

Explanation : 1! + 2! + 3! = 1 + 2 + 6 = 9
'''
def factorial(n):
    if n < 0:
        return " no factorial for -ve"
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1,n+1):
            fact = fact * i 
        return fact 
n = int(input())
s = 0
for digit in str(n):
    s += factorial(int(digit))
print("stong number" if sum == n else "not a strong number")
        
