# to print chars

n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(96+j),end=' ')
    print()
    
# a 
# a b 
# a b c 
# a b c d 
# a b c d e 

#print patterns of numbers
n= int(input())
c=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print("%2d"%(c),end=' ')
        c+=1
    print()

#  1 
#  2  3 
#  4  5  6 
#  7  8  9 10 
# 11 12 13 14 15 

#print column wise
n= int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i+(j-1)*n,end=' ')
    print()

# 1 6 11 16 21 
# 2 7 12 17 22 
# 3 8 13 18 23 
# 4 9 14 19 24 
# 5 10 15 20 25 

##print odd or even of n numbers using list 
numbers = list(map(eval, input().split()))

for num in numbers:
    if num % 2 != 0:
        print('odd '+str(num))
    else:
        print('even '+str(num))


##check if given number is even or odd
n=int(input('enter the number'))
if n%2==0:
    print('even')
else:
    print('odd')



##check which is greatest among the three 

a, b, c = map(int, input("Enter three values: ").split())
if a > b and a > c:
    print('Greatest is ' + str(a))  
elif b > c:
    print('Greatest is ' + str(b))  
else:
    print('Greatest is ' + str(c))


numbers = list(map(int,input().split()))

for num in numbers:
    if num % 2 == 0:
        print(str(num)+' is even')
    else:
        print(str(num)+' is odd ')


def isprime(num):
    f=True
    if num<=1:
        f=False
    for i in range(2,num):
        if num%i==0:
            f=False
            break
    if f:
        print('prime')
    else:
        print('not prime')
isprime(6)

# mirror pattern base
n= int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1:
            print('*',end=" ")
        else:
            print(' ',end=' ')
    print()
# * * * * * 
# *         
# *         
# *         
# * * * * * 


n= int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1:
            print('*',end=" ")
        else:
            print(' ',end=' ')
    for j in range(n-1,0,-1):
        if i==1 or j==1:
            print('*',end=" ")
        else:
            print(' ',end=' ')
    print()
for i in range(n-1,0,-1):
    for j in range(1,n+1):
        if i==1 or j==1:
            print('*',end=" ")
        else:
            print(' ',end=' ')
    for j in range(n-1,0,-1):
        if i==1 or i==n or j==1:
            print('*',end=" ")
        else:
            print(' ',end=' ')
    print()

# * * * * * * * * * 
# *               * 
# *               * 
# *               * 
# *               * 
# *               * 
# *               * 
# *               * 
# * * * * * * * * *

#inverse pyramid of numbers 
n= int(input())
for i in range(1,n+1):
    print('  '*(i),end='')
    for j in range(1,n-i+1):
        print(j,end=' ')
    for j in range(n+1-i,0,-1):
        print(j,end=' ')
    print()
  # 1 2 3 4 5 4 3 2 1 
  #   1 2 3 4 3 2 1 
  #     1 2 3 2 1 
  #       1 2 1 
  #         1 

n= int(input())
for i in range(1,n+1):
    print('  '*(i),end='')
    for j in range(1,n-i+1):
        print(j,end=' ')
    for j in range(n+1-i,0,-1):
        print(j,end=' ')
    print()
for i in range(n-1,0,-1):
    print('  '*(i),end='')
    for j in range(1,n-i+1):
        print(j,end=' ')
    for j in range(n+1-i,0,-1):
        print(j,end=' ')
    print()
  # 1 2 3 4 5 4 3 2 1 
  #   1 2 3 4 3 2 1 
  #     1 2 3 2 1 
  #       1 2 1 
  #         1 
  #       1 2 1 
  #     1 2 3 2 1 
  #   1 2 3 4 3 2 1 
  # 1 2 3 4 5 4 3 2 1


#armstrong number

n= int(input())
t=n  # temporary 
l=0  # length 
while t!=0:
    l=l+1
    t=t//10
#print(l)
t=n     #1234
s=0
while t!=0:
    d=t%10
    s=s+d**l   #(1**4+2**4+3**4+4**4)
    t=t//10
if s==n:
    print('armstrong number')
else:
    print('not')
