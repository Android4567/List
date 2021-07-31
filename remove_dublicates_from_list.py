l = []
mainlist =[]
for i in range(10):
    num = int(input(f'Enter the {i+1} element to add in a list => '))
    l.append(num)
for j in l:

   if j not in mainlist:
       mainlist.append(j)
print(l)
print(f'list after removing dublicate values is {mainlist}')

