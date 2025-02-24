#staircase hackerrank
n=int(input())
def staircase(n):
    for i in range(1,n):
        print(" "*(n-i),end="")
        print("#"*i)
    for i in range(1,n+1):
        if i==n:
            print(" "*(n-i),end="")
            print("#"*i)

staircase(n)

# birthday cake hackerrank
n=int(input())
l=list(map(int,input().split()))
def birthdayCakeCandles(l):
    # Write your code here
    # return candles.count(max(candles))
    c=0
    max=l[0]
    for i in range(len(l)):
        if max<l[i]:
            max=l[i]
    for i in l:
        if max==i:
            c=c+1
    return c

print(birthdayCakeCandles(l))

#simple sum of array hackerrank
def simpleArraySum(n):
    ar=[]
    s=0
    for i in range(n):
        ar.append(int(input()))
    for i in ar:
        s=s+i
    return print(s)
n=int(input())
simpleArraySum(n)

#plus minus hacker rank 
n=int(input())
arr=list(map(int,input().split()))
def plusMinus(arr):
    # Write your code here
    p=n=z=0
    for i in arr:
        if i>0:
            p=p+1
        elif i<0:
            n=n+1
        else:
            z=z+1
    print(format(p/len(arr),'6f'))
    print(format(n/len(arr),'6f'))
    print(format(z/len(arr),'6f'))

plusMinus(arr)

#super reduced string

def superReducedString(s):
    # Write your code here
    s=list(s)
    i=0
    while i<len(s)-1:
        if s[i]==s[i+1]:
            del s[i+1]
            del s[i]
            i=0
        else:
            i=i+1
    if len(s)==0:
        return "Empty String"
    else:
        return "".join(s)

#counting valleys

def countingValleys(steps, path):
    # Write your code here
    n=0
    c=0
    for i in path:
        if i=="U":
            n=n+1
            if n==0:
                c=c+1
        elif i=="D":
            n=n-1
        
    return c

#time conversion

def timeConversion(s):
    # Write your code here
    t=s[-2:]
    s=s[:-2].split(":")
    
    if t=="PM":
        if int(s[0])<12:
            s[0]=str(int(s[0])+12)
        return ":".join(s)
    elif t=="AM":
        if int(s[0])>=12:
            s[0]="{:02d}".format(int(s[0])-12)
        return ":".join(s)


#diagonal difference


def diagonalDifference(arr):
    # Write your code here
    s1=s2=0
    for i in range(len(arr)):
        s1=s1+arr[i][i]
        for j in range(len(arr[i])):
            if (i+j)==len(arr[i])-1:
                s2=s2+arr[i][j]
    return abs(s1-s2)

#min max sum

def miniMaxSum(arr):
    # Write your code here
    min_sum=sum(arr)-max(arr)
    max_sum=sum(arr)-min(arr)
    print(min_sum,max_sum)

#breaking the records

n=int(input())
l=list(map(int,input().split()))
def breakingRecords(l):
    # Write your code here
    mc=mxc=0
    m=mx=l[0]
    for i in l:
        if i<m:
            m=i
            mc=mc+1
        elif i>mx:
            mx=i
            mxc=mxc+1

    print(mxc,mc)
breakingRecords(l)

# In this challenge, you will determine whether a string is funny or not. To determine whether a string is funny, create a copy of the string in reverse e.g. .abc->cba Iterating through each string, compare the absolute difference in the ascii values of the characters at positions 0 and 1, 1 and 2 and so on to the end. If the list of absolute differences is the same for both strings, they are funny.

# Determine whether a give string is funny. If it is, return Funny, otherwise return Not Funny.
s='lmnop'values are[112,111,110,109,108] s.reverse='ponml' ordinal values are [108,109,110,111,112] absolutr differnce is [1,1,1,1]
def funnyString(s):
    # Write your code here
    r=s[::-1]
    flag=True
    for i in range(1,len(s)):
        if abs(ord(s[i])-ord(s[i-1]))!=abs(ord(r[i])-ord(r[i-1])):
            flag=False
    if flag:
        print('Funny')
    else:
        print('not funny')
q= int(input('enter q: '))
for i in range(q):
    s=input('enter string: ')
    funnyString(s)

here is a string,s , of lowercase English letters that is repeated infinitely many times. Given an integer, , find and print the number of letter a's in the first  n letters of the infinite string.

Example
s='abcac'
n=10
there are 4 occurances of of a in this sub string 

def repeatedString(s, n):
    # Write your code here
    c=s.count('a')
    print(c,'is intial')
    l=len(s) 
    rem=n//l
    print(rem)
    c=c*rem
    print(c,'after mul')
    l=l*rem
    
    if n>l:
        rem=n%l
        for i in s[:rem]:
            if i=='a':
                c=c+1
                
    return c
s=input()
n=int(input())
print(repeatedString(s,n))
