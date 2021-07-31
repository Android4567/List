# Creating list variable
listA = []

# Ask for number of values
n = int(input('Enter the count of nuber you want to write => '))

# Making list
for i in range(n):
    val = int(input(f'Enter the {i+1} number'))
    listA.append(val)

# Number for search
search = int(input('Enter the number you want to search in list => '))

# To get position of search in list
count = 0
for i in listA:
    if search != i:
        count += 1
    else:
        break

# Print the list
print('list is',listA)

# Number is available in list or not
for i in listA:
    if i == search:
        print(f'number is available in list at {count+1} position ')
if search not in listA:
    print('number is not available in list')
    
