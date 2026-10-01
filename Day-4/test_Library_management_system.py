from Library_management_system import Book, Member, Library

def test_book_creation():
    book = Book(101, "Python Basics", "John Smith")
    assert book.book_id == 101
    assert book.title == "Python Basics"
    assert book.author == "John Smith"
    assert book.available is True
    
def test_book_is_borrowed():
    book = Book(101, "Python Basics", "John Smith")
    assert book.is_borrowed() is False
    book.available = False
    assert book.is_borrowed() is True
    
def test_member_creation():
    member = Member(1, "Ananya")
    assert member.member_id == 1
    assert member.name == "Ananya"
    assert member.books_borrowed == {}
    
def test_library_creation():
    library = Library()
    assert library.books == []
    assert library.members == []
    
def test_add_book_to_library():
    library = Library()
    book = Book(101, "Python Basics", "John Smith")
    library.books.append(book)
    assert book in library.books
    assert len(library.books) == 1
    
def test_add_member_to_library():
    library = Library()
    member = Member(1, "Ananya")
    library.members.append(member)
    assert member in library.members
    assert len(library.members) == 1
    
def test_borrow_book():
    library = Library()
    book = Book(101, "Python Basics", "John Smith")
    member = Member(1, "Ananya")
    library.books.append(book)
    library.members.append(member)
    library.borrow_book(book, member)
    assert book.available is False
    assert member.books_borrowed == {101: "Python Basics"}
    
def test_borrow_already_borrowed_book():
    library = Library()
    book = Book(101, "Python Basics", "John Smith")
    member = Member(1, "Ananya")
    library.books.append(book)
    library.members.append(member)
    library.borrow_book(book, member)
    result = library.borrow_book(book, member)
    assert result == "Book already borrowed..."
    
def test_return_book():
    library = Library()
    book = Book(101, "Python Basics", "John Smith")
    member = Member(1, "Ananya")
    library.books.append(book)
    library.members.append(member)
    library.borrow_book(book, member)
    library.return_book(book, member)
    assert book.available is True
    assert member.books_borrowed == {}


def test_return_book_not_borrowed():
    library = Library()
    book = Book(101, "Python Basics", "John Smith")
    member = Member(1, "Ananya")
    library.books.append(book)
    library.members.append(member)
    result = library.return_book(book, member)
    assert result == "Member didn't borrow this book..."