# to print chars

n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(96+j),end=' ')
    print()

#print patterns of numbers
n= int(input())
c=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print("%2d"%(c),end=' ')
        c+=1
    print()


#print column wise
n= int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i+(j-1)*n,end=' ')
    print()