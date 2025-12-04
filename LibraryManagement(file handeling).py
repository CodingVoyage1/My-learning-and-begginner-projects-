#Library Management System v2.0 (File Handling)

class Library:
    def __init__(self, name):
        self.name = name 
        self.kitaabs = []

        try:
            with open("bookdata.txt" "w") as f:
                for line in f:
                    self.kitaabs.append(line.strip())

        except FileNotFoundError:
            pass
    def add_book2(self,kitaab):
        if kitaab.strip() != "":
          with open("bookdata.txt","a") as f:
             f.write(kitaab + "\n") 
             print("Aapki Kitaab Jodi Gayi ....")
    def show_book2(self):
        print(f'\n{self.name} ki kitaabe..')
        if not self.kitaabs:
            print('Kitaabe Nahi hai ....')
        else:
            for book in self.kitaabs:
                print(book) 

lib2 = Library("Lucknow")

while True :
    book = input('Apni kitaab ka naam likhiye (q se bahar , s se book dikhana) :')

    if book.lower()=='q':
        print('Library Band...')
        break
    elif book.lower()=='s':
        print('Apki kitaabe')
        lib2.show_book2()
    else:
        lib2.add_book2(book)
    