# diplay loanley integrs in strings

s=str(input())

for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if s[i]==s[j]:
            c+=1
    if c==1:
        print(s[i])
        


#insert items into list dynamically and then re range the list numbers so that first 
# num is max and next is min next is max and so on...

l=[]
n=int(input())
#appedning ino list according to length 
for i in range(n):
    l.append(int(input()))
#print(l)
#sorting (bubble)
for i in range(n):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
#print(l)
i=0
j=len(l)-1
while i<len(l):
    l.insert(i,l.pop(j))
    i+=2
print(l)





# function to  remove duplicates and then arrange in ascending order

l=list(map(int,input().split()))
i=0
while i<len(l):
    j=i+1
    while j<len(l):
        if l[i]==l[j]:
            l.pop(j)
        else:
            j+=1
    i+=1    
# print(l)
l.sort()
print(l)


# function to  remove duplicates and then arrange in ascending order

l=list(map(int,input().split()))
for i in l:
    if l.count(i)>1:
        l.remove(i)
l.sort()
print(l)

# find if sum of all last digits is divisible by 10 

n=int(input('enter length: '))
l=[]
s=0
for i in range(n):
    l.append(int(input()))
for i in l:
    t=0
    t=i%10
    s=s*10+t
print('sum is: ',s)
if s%10==0:
    print('YES')
else:
    print('NO')
