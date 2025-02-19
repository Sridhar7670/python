inputs = input("Enter values separated by spaces: ").split()

for value in inputs:
    try:
        # Attempt to evaluate the input to its appropriate type
        evaluated_value = eval(value)
    except:
        # If eval fails, treat it as a string
        evaluated_value = value
    
    # Check the type and print
    if isinstance(evaluated_value, int):
        print(f"{value}: integer")
    elif isinstance(evaluated_value, float):
        print(f"{value}: float")
    elif isinstance(evaluated_value, str):
        print(f"{value}: string")
    else:
        print(f"{value}: something else")

# to print min max sum using pre defined functions
n = [4, 1, 9, 3, 7]
print(min(n))
print(max(n))
print(sum(n))

# to print min max sum without using pre defined functions
n = [4, 1, 9, 3, 7]
min=max=n[0]
for i in n:
    if max<i:
        max=i
    elif min>i:
        min=i
for i in range(1,len(n)):
        n[0]+=n[i]
print(n[0])
print(min,max)

#print reverse using pre defined
n = [4, 1, 9, 3, 7]
n.reverse()
print(n)

# print reverse without using predefined fucntion 
n = [4, 1, 9, 3, 7]
for i in range(len(n)):
    n.insert(i,n.pop())
print(n)

#sort in ascending and descending order using pre defined function 
n = [4, 1, 9, 3, 7]
n.sort()
print(n)
n.sort(reverse=True)
print(n)


#printing nearest prime number 
num = int(input('Enter the number: '))

def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def near_prime(num):
    if isprime(num):
        print('The number is prime itself:', num)
    else:
        lower = num - 1
        upper = num + 1
        while True:
            if isprime(lower):
                print('Nearest prime is', lower)
                break
            elif isprime(upper):
                print('Nearest prime is', upper)
                break
            else:
                lower -= 1
                upper += 1
near_prime(num)




#printing nearer prime upper and lower

num = int(input('Enter the number: '))

def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)):
        if num % i == 0:
            return False
    return True

def near_prime(num):
    if isprime(num):
        pass
    
    lower = num - 1
    upper = num + 1
    f1,f2=True,True
    
    while True:
        if isprime(lower) and f1 :
            print('lower prime number is',lower)
            f1=False
        if isprime(upper) and f2:
            print('the upper prime num is',upper)
            f2=False
        if not f1 and not f2:
            break
            
        lower-=1
        upper+=1
        
near_prime(num)




#find missing in list without using pre defined functions

l=list(map(int,input('enter the list of numbers').split()))
# m=min(l)
# n=max(l)
m=n=l[0]
for i in l:
    if m>i:
        m=i
    elif n<i:
        n=i
print('min is: ',m,'max is: ',n)
print('missing numbers are: ')
for i in range(m,n):
    if i not in l:

        print(i,end=" ")


# diplay lonely interger in the list 

l=list(map(int,input().split()))
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if l[i]==l[j]:
            c+=1
    if c==1:
        print(l[i])



# second largest from list 

l=list(map(int,input().split()))
l.sort()
for i in range(len(l)-1,-1,-1):
    if l[i] !=l[i-1]:
        print(l[i-1])
        break 


# second largest from list 
l=list(map(int,input().split()))
m=max(l)
while m in l:
    l.remove(m)
print(max(l))


# sort the list without using predefined function 

l=list(map(int,input().split()))
i=0
while i<len(l):
    j=i+1
    while j<len(l):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
        else:
            j+=1
    i+=1
print(l)


# find maximum repeated number
l=list(map(int,input().split()))

maxi=0
elem=None
for i in l:
    c=0
    for j in l:
        if i==j:
            c+=1
    if c>maxi:
        maxi=c
        elem=i
print('the repeated elem is ',elem,'the number of repetations :',maxi)


#reverse the list items without using external memory 

l=list(map(int,input().split()))
for i in range(len(l)):
    l.insert(i,l.pop())
print(l)


#deleting duplicates without using external memory

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
print(l)


#display lonely integer 

l=list(map(int,input().split()))
for i in range(min(l),max(l)):
    if i not in l:
        print(i)
        break

# to display count of prime numbers in list 
l = list(map(int, input().split()))
c = 0

for number in l:
    if number > 1:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            c += 1

print(c)

# to check if given number at odd index in list id divisible to 3 or 5 and add sum 

l = list(map(int, input().split()))
i = 1
s = 0
while i < len(l):
    if l[i] % 3 == 0 or l[i] % 5 == 0:
        s += l[i]
    i += 2  # Move to the next odd index
print(s)


