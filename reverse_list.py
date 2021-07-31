listA = []
n = int(input('Enter the count of numbers you want to write => '))
for num in range(n):
    val = int(input(f'Enter the {num+1} number => '))
    listA.append(val)
res = []

'''for i in range(listA[-1],listA[0]-1,-1):
    res.append(i)
print(res)
'''
# or

'''print(listA[::-1])'''