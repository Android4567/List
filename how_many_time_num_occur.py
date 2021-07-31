list1 = []
for i in range(10):
    val = int(input(f'Enter The {i+1} element to add in the list => '))
    list1.append(val)
flag = False
print(list1)
Search_count = int(input('Enter the number to know that occur how many time in thre list => '))
count = 0
for j in list1:
    if j == Search_count:
        count += 1
        flag = True
if flag:
    print(Search_count,f"accurs, {count} ,in a list")

if Search_count not in list1:
    print('number is not available in list')
