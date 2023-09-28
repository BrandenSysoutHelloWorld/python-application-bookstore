# IMPORTS
import sqlite3

# BOOK CLASS
class Book:
    def __init__(self, id=int(), title=str(), author=str(), quantity=int()):
        self.id = id
        self.title = title
        self.author = author
        self.quantity = quantity
    
    # UPDATE BOOK OBJECT
    def update_book(self, option, updated_record):
        match option:
            case 'title':
                self.title = updated_record
                print(f"SUCCESSFULLY UPDATED BOOK's TITLE TO: {self.title}")
            case 'author':
                self.author = updated_record
                print(f"SUCCESSFULLY UPDATED BOOK's AUTHOR TO: {self.author}")             
            case 'quantity':
                self.quantity = updated_record
                print(f"SUCCESSFULLY UPDATED BOOK's QUANTITY TO: {self.quantity}")
            case _:
                print("Invalid Record Type!")
    
    def __str__(self):
        output = f'''
{self.id} | BOOK TITLE: {self.title}
        AUTHOR: {self.author}
        QUANTITY(Current Stock): {self.quantity}
'''
        return output

# LIST TO STORE BOOKS
books = []

# LOAD DATA INTO MEMORY
def load_books():
    # SEED DATA WITH BOOK OBJECT & APPEND THE BOOKS LIST
    book_obj = Book(id=3001, title="A Tale of Two Cities", author="Charles Dickens", quantity=30)
    books.append(book_obj)    
    book_obj = Book(id=3002, title="Harry Potter and the P", author="J.K. Rowling", quantity=40)
    books.append(book_obj)
    book_obj = Book(id=3003, title="The Lion, the Witch and the Wardrobe", author="C.S. Lewis", quantity=25)
    books.append(book_obj)
    book_obj = Book(id=3004, title="The Lord of the Rings", author="J.R.R. Tolkien", quantity=37)
    books.append(book_obj)
    book_obj = Book(id=3005, title="Alice in Wonderland", author="Lewis Carroll", quantity=12)
    books.append(book_obj)

