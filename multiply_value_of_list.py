# Creating lists

list1 = []
list2 = []

# Define number of elements in list

n = int(input('Enter the number you want to make list => '))

# Append elements in list by user input

for a in range(n):
    val1 = int(input(f'Enter the {a+1} element for list 1 => '))
    list1.append(val1) 
print('')
for b in range(n):
    val2 = int(input(f'Enter the {b+1} element for list 2 => '))
    list2.append(val2)

# print the list

print('list 1 is ',list1)
print('list 2 is ',list2)

# Take add1 and add2 to convert 'num' to 'str'

add1 = ''
add2 = ''
for num1 in list1:
    add1 = add1 + str(num1)
for num2 in list2:
    add2 = add2 + str(num2)

# Output (Answer)

for k in list1:

    print(k,end='')
print(' *',end=' ')
for l in list2:
    print(l,end='')
print(' =',end=' ')
add1 = int(add1)
add2 = int(add2)
print(add1*add2)

