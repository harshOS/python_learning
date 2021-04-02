class Library():
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lendbooks = {}
    
    def display(self):      
        print('Below are the books available')
        for book in self.booklist:
            print(book)

    def addBook(self,bookname):
        self.booklist.append(bookname)
        print('Book : {} added successfully to list'.format(bookname))

    def lendBook(self,bookname):
        if bookname in self.booklist:
            if bookname in self.lendbooks:
                print('Book :{} is not available, book is cuurently with {}'.format(bookname,self.lendbooks.get(bookname)))
            else:
                print('Book is available Enter your name : ',end ='')
                username = input()
                self.lendbooks.update({bookname:username})
                print('You checked out book : ',bookname)
            
        else:
            print('Book not in the list, Please enter a book form list : ', self.booklist)

    def returnBook(self,bookname,username):
        if bookname in self.booklist:
            if bookname in self.lendbooks and self.lendbooks.get(bookname) != username:
                print('Book :{} is cuurently with {}, Enter valid details'.format(bookname,self.lendbooks.get(bookname)))
            else:
                self.lendbooks.pop(bookname)
                print('Book : {} Retured successfully :'.format(bookname))
            
        else:
            print('Book not in the list, Please enter a book form list : ', self.booklist)

    def removeBook(self,bookname):
        if bookname in self.booklist:
            if bookname in self.lendbooks:
                self.lendbooks.pop(bookname)
            self.booklist.remove(bookname)
            print('Book :{} removed successfully'.format(bookname))
        else:
            print('Book not in list')



if __name__ == '__main__':
    l1 = Library(['Python','Django','SQL server','php','C'],'harshith')

    while(True):
        print('Welcome to {} Library'.format(l1.name))
        print('Choose from the option below')
        print('1, View books')
        print('2, Add book')
        print('3, Lend book')
        print('4, Return book')
        print('5, Remove book')

        user_choice = input('')

        if user_choice == '1':
            l1.display()

        elif user_choice == '2':
            print('Enter book name : ', end='')
            bookname = input()
            l1.addBook(bookname)

        elif user_choice == '3':
            print('Enter the bookname : ',end = '')
            bookname = input()
            l1.lendBook(bookname)

        elif user_choice == '4':
            print('Enter the bookname : ',end = '')
            bookname = input()
            print('Enter your name : ',end = '')
            username = input()
            l1.returnBook(bookname,username)

        elif user_choice == '5':
            print('Enter the bookname : ',end = '')
            bookname = input()
            l1.removeBook(bookname)
        else:
            print("Invalid Option")
        
        print('Press c to continue and q to quit')
        user_choice2 = input()
        if user_choice2 == "q":
            exit()
        elif user_choice2 == "c":
            continue
        else:
            print("Invalid Option")

        
    