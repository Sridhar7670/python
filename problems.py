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



Find StringCode:
Crazy Zak has designed the below steps which can be applied on any given string to produce a number.
STEP1: in each word, find the sum of the difference between the first letter and the last letter, second letter and the penultimate letter, and so on till the center of the word.
STEP2: concatenate the sums of each word to form the result.
For example:
If the given String is “WORLD WIDE WEB” Step1: In each word, find the sum of the Difference between the first letter and the last letter, second letter and the penultimate letter, and so on till the center of the word. WORLD=[W-D]+[O-L]+[R]=[23-4]+[15-12]+[18]=19+3+18=[40] WIDE=[W-E]+[I-D]=[23-5]+[9-4]=[18]+[5]=[23] WEB=[W-B]+[E]=[23-2]+[5]=[21]+[5]=[26]
STEP2: Concatenate the sums of each word to form the result [40][23][26] [402326]
The answer(output) should be the number 402326
NOTE1: the value of each letter is its position in the English alphabet system i.e., a=A=1, b=B=2, and so on till z=Z=26.
So, the result will be the same for “WORLD WIDE WEB” or “World Wide Web” or “world wide web” or any other combination of uppercase and lowercase letters.
IMPORTANT NOTE: In step1, after subtracting the alphabet, we should use the absolute values for calculating the sum. For instance, in the below example, both [H-O] and [E-L] result in negative number -7. But the positive number 7 (absolute value of -7) is used for calculating the sum of the differences .
Hello=[H-O]+[E-L]+[L]=[8-15]+[5-12]+[12]=[7]+[7]+[12]=[26]
Sample Input 0:
World Wide Web
output:
402326
sample out 1:
Hello World
output:
2640


code:
s=input().upper().split()
n=""
for w in s:
    i=0
    j=len(w)-1
    t3=0
    while i<j:
        t1=ord(w[i])-64
        t2=ord(w[j])-64
        t3=t3+abs(t1-t2)
        i+=1
        j-=1
    if len(w)%2==1:
        t3=t3+ord(w[i])-64
    n=n+str(t3)
print(n)
        

nthcharecter:
eg: input:
a1b1c3
5
output: c
a1b1c3 is the input decrypted string is abccc 5th charecter in the decrypted sting is 'c'
eg:2
input:
a3b2
7
output: -1 there are only 5 charecters in a given string 7th charecter was not their so it is -1
Sample Input 0
a1b1c3
5
Sample Output 0
c
Sample Input 1
a3b2
7
Sample Output 1
-1

code:
s=input()
n=int(input())
c=0
i=1
while i<len(s):
    c=c+int(s[i])
    if c>=n:
        print(s[i-1])
        break 
    i=i+2
else:
    print(-1)



Strong Password:
The website considers a password to be strong if it satisfies the following criteria:

Its length is at least .
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

Note: Here's the set of types of characters in a form you can paste in your solution:

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
Example
password:'2bbbb'
This password is 5 characters long and is missing an uppercase and a special character. The minimum number of characters to add is 2
password:'2bb#A'
This password is 5 characters long and has at least one of each character type. The minimum number of characters to add is 1
Function Description
Complete the minimumNumber function in the editor below.
minimumNumber has the following parameters:
int n: the length of the password
string password: the password to test
Returns
int: the minimum number of characters to add

code:

def minimumNumber(n, s):
    # Return the minimum number of characters to make the password strong
    f1=f2=f3=f4=1
    for ch in s:
        if ch.isdigit():
            f1=0
        if ch.isupper():
            f2=0
        if ch.islower():
            f3=0
        if ch in "!@#$%^&*()-+ ":
            f4=0
    if (n>=6):
        return f1+f2+f3+f4
    else:
        return (max((6-n),(f1+f2+f3+f4)))
        
extractingdigits:
Extract all the digits from the given string and form a largest number posible.

if digits are not there display 0.

Input Format

eg: input: he9w2e3e1 output: 9321

input: jsfdvsndkvjs output: 0
code:

s=input()
l=[]
for ch in s:
    if ch.isdigit():
        l.append(int(ch))
l.sort()
n=0
i=0
while i <len(l):
    n=n*10+l.pop()
    
print(n)


