a = int(input("Enter the first value => "))
b = int(input("Enter the second value => "))

res = a*b
l = len(str(res))
mid = []
counter = 0
for i in range(len(str(b))-1,-1,-1):
    m = a * int(str(b)[i])
    if (counter==0):
        mid.append(str(m))
        counter = counter+1
    else:
        mid.append(str(m)+('x'*counter))
        counter = counter+1
# print(counter)
# print(mid)


for i in [a,b]:
    for sp in range(l-len(str(i))):
        print(' ',end='')
    print(i)
print("----------------")
for i in mid:
    for sp in range(l-len(i)):
        print(' ',end='')
    print(i)
print("----------------")
print(res)
print("----------------")