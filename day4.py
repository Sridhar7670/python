# find if elemnet exists or not 

l= list(map(int,input().split()))
k= int(input())
for i in range(len(l)):
    if l[i]==k:
        print(l[i])
        break
else:
    print('not found')

# find max , min in a list
l= list(map(int,input('enter list items ').split()))
min=max=l[0]
for i in l:
    if i<min:
        min=i
    elif i>max:
        max=i
print('max is: ',max,'min is: ',min)

# find sum of all numbers in list 

l=list(map(int,input('enter listr values').split()))
s=0
for i in l:
    s+=i
print('sum is ',s)