#creating nested list 
l=[]
r=int(input())
c=int(input())
for i in range(r):
    x=[]
    for j in range(c):
        x.append(int(input()))
    l.append(x)
print(l)


#word weight
s=input()
w=0
for ch in s:
    w=w+ord(ch)-96
print(w)


# heighest repeated count frequcny
s=input()
count={}
for i in s:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1

print(sorted(count.items(),reverse=True,key=lambda x:x[1])[0])


#string anagram 
s1=input()
s2=input()
if len(s1)==len(s2):
    for i in s1:
        if i in s2:
            s2.replace(i,"",1)
    if len(s2)==0:
        print('yes')
    else:
        print('no')  
else:
    print('no')


# super reducible string 

s=list(input())
i=0
while i<len(s)-1:
    if s[i]==s[i+1]:
        del s[i]
        del s[i]
        i=0
    else:
        i=i+1
if len(s)==0:
    print('empty')
else:
    print("".join(s))


# Creating a dictionary
dic= {'name': 'John', 'age': 25, 'city': 'New York'}
print(dic.items())

dic['name']='sunny'
print(dic)

dic.popitem()
print(dic)

dic.pop('name')
print(dic)

del dic['age']
print(dic)

dic['name']='sridhar'
dic['age']=21

print(dic)
dic1=dic.copy()

print(dic1)


dic.clear()
print(dic)



# reverse a string without disturbing symbols
s=list(input().lower())
i=0
j=len(s)-1
while i<j:
    if s[i].isalnum() and s[j].isalnum():
        s[i],s[j]=s[j],s[i]
        i=i+1
        j=j-1
    elif s[i].isalnum():
        j=j-1
    elif s[j].isalnum():
        i=i+1
print("".join(s))


#
s=list(input())
s1=[]
s2=""
for i in s:
    s1.insert(0,(i,s.count(i)))
print(s1)
for i in s1:
    s2+=i[0]+str(i[1])
print(s2)


#find key and vak=lues in dictionary 

rec={}
n=int(input())
for i in range(1,n+1):
    name=input("enter name")
    marks=int(input("enter marks in percentage"))
    rec[name]=marks
print('name of student \t % of marks')
for x in rec:
    print(x,"\t\t",rec[x])
del rec['sridhar']
print(rec)


#basic of dict
d=dict({1:'hello',2:'hi',3:'hey'})
print(d.get(8))
print(d.get(1))
print(d.items())
d.pop(1)
print(d)
d.popitem()
print(d)
    # None
    # hello
    # dict_items([(1, 'hello'), (2, 'hi'), (3, 'hey')])
    # {2: 'hi', 3: 'hey'}
    # {2: 'hi'}
d=dict({1:'hello',2:'hi',3:'hey'})
x=d.copy()
s=dict({1:'bye',4:'welcome'})
d.update(s)
print(d)
print(x)
    # {1: 'bye', 2: 'hi', 3: 'hey', 4: 'welcome'}
    # {1: 'hello', 2: 'hi', 3: 'hey'}

d=eval(input('enter dict'))
s=sum(d.values())
print(s)
    # enter dict {'a':100,'b':200,'c':300}
    # 600


#count repeated frequency
s=input('enter some word')
d={}
for i in s:
    d[i]=d.get(i,0)+1
# print(d)
for k,v in d.items():
    print(k,'occured',v,'times')

    # enter some word hello world
    # h occured 1 times
    # e occured 1 times
    # l occured 3 times
    # o occured 2 times
    #   occured 1 times
    # w occured 1 times
    # r occured 1 times
    # d occured 1 times



#vowels ocuured how many times 
s=input('enter some word')
v={'a','e','e','o','u'}
d={}
for i in s:
    if i in v:
        d[i]=d.get(i,0)+1
# print(d)
for k,v in d.items():
    print(k,'occured',v,'times')
    # enter some word hello world i am sridhar 
    # e occured 1 times
    # o occured 2 times
    # a occured 2 times



#searching alogrithm in dict 

n=int(input())
d={}
for i in range(n):
    name=input('enter name')
    marks=int(input('enter marks'))
    d[name]=marks
while True:
    name=input('enter student name')
    marks=d.get(name,-1)
    if marks==-1:
        print('student data not found')
    else:
        print('the marks of',name,'are',marks)
    option=input('want to search again [Yes|No]')
    if option=='No':
        print('okay have a great day')
        break

        #  2
        # enter name s
        # enter marks 99
        # enter name a
        # enter marks 12
        # enter student name s
        # the marks of s are 99
        # want to search again [Yes|No] No
        # okay have a great day

#fun with dictionaries
squares={x:x*x for x in range(1,6)}
print(squares)
double={x:2*x for x in range(1,6)}
print(double)
