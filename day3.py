##to print pattern 
def printed(n):
    if n==1:
        print('*')
        return 
    print('*' *n)
    for i in range(n-2):
        print('*' +' '*(n-2)+'*')
    print('*' *n)
i=int(input())
printed(i)

n=int(input())
for i in range (1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()
    
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 

n=int(input())
for i in range (1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()
    
# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5 


n= int(input())
for i in range (1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 


n= int(input())
for i in range (1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 


n= int(input())
for i in range(1,n+1):
    print("  "*(n-i),end='')
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#         1 
#       1 2 
#     1 2 3 
#   1 2 3 4 
# 1 2 3 4 5

n= int(input())
for i in range(1,n+1):
    print("  "*(n-i),end='')
    for j in range(i+1,1,-1):
        print(i,end=" ")
    print()
    
#         1 
#       2 2 
#     3 3 3 
#   4 4 4 4 
# 5 5 5 5 5 

n= int(input())
for i in range(1,n+1):
    print("  "*(n-i),end='')
    for j in range(i+1,1,-1):
        print(j-1,end=" ")
    print()
    
#         1 
#       2 1 
#     3 2 1 
#   4 3 2 1 
# 5 4 3 2 1

n= int(input())
for i in range(1,n+1):
    print("  "*(n-i),end='')
    for j in range(i+1,1,-1):
        print(j-1,end=' ')
    print()
    
#         1 
#       2 1 
#     3 2 1 
#   4 3 2 1 
# 5 4 3 2 1

n= int(input())
for i in range(1,n+1):
    print("  "*(n-i),end='')
    for j in range(n,n-i,-1):
        print(j,end=' ')
    print()

#         5 
#       5 4 
#     5 4 3 
#   5 4 3 2 
# 5 4 3 2 1

n= int(input())
for i in range(1,n+1):
    print(" "*(n-i),end='')
    for j in range(n,n-i,-1):
        print(j,end=' ')
    print()
    
#     5 
#    5 4 
#   5 4 3 
#  5 4 3 2 
# 5 4 3 2 1    

n= int(input())
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(i):
        print('*',end=' ')
    print()
    
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     *


n= int(input())
for i in range(1,n+1):
    print(" "*(n-i),end='')
    for j in range(n,n-i,-1):
        print('*',end=' ')
    print()
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(i):
        print('*',end=' ')
    print()

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     *
