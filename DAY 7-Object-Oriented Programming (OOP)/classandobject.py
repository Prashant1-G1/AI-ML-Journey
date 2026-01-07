class Student():
    def show_name(self,name):
        print(f"Student name: {name}")
    def show_age(self,age):
        print(f"Student age: {age}")

lip=Student()#object define

lip.show_age(14),lip.show_name("Prashant")

class LibraryBook:
    def __init__(self, shelf_number, genre, book_name):
        self.shelf_number = shelf_number
        self.genre = genre
        self.book_name = book_name
        self._is_available = True   # Encapsulation (protected)

    def borrow_book(self):
        if self._is_available:
            self._is_available = False
            return f"{self.book_name} has been borrowed."
        return f"{self.book_name} is currently unavailable."

    def return_book(self):
        self._is_available = True
        return f"{self.book_name} has been returned."

    def get_status(self):
        return "Available" if self._is_available else "Borrowed"
    
book1 = LibraryBook(4, "Horror", "Alone")
book2 = LibraryBook(3, "Comedy", "Crazy Captain")

print(book1.borrow_book())
print(book1.get_status())

print(book1.borrow_book())




