
#_hello= "hello world"
#print(_hello)

# hex(100)
# print(hex(100))

# print(oct(0B1111))

# print(oct(0x123))

# f=0B1111
# print(f)

# print(True*True)
# print(False+False)

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

##arrange in ascending order (3 numbers)
a, b, c = map(int, input("Enter three values: ").split())
if a>b and a>c:
    if b>c:
        print(c,b,a)
    else:
        print(b,c,a)
elif b>c and b>a:
    if a>c:
        print(c,a,b)
    else:
        print(a,c,b)
elif c>a and c>b:
    if a>b:
        print(b,a,c)
    else:
        print(a,b,c )

##print odd or even of n numbers using list 
numbers = list(map(int,input().split()))

for num in numbers:
    if num % 2 == 0:
        print(str(num)+' is even')
    else:
        print(str(num)+' is odd ')


##check is prime or ot using flag and not using flag
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

#withot using flag 
def isprime(num):
    
    if num<=1:
        print('not prime')
    for i in range(2,num):
        if num%i==0:
            print('not prime')
            break
    else:
        print('prime')       
isprime(7)


#reverse a string slicing operation 
def revstring(str):
    return str[::-1]
string='hello world'
print(revstring(string))

#reverse word-by-word in str 
def revstring(str):
    return ' '.join(i[::-1] for i in str.split(' '))

string='hello world'
print(revstring(string))

#reverse without slicing 
s='qwerty poiuy'
rev=''
for i in range(len(s)):
    rev+=s[i]
print(rev)

#reversing word by world using external string
s = 'qwerty poiuy'
rev = ''

words = s.split()


for word in words:
    rev += word[::-1] + ' '  

rev = rev.strip()  # Remove the trailing space
print(rev)
