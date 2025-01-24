##to print pattern 
def printed(n):
    if n==1:
        print('*')
        return 
    print('*' *n)
    for i in range(n-2):
        print('*' +' '*(n-2)+'*')
    print('*' *n)
i=int(input())
printed(i)

n=int(input())
for i in range (1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()


n=int(input())
for i in range (1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()


n= int(input())
for i in range (1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()


n= int(input())
for i in range (1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

n= int(input())
for i in range(1,n+1):
    print("  "*(n-i),end='')
    for j in range(1,i+1):
        print(j,end=" ")
    print()


n= int(input())
for i in range(1,n+1):
    print("  "*(n-i),end='')
    for j in range(1,i+1):
        print(i,end=" ")
    print()


n= int(input())
for i in range(1,n+1):
    print("  "*(n-i),end='')
    for j in range(1,i+1):
        print(j,end=" ")
    print()



n= int(input())
for i in range(1,n+1):
    print("  "*(n-i),end='')
    for j in range(i+1,1,-1):
        print(i,end=" ")
    print()


n= int(input())
for i in range(1,n+1):
    print("  "*(n-i),end='')
    for j in range(i+1,1,-1):
        print(j-1,end=" ")
    print()
