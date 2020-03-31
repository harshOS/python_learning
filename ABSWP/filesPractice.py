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
# >>>
