#comparing linear search and binary search

import random

list = []
itr = 0
for i in range(100):
    list.append(random.randrange(0,1000))

list.sort()

#linear search
print(list)
search_num = int(input('Enter a number to search in the list: '))

for i in list:
    itr += 1
    if i == search_num:
        print('Number found at',list.index(search_num))
        print('It took total of ',itr,'terations')
        break

else:
    print('number not in the list')
    print('It took total of ',itr,'iterations')

itr = 0
mid = 0
start = 0
end = len(list)

#Binary search
while(start < end):
    mid = int((start + end)/2)
    print(start,mid, mid)
    itr += 1
    print('Iteration {} : Current list is {}'.format(itr,list[start:mid]))
    if list[mid] == search_num:
        print('Number found at',list.index(search_num))
        print('It took total of ',itr,'terations')
        break
    elif(search_num < list[mid]):
        end = mid - 1
    else:
        start = mid + 1
else:
    print('number not in the list')
    print('It took total of ',itr,'iterations')






































