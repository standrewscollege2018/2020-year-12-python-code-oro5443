#list order name, price, author
bookstore = [["the bible", 0, "jesus christ"], ["the quran", 0, "muhammad"]]
options = ["VIEW", "ADD", "EDIT", "REMOVE"]

def book_add():
    print("what is the title of the book you want to add?")
    book_add = input()
    bookstore.append(book_add)
    print("what is the price of the book you want to add?")
    book_price = int(input())
    print(bookstore)

def book_edit():
    print("what is the title of the book you want to edit?")
    print(bookstore[0][0]) 
    print("what is the part you want to edit?")
    print("0) title")
    print("1) price")
    print("2) author")
    

menu = True
print("welcome to the bookstore administration")
while menu == True:
    print("would you like to view, add, edit or remove books?")
    option = input()
    option = option.upper()
    print(option)
    if option in options:
        menu = False
        if option == "VIEW":
            print(bookstore)
        elif option == "ADD":
            book_add()
        elif option == "EDIT":
            book_edit()
        elif option == "REMOVE":
            print()
    else:
        print("invalid entry")
