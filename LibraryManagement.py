#Library Management Programme 

class Library:
    def __init__(self, name):
        self.name = name
        self.books=[]

    def add_books(self, book):
        self.books.append(book)
        print(f'"{book}" was added...')
    def show_books(self):
        print(f'\n{self.name} ki books')
        if not self.books:
            print('No Book Available ')
        else:

          for book in self.books:
            print(f'- {book}')

lib = Library('Lucknow Library')

while True:
    book = input('Enter your books to add(q to quit, s to show) : ')
    if book.lower() == 'q':
        print('Programme Closed')
        break
    elif book.lower() == "s":
        print(' Your books')
        lib.show_books()
    else:
        lib.add_books(book)