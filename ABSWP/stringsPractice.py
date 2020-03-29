# while True:
#     print('Enter your age:')
#     age = input()
#     if age.isdecimal():
#         break
#     print('Please enter a number for your age.')
# while True:
#     print('Select a new password (letters and numbers only):')
#     password = input()
#     if password.isalnum():
#         break
#     print('Passwords can only have letters and numbers.')

# print(', '.join(['cats', 'rats', 'bats']))
# print(' '.join(['My', 'name', 'is', 'Simon']))
# print('ABC'.join(['My', 'name', 'is', 'Simon']))
#
# print('MyABCnameABCisABCSimon'.split('ABC'))
# print('My name is Simon'.split(' '))

# print('Hello'.rjust(20))
# print('Hello'.rjust(20, '*'))
#
# print('Hello'.ljust(20))
# print('Hello'.ljust(20, '-'))
#
# print('Hello'.center(20))
# print('Hello'.center(20, '='))

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)