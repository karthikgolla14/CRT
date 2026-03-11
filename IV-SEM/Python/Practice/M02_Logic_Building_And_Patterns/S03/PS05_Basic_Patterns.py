'''

n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end = " ")
    print()

   
n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end = "")
    print()


n = 4
A
A B 
A B C 
A B C D

N = 4
1 
2 3
4 5 6
7 8 9 10

N = 4

* * * *
*     *
*     *
* * * *

STAIR CASE 
IN 
Hacker RANK


n = int(input())
for i in range(n):
    for j in range(n):
        print('*',end = ' ')
    print()

n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print('*' , end = ' ')
    print()


n = int(input())
for i in range(n,0,-1):
    for j in range(i):
         print('*' , end = ' ')
    print()


n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j , end = ' ')
    print()

n = int(input())
num = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num , end = ' ')
        num += 1
    print()

n = int(input())
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j== 0 or j == n-1:
            print('*',end = ' ')
        else:
            print(' ',end= ' ')
    print()        
'''