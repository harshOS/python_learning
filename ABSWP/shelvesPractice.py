import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

file = shelve.open('mydata')
print(file['cats'])
print(type(file))
print(list(file.keys()))
print(list(file.items()))
print(list(file.values()))

file.close()



