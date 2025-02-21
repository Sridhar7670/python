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


# extract all the possible numbers from the string and form largest even number else print(-1)
s=input()
n=[]
for i in s:
    if i.isdigit():
        n.append(i)
#print(n)
n.sort(reverse=True)
print(n)
for i in range(len(n)-1,-1,-1):
    if int(n[i])%2==0:
        n.append(n.pop(i))
        print("".join(n)) 
        break   
else:
    print(-1)
# output:
    # 9765142
    # ['9', '7', '6', '5', '4', '2', '1']
    # 9765412


#numerical sorting on string date

l=['8','9','999','878','27878686787','2','9']
sorted(l, reverse=True) #will only work on numbers
print(l)
l.sort(key=lambda x:(len(x),x))
print(l)
# output:
    # ['8', '9', '999', '878', '27878686787', '2', '9']
    # ['2', '8', '9', '9', '878', '999', '27878686787']


#sort without using lambda
l = ['8', '9', '999', '878', '27878686787', '2', '9']
l.sort(key=str)
print(l)
l = sorted(l, key=int)
print(l)
# output:
#     ['2', '27878686787', '8', '878', '9', '9', '999']
#     ['2', '8', '9', '9', '878', '999', '27878686787']
