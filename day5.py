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
