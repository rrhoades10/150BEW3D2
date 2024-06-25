# functional example of the library management system

# create a book class to set book attributes and create getters and setters where necessary
# create a series of functions that will take our book objects and store them in a dictionary
# create driver code to prompt the user for their choices

class Book:
    def __init__(self, title, author, genre):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__is_available = True

    # Getter and Setters
    def get_title(self):
        return self.__title
    # no setter for title becuase we literally cant change the title of a book...irl
    
    # getter for __is_available
    def get_availability(self):
        return self.__is_available
    
    # setter for availability
    def set_availability(self):
        # if self.__is_available is True we set it to false
        if self.get_availability():
            self.__is_available = False
        # else self.__is_available is False we set it to true
        else:
            self.__is_available = True
    # getter for author
    def get_author(self):
        return self.__author


    # getter for genre
    def get_genre(self):
        return self.__genre
    
    
    # method for borrowing a book
    def borrow_book(self):
        # if its available then we set use the setter to set it to the opposite which is False
        if self.get_availability():
            self.set_availability()
            return True #returns True that we are able to borrow the book
        return False
    
    def return_book(self):
        self.set_availability() #sets the availability back to true if its False

# functionality for adding infomration to our dictionary which is defined in the main function below
def add_book(library):
    title = input("Enter the book's title: ")
    author = input("Enter the book's author")
    genre = input("Enter the book's genre")
    book = Book(title, author, genre)
    library[title] = book #title is the key the value is the book object

def check_out(library, current_loans):
    title = input("Please enter the book you'd like to check out")
    # user will eventually come from another class - this could be a username or user id from a user object
    user = input("Please enter the library id")
    # checks if the title(key) is in the library and checking if we can borrow the book
    if title in library and library[title].borrow_book():
        current_loans[title] = user
        #               using the getter for the title
        print(f"Book {library[title].get_title()} has been checked out to {user}")
    else:
        print("Book is not available or not found")

def search_book(library):
    title = input("What is the title you're looking for? ")
    if title in library:
        book = library[title]
        print("Book found, here is some info: ")
        print(book.get_title())
        print(book.get_author())
        print(book.get_genre())
        print(book.get_availability())
    else:
        print("Sorry! That book is not in our library.")

def display_books(library):
    for book in library.values():
        #                            we dont have getters for author and genre BUT! We totally could and that would be radical
        print(f"{book.get_title()} by {book.get_author()}: {book.get_genre()}: {book.get_availability()}")

# driver code
def main():
    # dictionary will store the key as the book title and the value will be the whole book object
    library = {} #this would be fine as a list too
    current_loans = {}
    # users = {} - we dont need this now, but you will later
    while True:
        print("\n1. Add Book\n2. Checkout Book\n3. Search Book\n4. Display All Books\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            check_out(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

main()



            
