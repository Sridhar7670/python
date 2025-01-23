# add all the digits in a number 
n=int(input())
s=0
while n!=0:
    s+=n%10
    n=n//10
print(s)


#print first n numbers in reverse order 
n=int(input())
while n>1:
    print(n ,end=" ")
    n-=1

#sum of first 100 numbers 
s=0
n=1
while n<=100:
    s+=n
    n=n+1
print(s)    


#print all even numbers under 50

n=int(input())
while n>0:
    n-=1
    if n%2==0:
        print(n,end=' ')


# muliplication table 
n=int(input())
i=1
while i<=10:
   # print(f'{n}* {i}={n*i}')
    print(n,'*',i,'=',n*i)
    i+=1

#find prime using for else
n=int(input())

if n<=1:
        print(False)
else:  
    for i in range(2,n):
        if n%i==0:
            print(False)
            break
    else:
        print(True)
        


#find common elements in two lists

a=[5,6,9,78,56]
b=[6,4,3,2,9]
l=[]
for i in a:
    if i in b:
        l.append(i)
print(l)

# enter only desired length into the list 
a=[]
n=int(input('enter number of items'))

for i in range(n):
    t=int(input())
    a.append(t)
print(a)

# enter all the values into list at once using map 
a=list(map(int,input().split()))
print(a)

#apped into list using map 
a=[]
n=int(input('enter number of items'))
a=list(map(int,input().split()))
print(a)

# fibonacci sequence 

n=int(input())
a,b=-1,1
for i in range(n):
    next_n=a+b
    a=b
    b=next_n
    print(next_n)

