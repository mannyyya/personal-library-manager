print("___________Personal Library Management___________")

books = []
book = {}

features = ["add book", "view books", "search book", "delete book", "update books", "save library", "load library", "total books", "by_genre", "exit"  ]

def add():
    title = input("enter the name of the book: ")
    author = input("enter the name of the author: ")
    year = input("enter the year of the book: ")
    genre = input("enter the genre of the book: ")
    book = {"title" : (title), 
            "author" : (author),
            "year" : (year),
            "genre" : (genre)}
    books.append(book)

def view():
    for book in books:
        for key,value in book.items():
            print(key, ":", value)

def search():
    title = input("enter the name of the book: ")
    found = False
    for book in books:
        if book["title"].lower() == title.lower():
            found = True
            print("Found")
            for key,value in book.items():
                print(key, ":", value)
    if not found:
        print("Not Found")

def delete():
    title = input("enter the name of the book: ")
    found = False
    for book in books:
        if book["title"].lower() == title.lower():
            found = True
            print("Found")
            books.remove(book)
            print("the given book is deleted")
            break
    if not found:
        print("not found")
    
def update():
    title = input("enter the name of the book: ")
    for book in books:
        if book["title"].lower() == title.lower()
            new_author = input("enter the new author: ")
            new_year = input("enter the new year: ")
            new_genre = input("enter the new genre: ")
            book["author"] = new_author
            book["year"] = new_year
            book["genre"] = new_genre

def savlib():
    file = open("library.txt","w")
    for book in books:
        line = book["title"]+","+book["author"]+","+book["year"]+","+book["genre"]+"\n"
        file.write(line)
        file.close()
        print("SUCCESSFUL")

def loadlib():
    books.clear()
    file = open("library.txt", "r")
    for line in file:
        line = line.strip()
        parts = line.split(",")
        book = {
        "title": parts[0],
        "author": parts[1],
        "year": parts[2],
        "genre": parts[3]}
        books.append(book)
    file.close()
    print("Library loaded successfully!")
    
def total():
    count = 0
    for book in books:
        count += 1
    print(f"{count} books")

def genre_by():
    freq={}
    genre = book["genre"]
    for book in books:
        for genre in book:
            if genre in freq:
                freq[genre] += 1
            else:
                freq[genre] = 1
    print(freq)

def quit():
    print("Thank you for visting our library")

while True: 
    print("FEATURES")
    for x, feature in enumerate(features, start = 1):
        print(x, feature)
    try: 
        choice = int(input("choose form 1-10 from MENU : "))
    except ValueError:
        print("choose the correct choice for the working of the calculator")
        continue
    if choice == 1:
        add()
    elif choice == 2:
        view()
    elif choice == 3:
        search()
    elif choice == 4:
        delete()
    elif choice == 5:
        update()
    elif choice == 6:
        savlib()
    elif choice == 7:
        loadlib()
    elif choice == 8:
        total()
    elif choice == 9:
        genre_by()
    elif choice == 10:
        quit()
        break




