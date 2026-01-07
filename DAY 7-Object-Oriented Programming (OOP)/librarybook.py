class LibraryBooks():
    available_book=[]
        
    def __init__(self,book_name,book_Shelf,book_genre):
        self.book_name=book_name
        self.book_shelf=book_Shelf
        self.book_genre=book_genre
        self.available=True
        LibraryBooks.available_book.append(self)
    
    def Book_Borrow(self):
        if self.available:
            self.available=False
            return f"Book named {self.book_name} has been Borrowed."
        else:
            return f"Book named {self.book_name} is currently not available"
    def Returned(self):
        self.available=True
        return f"Book named {self.book_name} has been returned succesfully"
    
    def Get_Status(self):
        return f"Book= {self.book_name} is Available" if self.available else f"Book= {self.book_name} is Unavailable"
    
    def show_available_genres(books_list):
        genres = {book.book_genre for book in books_list if book.available}
        if genres:
            return f"Available Genres: {', '.join(genres)}"
        else:
            return "No genres available right now."
    
    

    
book1=LibraryBooks("Alone",4,"Horror")
book2=LibraryBooks("The cat",8,"Comedy")

print(book1.Get_Status())
print(book1.Book_Borrow())
print(book1.Book_Borrow())
print(book1.Returned())
print(book1.Get_Status())
print(LibraryBooks.show_available_genres())
