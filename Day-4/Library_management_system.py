from dataclasses import dataclass, field

@dataclass
class Book:
    book_id: int
    title: str
    author: str
    available: bool = True 
    
    def is_borrowed(self):
        if self.available:
            return False
        return True
    
    def __repr__(self):
        return f"Book(Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.available})"
    
@dataclass
class Member:
    member_id: int
    name: str
    books_borrowed: dict[int, str] = field(default_factory=dict)
    
    def __repr__(self):
        return f"Member(ID: {self.member_id}, name: {self.name}, Borrowed_books: {self.books_borrowed})"
    
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        
    def add_book(self):
        book_id = int(input("Enter Book ID: "))
        title = input("Enter book title: ")
        author = input("Enter book's author name: ")
        available = True
        book = Book(book_id, title, author, available)
        self.books.append(book)
    
    def add_member(self):
        member_id = int(input("Enter Member ID: "))
        name = input("Enter name of the member: ")
        books_borrowed = {}
        member = Member(member_id, name, books_borrowed)
        self.members.append(member)
    
    def borrow_book(self, book, member):
        if book in self.books and book.available and member in self.members:
            member.books_borrowed[book.book_id] =  book.title
            book.available = False
        elif not book.available:
            return "Book already borrowed..."
        else:
            return "Book not available..."
        
    def return_book(self, book, member):
        if member in self.members and book in self.books:
            if book.book_id in member.books_borrowed:
                del member.books_borrowed[book.book_id]
                book.available = True
            else:
                return "Member didn't borrow this book..."
        else:
            return "Book or member not valid..."