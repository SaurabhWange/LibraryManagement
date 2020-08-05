class Library():
    def __init__(self,list_of_books,Library_name):
        # creating a dictionary of all books keys
        self.lend_data = {}
        self.list_of_books = list_of_books
        self.library_name = Library_name

        # adding books to dictionary
        for books in self.list_of_books:
            # none means No author have lend this book
            self.lend_data[books] = None

    def display_books(self):
        for index,books in enumerate(self.list_of_books):
            print(f"{index}){books}")

    def lend_book(self,book,author):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book] = author
            else:
                print(f"Sorry This book is lend by {self.lend_data[book]}")
        else:
            print("You have written wrong book name")

    def return_book(self,book,author):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data[book]= None
            else:
                print("Sorry but This book is not Lend")
        else:
            print("You have written wrong book name")

    def add_book(self,book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name] = None

    def delete_book(self,book_name):
        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)

def main():

    list_books = ['Cookbook','Sherlock Holmes','Chacha_chaudhary','Rich Dad and Poor Dad']
    Library_name = "Saurabh"

    Saurabh = Library(list_books,Library_name)
    print(Saurabh.lend_book( "Cookbook", "Sagar" ) )
    print( Saurabh.lend_book( "A", "Saurabh" ) )
    print( Saurabh.lend_data )
main()
