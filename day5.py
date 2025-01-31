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