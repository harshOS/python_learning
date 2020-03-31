import os
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))

print(os.getcwd())
#os.chdir() #chage working directory
#os.mkdir() #make new directory
# print(os.path.abspath('.')) #getting absolute path
# print(os.path.abspath('python_learning'))
# >>> os.path.dirname('test')
# ''
# >>> os.path.basename('test')
# 'test'
# >>> os.path.basename('.')
# '.'
# >>> os.path.abspath
# <function abspath at 0x011C7CD8>
# >>> os.path.abspath('test')
# 'C:\\Users\\Harshith NG\\PycharmProjects\\python_learning\\ABSWP\\test'
# >>> os.getcwd()
# 'C:\\Users\\Harshith NG\\PycharmProjects\\python_learning\\ABSWP'
# >>> os.path.abspath('.')
# 'C:\\Users\\Harshith NG\\PycharmProjects\\python_learning\\ABSWP'
# >>> os.path.abspath('..')
# 'C:\\Users\\Harshith NG\\PycharmProjects\\python_learning'
# >>> os.path.split('C:\\Users\\Harshith NG\\PycharmProjects\\python_learning\\ABSWP')
# ('C:\\Users\\Harshith NG\\PycharmProjects\\python_learning', 'ABSWP')
# >>> os.path.sep
# '\\'
# >>> os.path.getsize()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: getsize() missing 1 required positional argument: 'filename'
# >>> os.path.getsize(os.getcwd())
# 4096
# >>> os.listdir()
# ['bulletAdder.py', 'collatzSeries.py', 'DSpractice.py', 'filesPractice.py', 'isPhoneNumber.py', 'isPhoneNumberIN.py', 'password_locker.py', 'phoneAndemail.py', 'phoneNumINRegex.py', 'README.md', 'stringsPractice.py', 'test']
# >>> os.path.getsize('..')
# 4096
# >>> os.path.exists('test')
# True
# >>> os.path.isfile('test')
# False
# >>> os.path.isdir('test')
# True

# >>> r = open('README.md')
# >>> r
# <_io.TextIOWrapper name='README.md' mode='r' encoding='cp1252'>
# >>> content = r.read()
# >>> content
# 'Practice codes from book "Automate the Boring Stuff with Python, 2nd Edition\nPractical Programming for Total Beginners\nby Al Sweigart"'

