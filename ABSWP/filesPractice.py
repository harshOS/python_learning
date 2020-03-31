import os
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))