delete duplicates:
Delete duplicate elements from list without changing insertion order
eg 4 3 5 2 1 4 3 7 7
then 4 3 5 2 1 7
by using some other list 

l=list(map(int,input().split()))
n=[]
for i in l:
    if i not in n:
        n.append(i)       
print(*n)    

operating on same list 
l=list(map(int,input().split()))
i=0
while i<len(l)-1:
    j=i+1
    while j <len(l):
        if l[i]==l[j]:
            l.pop(j)
        else:
            j=j+1
    i=i+1
print(*l)        
        
        
moving zeros:
Write a program that moves all the zeroes to the end of a list. Remining elements order should be same as the original list.
example:
[1, 2, 0, 0, 4, 0, 5] ➞ [1, 2, 4, 5, 0, 0, 0] [0, 0, 2, 0, 5] ➞ [2, 5, 0, 0, 0] [4, 4, 5] ➞ [4, 4, 5] [0, 0] ➞ [0, 0] [3,0,1,2,0] ➞ [3,1,2,0,0]
Input Format
all the list elements are in the same line
Output Format
all the list elements need to display on the same line
code:
using variable c:

l=list(map(int,input().split()))
c=0
while 0 in l:
    l.remove(0)
    c=c+1
    
while c>0:
    l.append(0)
    c=c-1
print(*l)

wihtout using external variable:

l=list(map(int,input().split()))
i=0
while i<len(l):
    if l[i]==0:
        l.remove(l[i])
        l.append(0)
    i=i+1
print(*l)





return or print the second largest in list 


code:
without using pre defined fucntion 
l=list(map(int,input().split()))
mx=l[0]
for i in l:
    if i>mx:
        mx=i

while mx in l:
        l.remove(mx)
    
print(max(l))

using pre defined

l=list(map(int,input().split()))
m=max(l)
while m in l:
    l.remove(m)
print(max(l))


if we list all the natural numbers below 10 divisble by 3 or 5 and sum them we get 23
below 10 : 3 5 6 9 sum is 23
below 100: 3 5 6 9 ..... sum is 2318
solved but time complexity is more 
#!/bin/python3
t=int(input())
for i in range(t):
    n=int(input())
    c=0
    for i in range(1,n):
        
        if i%3==0 or i%5==0:
            c=c+i
    print(c)

reduced time complexity 
def sum_of_multiples(n, k):
    m = (n - 1) // k   
    return k * m * (m + 1) // 2

t = int(input())
for i in range(t):
    n = int(input())
    s = sum_of_multiples(n, 3) + sum_of_multiples(n, 5) - sum_of_multiples(n, 15)
    print(s)


Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with  1 and 2, the first  10 terms will be:
1,2,3,5,8,13,21,34,55,89
By considering the terms in the Fibonacci sequence whose values do not exceed N, find the sum of the even-valued terms.
for N=10, we have {2,8} sum is 10
for N=100 , we have{2,3,34} sum is 44

code:
    
def fibonaci(n):
        if n == 1:
            return 1
        if n <= 0:
            return 0
        a, b = 0, 1  
        ans = 0
        while True: 
            if a % 2 == 0: 
                ans += a  
            a, b = b, a + b 
            if a > n:  
                break
        print(ans)  
        
t=int(input())
for i in range(t):
    n=int(input())
    fibonaci(n)

# binary sorting
 
l=list(map(int,input().split()))
k=int(input())
i=0
u=len(l)-1
while i<=u:
    m=(i+u)//2
    if k==l[m]:
        print('index is',m)
        break
    elif k<l[m]:
        u=m-1
    else:
        i=m+1
else:
    print(-1)


 #bubble sort

l=list(map(int,input().split()))
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[j]<l[i]:
             l[i],l[j]=l[j],l[i]
print(l)
6 4 9 2 3 77 
[2, 3, 4, 6, 9, 77]

 #selection sort:

l=list(map(int,input().split()))
for i in range(len(l)-1):
    k=i
    for j in range(i+1,len(l)):
        if l[j]<l[k]:
            k=j
    l[i],l[k]=l[k],l[i]
print(l)
5 8 4 2 6 9 7 1 3 
[1, 2, 3, 4, 5, 6, 7, 8, 9]

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
  9765142
