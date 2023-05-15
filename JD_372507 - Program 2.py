class Book:
    # Initialise the `Book` class
    def __init__(self, title, author, publisher, published):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.published = published

    # When this function is called, it returns the title of the book followed by the author
    def getBook(self):
        return f"{self.title} by {self.author}"
    
    # When this function is called, it returns when the book was published, and who published it
    def getPublication(self):
        return f"{self.published} - {self.publisher}"
    
    # When this function is called, it formats the title, author, publisher, and the publication date, into
    # into an easy to read way.
    def toString(self):
        return f"""
        Title: {self.title}
        Auhor: {self.author}
        Publisher: {self.publisher}
        Publication Date: {self.published}
        """

class Library:
    # This initialises the `Library` class
    def __init__(self):
        self.books = []

    # This function checks to make sure the new book doesn't already exist in the `books` list
    def indexExists(self, new):
        for book in self.books:
            if book.title == new.title and book.author == new.author:
                return True
        return False

    # This function opens the `book_details.txt` and opens and writes to the `indexed_books.txt` files
    def index(self, input, output):
        # This opens the `book_details.txt` in "read" mode
        with open(input, 'r') as file:
            for line in file:
                title, author, publisher, published = line.strip().split(',')
                book = Book(title, author, publisher, published)
                if not self.indexExists(book):
                    self.books.append(book)

        # This opens the `indexed_books.txt` in "write" mode
        with open(output, 'w') as outputFile:

            # This codeblock iterates through the `books` list and adds "[1]", "[2]", etc. to the start of each book details after the `book.toString()` function
            for i, book in enumerate(self.books):
                index = f"[{i+1}]"
                indexed = f"{index}{book.toString()}\n"

                outputFile.write(indexed)

# Create an object by calling the `Library()` class
library = Library()
# Run the `book_details.txt` file through the Library.index() function, and output the result to the `indexed_books.txt` file
library.index('book_details.txt', 'indexed_books.txt')