# LOAD DATABASE SNAPSHOT & DATA IS DERIVED FROM BOOKS LIST
def load_snapshot():
    try:
        # CONNECTION TO DATABASE & INITIALIZE CURSOR VARIABLE
        conn = sqlite3.connect('ebookstore.db')
        cursor = conn.cursor()

        # CREATE BOOKS TABLE
        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                       id INTEGER PRIMARY KEY,
                       Title TEXT,
                       Author TEXT,
                       Qty INTEGER)''')
        
        # INSERT BOOK DATA INTO BOOKS TABLE
        for book in books:           
            cursor.execute('''INSERT INTO books(id, Title, Author, Qty) VALUES(?, ?, ?, ?)''', (book.id, book.title, book.author, book.quantity))
        
        # CLOSE CURSOR OBJ
        cursor.close()

    # HANDLE ERRORS PROPERLY!
    except sqlite3.Error as error:
        print('\n')

# ADD A NEW BOOK TO DATABASE & LIST
def add_book():
    print('\n\n-------------\n[ADD] A NEW BOOK:')

    while True:
        try:
            # PROMPT USER FOR BOOK DETAILS
            new_id = int(input("Please enter a numeric value for: Book ID\n> "))
            # CHECK THAT THE ID IS NOT A DUPLICATE
            duplicate_flag = False
            for book in books:
                if new_id == book.id:
                    duplicate_flag = True
                    print("Book [ID] Already Exists! Please Try Again...")
                    break 
            if duplicate_flag == True:
                continue        
            new_title = str(input("Please enter the Title of the Book\n> "))
            new_author = str(input("Please enter the Author of the Book\n> "))
            new_quantity = int(input("Please enter a numeric value for: Book Stock Quantity\n> "))
            break
        except:
            print("INVALID VALUE ENTERED! Please Try Again...")
            continue

    # CREATE NEW BOOK OBJECT
    new_book = Book(id=new_id, title=new_title, author=new_author, quantity=new_quantity)
    
    # APPEND NEW BOOK OBJECT TO LIST & UPDATE DATABASE
    books.append(new_book)
    try:
        # CONNECTION TO DATABASE & INITIALIZE CURSOR VARIABLE
        conn = sqlite3.connect('ebookstore.db')
        cursor = conn.cursor()
        print('INITIALIZED DATABASE SUCCESSFULLY!')

        # INSERT BOOK DATA INTO BOOKS TABLE
        cursor.execute('''INSERT INTO books(id, Title, Author, Qty) VALUES(?, ?, ?, ?)''', (new_book.id, new_book.title, new_book.author, new_book.quantity))
    
    # HANDLE ERRORS PROPERLY!
    except sqlite3.Error as error:
        print('Error occurred - ', error)  
        return 500
    
    print("SUCCESSFULLY ADDED NEW BOOK!")
    print(new_book)
    return 200
    
# UPDATE A BOOK & IT'S INFORMATION
def update_book():
    print('\n\n-------------\n[UPDATE] A BOOK:')
    while True:
        my_flag = False
        # PROMPT USER FOR BOOK ID
        book_id = int(input("Please Enter book [ID]\n> "))

        # BOOK OBJECT VARIABLE
        selected_book = Book(None)

        # ITERATE OVER BOOK OBJECTS IN BOOKS LIST
        for book in books:
            # WHEN BOOK IS FOUND
            if book.id == book_id:
                my_flag = True
                print(book)
                print("UPDATE THIS BOOK? (yes / no)")
                update_proceed = input("> ")
                # ENSURE THAT THE BOOK SELECTED IS THE DESIRED OUTCOME
                if update_proceed.lower() == "yes":
                    selected_book = book
                    break
                else:
                    print("CANCELED BOOK UPDATE! Returning back to Main-Menu...")
                    return main_menu()
        
        # CHECK IF BOOK WAS FOUND
        if my_flag != True:
            print(f"Unable to locate a book with the [ID]: {book_id}!\nPlease Try Again...")
            continue
        else:                
            break

    while True:
        # PRINT UPDATE MENU
        print("Please select an option to preform a book update")        
        print("UPDATE-MENU")
        print("1. UPDATE BOOK TITLE")
        print("2. UPDATE BOOK AUTHOR")
        print("3. UPDATE BOOK QUANTITY")

        # CAPTURE SELECTION
        try:
            update_selection = int(input("> "))            
        except:
            print("ERROR - Selection be a number...")
            continue
    
        # NOTIFY USER WHICH BOOK IS SELECTED
        print(f"UPDATING BOOK: {selected_book.id} | {selected_book.title}")

        # MATCH UPDATE SELECTION WITH BOOK ATTRIBUTES
        match update_selection:
            case 1:
                # PROMPT FOR UPDATED BOOK TITLE & UPDATE BOOK OBJECT
                print(f"Current Book TITLE: {selected_book.title}")
                update_title = str(input("Enter the Updated Book TITLE\n> "))
                selected_book.update_book('title', update_title)
            case 2:
                # PROMPT FOR UPDATED BOOK AUTHOR & UPDATE BOOK OBJECT
                print(f"Current Book AUTHOR: {selected_book.author}")
                update_author = str(input("Enter the Updated Book AUTHOR\n> "))
                selected_book.update_book('author', update_author)
            case 3:
                # PROMPT FOR UPDATED BOOK QUANTITY & UPDATE BOOK OBJECT
                print(f"Current Book QUANTITY: {selected_book.quantity}")
                update_quantity = str(input("Enter the Updated Book QUANTITY\n> "))
                selected_book.update_book('quantity', update_quantity)           
            case _:
                print("INVALID SELECTION! Returning to Main-Menu...")
                return 404    
                    
        # LOAD SNAPSHOT IN ORDER TO SAVE CHANGES TO DATABASE
        load_snapshot()

        # PROMPT USER TO CONTINUE EDITING THE SELECTED BOOK - HANDLE THE SELECTION
        print(f"Continue Editing Book: {selected_book.id} | {selected_book.title}? (yes / no)")
        update_continue = input("> ")
        if update_continue == "yes":
            continue
        else:
            print("EXITED UPDATE MODE! Returning to Main-Menu...")
            return 200              

# DELETE A BOOK FROM LIST & DATABASE
def delete_book():
    print('\n\n-------------\n[DELETE] A BOOK:')
    while True:
        my_flag = False
        # PROMPT USER FOR BOOK ID
        book_id = int(input("Please Enter book [ID]\n> "))

        # BOOK OBJECT VARIABLE
        selected_book = Book(None)

        # ITERATE OVER BOOK OBJECTS IN BOOKS LIST
        for book in books:
            # WHEN BOOK IS FOUND
            if book.id == book_id:
                my_flag = True
                print(book)
                print("DELETE THIS BOOK? (yes / no)")
                update_proceed = input("> ")
                # ENSURE THAT THE BOOK SELECTED IS THE DESIRED OUTCOME
                if update_proceed.lower() == "yes":
                    books.pop(books.index(book))
                    print("Successfully Deleted Book!")
                    break
                else:
                    print("CANCELED BOOK DELETE! Returning back to Main-Menu...")
                    return main_menu()
        
        # CHECK IF BOOK WAS FOUND
        if my_flag != True:
            print(f"Unable to locate a book with the [ID]: {book_id}!\nPlease Try Again...")
            continue
        else:                
            break
    
    return main_menu()

# SEARCH FUNCTION TO SEARCH FOR A BOOK BY TITLE OR ID
def search_books():
    print("SEARCH FOR A BOOK.\nPlease enter a Book's [TITLE] or [ID]")
    search_term = input("> ")

    my_flag = False

    # CHECK IF THE SEARCH IS AN ID OR TITLE
    try:
        search_id = int(search_term)
        print("SEARCH RESULTS:")
        # SEARCH BY BOOK's ID
        for book in books:        
            if book.id == search_id:                
                print(book)
                my_flag = True
    except:
        search_title = str(search_term)
        print("SEARCH RESULTS:")
        # SEARCH BY BOOK's TILE
        for book in books:        
            if book.title.lower() == search_title.lower():
                my_flag = True                
                print(book)
    
    if my_flag != True:
        print("No Books Found!\n Enter any key to return to search")
        input("> ")
        search_books()
    else:
        print("Enter any key to return to Main-Menu")
        input("> ")
        return main_menu()

# PRINTS ALL BOOKS
def view_books():
    for book in books:
        print(book)

# STARTUP OF APPLICATION
def main_menu():

    # SEED DATABASE(snapshot)
    load_snapshot()

    # HANDLES USER INTERACTIONS WITH MENU & FUNCTIONS WHICH ARE MAPPED TO MAIN MENU
    while True:
        # RESPONSE VARIABLE USED TO HANDLE CERTAIN CODES RETURNED BY FUNCTIONS
        response = None
        # PRINT MENU
        print("E-BOOKSTORE - ONLINE E-BOOK MANAGEMENT SYSTEM")
        print("---------------------------------------------")
        print("MAIN-MENU:")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("0. Exit")
        print("(Please select one of the options above)")
        print("---------------------------------------------")

        # CAPTURE SELECTION     
        try:
            menu_selection = int(input("> "))
        
        # HANDLE ERRORS
        except:            
            print("INVALID SELECTION! Please Try Again...")
            continue

        # MATCH SELECTED OPTION
        match(menu_selection):
            # ENTER BOOK
            case 1:
                response = add_book()
            # UPDATE BOOK
            case 2:
                response = update_book()
            # DELETE BOOK
            case 3:
                response = delete_book()
            # SEARCH BOOKS
            case 4:
                response = search_books()
            # EXIT APPLICATION
            case 0:
                print("\n\nGOODBYE!")
                exit(code=0)
            case _:
                print("INVALID SELECTION! Please Try Again...")
                continue


        # HANDLE FUNCTION RESPONSE
        if response != 200:
            print("Oops Something Went Wrong! EXITING APPLICATION...")
            break
        else:
            continue

# INITIALIZE POPULATE BOOKS(list)
if len(books) == 0:
    load_books()
main_menu()
# END OF APPLICATION

###############################################
##### CREATED BY - BRANDEN VAN STADEN #########
''''GET IN TOUCH: brandenconnected@gmail.com'''
###############################################
