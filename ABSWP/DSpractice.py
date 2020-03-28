# spam = [2, 5, 3.14, 1, -7] #list
# spam.sort()
# print(spam)
# spam.sort(reverse=True)
# print(spam)

# spam = (1,2,3) #tuple
# #spam = 0 #tuples are immutable
# print(spam)

# print(type(('hello',)))
# #<class 'tuple'>
# type(('hello'))
# #<class 'str'>

# scam  = spam[1]
# print(id(spam))
# print(id(scam))
#
# spam[1] = "changed"
#
# print(spam,scam)

# spam = ['cats', 'dogs', 'moose']
# bacon = ['dogs', 'moose', 'cats']
# print(spam == bacon)
# eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
# ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
# print(eggs == ham)
#
# print(eggs.items())
# print(eggs.keys())
# print(eggs.values())

# picnicItems = {'apples': 5, 'cups': 2} #dict.get() method
# print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.') #get(keyvalue ,return value when key not available)
#
# print('I am bringing ' + str(picnicItems.get('eggs', "zero")) + ' eggs.')

# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# print(count)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.setdefault("brand")
# car['brand'] = "audi"
#
# print(x)
import pprint #cleaner printing
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)