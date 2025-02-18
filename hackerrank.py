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