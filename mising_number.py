listA = [1,2,3,4,5,6,7,9,10]

'''
res = [x for x in range(listA[0],listA[-1])
if x not in listA]
'''
#           Or 
res = []
num = listA[0]
for i in listA:
    if num != i:
        res.append(i-1)
        num +=1
    print(num)
    num = num+1
    




print('missing numbers are',res)


