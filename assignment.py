class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self._pages = pages  # Encapsulated attribute

    def read(self):
        print(f"Reading '{self.title}' by {self.author}.")

    def get_pages(self):
        return self._pages

class EBook(Book):
    def __init__(self, title, author, pages, filesize):
        super().__init__(title, author, pages)
        self.filesize = filesize

    def download(self):
        print(f"Downloading '{self.title}' ({self.filesize}MB).")

# Example usage:
book1 = Book("1984", "George Orwell", 328)
ebook1 = EBook("Digital Fortress", "Dan Brown", 356, 2)

book1.read()
print("Pages:", book1.get_pages())
ebook1.read()
ebook1.download()