['9', '7', '6', '5', '4', '2', '1']
9765412

 #numerical sorting on string date
l=['8','9','999','878','27878686787','2','9']
sorted(l, reverse=True) #will only work on numbers
print(l)
l.sort(key=lambda x:(len(x),x))
print(l)
 ['8', '9', '999', '878', '27878686787', '2', '9']
['2', '8', '9', '9', '878', '999', '27878686787']

 #sort without using lambda
l = ['8', '9', '999', '878', '27878686787', '2', '9']
l.sort(key=str)
print(l)
l = sorted(l, key=int)
print(l)
['2', '27878686787', '8', '878', '9', '9', '999']
['2', '8', '9', '9', '878', '999', '27878686787']

 s=input()
st=[]
r=""
for ch in s:
    st.append(ch)
while len(st)!=0:
    r=r+st.pop()
print(r)
hello 
olleh


  s=input()
st=[]
for ch in s:
    if ch in '{[(':
        st.append(ch)
    else:
        if len(st)==0:
            print('invalid')
            break
        elif st[-1]=='[' and ch==']':
            st.pop()
        elif st[-1]=='{' and ch=='}':
            st.pop()
        elif st[-1]=='(' and ch==')':
            st.pop()
        else:
            print('invalid')
            break
else:
    if len(st)==0:
        print('valid')
    else:
        print('invald')

  {[]}]
invalid



  s=input()
st=[]
for ch in s:
    if ch.isdigit():
        st.append(int(ch))
    else:
        b=st.pop()
        a=st.pop()
        match ch:
            case'+':
                st.append(a+b)  
            case'-':
                st.append(a-b)
            case'*':
                st.append(a*b)
            case'/':
                st.append(a/b)
print(st[-1])

354-0+9/8
8


def ispal(n):
    l=list(map(int,str(n)))
    i=0
    j=len(l)-1
    while i<j:
        if l[i]!=l[j]:
            return False
        i=i+1
        j=j-1
    return True
l=[1,2,3,4,121,444,345,456]
print(list(filter(ispal,l)))


# add first and last digits of a number 
 
def sumNumber(n):
    l=list(map(int,str(n)))
    return l[0]+l[-1]
sumNumber(12345)  


#apply gcd function on the list 
def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
# print(gcd(8,16))
from functools import reduce
l=list(map(int,input().split()))
print(reduce(gcd,l))



#usage of some Lambda functions 
from functools import *
l = [1, 2, 11, 4, 5, 6]

# reduce fucntion 
print(reduce(lambda x,y:x+y,l))
print(reduce(lambda x,y:x-y,l))

# map function 
print(list(map(lambda x:x*2 if x%2==0 else x,l)))
print(list(filter(lambda x:x if x%2==0 else 0,l)))

# simple application of lambda 
print([l[i]*2 if i % 2 == 0 else l[i] for i in range(len(l))])
print([l[i] * 2 if i%2!=0 else l[i] for i in range(len(l))])




s=input().lower()
n=""
for ch in s:
    if s.count(ch)==1:
        n+=str((ord(ch)-96))
    else:
        n+=str(s.count(ch))
print(n)
     
input:
hheelloo
output:
22222222

remove dublicates
def remdub(s):
    temp=""
    for ch in s:
        if ch not in temp:
            temp=temp+ch
    s=temp
    return s
s=input()
print(remdub(s))
hello
helo



 # aaaabbbccc  a4b3c3
def chcount(s):
    d={}
    for ch in s:
        d[ch]=d.get(ch,0)+1
    c=""
    for k,v in d.items():
        c+=k+str(v)
    return c
s=input()
print(chcount(s))


#a4r5t6 if n=6 op is r
s=input()
n=int(input())
i=1
c=0
while i<len(s):
    c=c+int(s[i])
    if n<c:
        print(s[i-1])
    i=i+2

#count chars and return count
     ex:aaaabbbbbaaaa
     a4b5a4
def chcount(s):
    l=[]
    i=1
    c=1
    while i<len(s):
        if s[i]==s[i-1]:
            c=c+1
        else:
            l.append(s[i-1]+str(c))
            c=1
        i=i+1
    l.append(s[-1]+str(c))
    return "".join(l)
s=input()
print(chcount(s))
