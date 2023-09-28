# My Bookstore Python Command Line Application

This is a Python command-line application for managing an online bookstore. It allows you to perform various useful operations such as adding, updating, deleting, searching, and viewing books in your bookstore. 

This Python Application aims to assist a bookstore owners & employees his/her day to day tasks.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Book Class](#book-class)
- [Functions](#functions)
  - [load_books](#load-books)
  - [load_snapshot](#load-snapshot)
  - [add_book](#add-book)
  - [update_book](#update-book)
  - [delete_book](#delete-book)
  - [search_books](#search-books)
  - [view_books](#view-books)
  - [main_menu](#main-menu)
- [Author](#author)

## Installation

To run the Bookstore application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/BrandenSysoutHelloWorld/python-application-bookstore.git
   cd python-application-bookstore
   ```

2. Make sure you have Python installed on your system.

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies (sqlite3 is part of the Python standard library):

   You don't need to install additional dependencies as sqlite3 is a part of the Python standard library.

6. Run the application:
   ```bash
   python bookstore.py
   ```

## Usage

The Bookstore application provides a menu-driven interface to interact with your bookstore. Here's how you can use the console menu within the `bookstore.py` script:

1. **Main Menu**:

   When you run `bookstore.py`, you'll see the main menu with the following options:

   ```
   E-BOOKSTORE - ONLINE E-BOOK MANAGEMENT SYSTEM
   ---------------------------------------------
   MAIN-MENU:
   1. Enter book
   2. Update book
   3. Delete book
   4. Search books
   5. View books
   0. Exit
   (Please select one of the options above)
   ---------------------------------------------
   ```

   To select an option, simply type the corresponding number and press Enter.

2. **Enter Book**:

   - Option 1 allows you to add a new book to your bookstore. Follow the prompts to enter the book's ID, title, author, and quantity. The book will be added to both the `books` list and the database.

3. **Update Book**:

   - Option 2 lets you update an existing book's title, author, or quantity. You'll need to enter the book's ID and choose which attribute you want to update.

4. **Delete Book**:

   - Option 3 allows you to delete a book from your bookstore. Enter the book's ID, and if confirmed, the book will be removed from both the `books` list and the database.

5. **Search Books**:

   - Option 4 enables you to search for a book by either its title or ID. Enter the search term, and the application will display matching books.

6. **View Books**:

   - Option 5 shows you a list of all the books in your bookstore, including their IDs, titles, authors, and quantities.

7. **Exit**:

   - Option 0 exits the application.

## Author

This Python command-line application was created by Branden van Staden. You can get in touch with the author at [brandenconnected@gmail.com](mailto:brandenconnected@gmail.com).

Now you can start managing your online bookstore with peace of mind!