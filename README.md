# 🎬 Movie Booking System

A simple **Movie Booking System** developed using **Python**.

This is a console-based application with two main sides:

- **Admin**
- **User**

The Admin can manage movies and shows, view bookings, and check seat availability.

The User can view movies, view showtimes, book tickets, select seats, and view booking details.

---

# 📌 Project Objective

The main objective of this project is to create a simple movie ticket booking system using Python.

The system handles:

- Movies
- Shows
- Screens
- Seats
- Ticket Prices
- Bookings

---

# 🛠️ Technology Used

- Python

---

# 🧠 Python Concepts Used

This project uses the following Python concepts:

### 1. Variables

Variables are used to store values such as:

- Movie name
- Date
- Time
- Screen
- Price
- User choice
- Seat count
- Booking details

Example:

    movie_name = input("Enter movie name: ")

---

### 2. Lists

Lists are used to store multiple values.

Examples:

    movies = ['BAHUBALI', 'RRR']

    bookings = []

    screen1_seats = [
        "A1", "A2", "A3", "A4", "A5"
    ]

Lists are used for:

- Movies
- Bookings
- Seats
- Show data

---

### 3. Dictionaries

Dictionaries are used to store data using key-value pairs.

Example:

    show = {
        "movie": "RRR",
        "date": "25-09-2026",
        "time": "06:00 PM",
        "screen": "Screen 1",
        "price": 200,
        "seats": [...]
    }

Booking details are also stored using dictionaries.

---

### 4. List of Dictionaries

The `shows` list contains multiple dictionaries.

Example:

    shows = [
        {
            "movie": "RRR",
            "date": "25-09-2026",
            "time": "06:00 PM"
        }
    ]

This is used to store multiple movie shows.

---

### 5. Dictionary of Lists / Nested Data

Each show dictionary contains its own `seats` list.

Example:

    {
        "movie": "RRR",
        "seats": [
            "A1", "A2", "A3"
        ]
    }

This allows every show to have its own seat status.

---

### 6. Functions

Functions are used to divide the application into different modules.

Examples:

    movie_booking()
    admin_login()
    admin_menu()
    add_movie()
    remove_movie()
    display_movies()
    add_show()
    remove_show()
    display_shows()
    manage_seats()
    view_bookings()
    user_login()
    user_display_movies()
    user_display_shows()
    user_book_tickets()
    user_seat()
    user_view_booking()

---

### 7. Function Definition using `def`

Functions are created using the `def` keyword.

Example:

    def add_movie():
        ...

---

### 8. Function Parameters and Arguments

Parameters are used to pass data into functions.

Example:

    def admin_login(admin_username, admin_password):

Here:

- `admin_username` is a parameter.
- `admin_password` is a parameter.

Arguments are passed when calling the function.

---

### 9. Return Statement

`return` is used to stop a function and return control.

Example:

    return

---

### 10. Conditional Statements

The project uses:

- `if`
- `elif`
- `else`

Example:

    if movie_name in movies:
        print("Movie already exists.")
    else:
        movies.append(movie_name)

---

### 11. For Loop

`for` loops are used to go through items in lists.

Example:

    for movie in movies:
        print(movie)

---

### 12. While Loop

`while` loops are used when an operation needs to continue until a condition becomes false.

Example:

    while count > 0:
        ...

---

### 13. Nested Loops

A loop is used inside another loop.

Example:

    while True:
        for show in shows:
            ...

Nested loops are used in operations such as removing all shows related to a movie.

---

### 14. Recursion

Some functions call themselves again to continue the application flow.

Examples:

    admin_menu()
    user_login()
    user_book_tickets()

---

### 15. User Input

The `input()` function is used to get information from the Admin and User.

Example:

    movie_name = input("Enter movie name: ").upper()

---

### 16. Type Casting

`int()` is used to convert user input from a string to an integer.

Example:

    choice = int(input("Enter your choice: "))

---

### 17. String Methods

The project uses string methods such as:

- `.upper()`
- `.lower()`

Examples:

    movie_name = input("Enter movie name: ").upper()

    choice = input("Enter choice: ").lower()

---

### 18. List Methods

The project uses list methods such as:

- `append()`
- `remove()`
- `index()`

Examples:

    movies.append(movie_name)

    movies.remove(movie_name)

    idx = seats.index(seat)

---

### 19. Membership Operator

The `in` operator is used to check whether an item exists in a list.

Example:

    if movie_name in movies:

---

### 20. Comparison Operators

The project uses:

- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`

Example:

    if seat_no > available_seats:

---

### 21. Logical Operators

The project uses the `and` operator to combine multiple conditions.

Example:

    if (
        show["movie"] == movie_name
        and show["date"] == date
        and show["time"] == time
        and show["screen"] == screen
    ):

---

### 22. `len()` Function

`len()` is used to find the number of items.

Example:

    len(selected_seats)

---

### 23. `break`

`break` is used to stop a loop.

Example:

    if admin_choice.lower() != 'y':
        break

---

### 24. `continue`

`continue` is used to skip the current iteration and continue with the next iteration.

Example:

    if choice.lower() == 'y':
        continue

---

### 25. F-Strings

F-strings are used to display dynamic values.

Example:

    print(f"{movie_name} has been added to the list.")

---

### 26. Dictionary Access

Dictionary values are accessed using keys.

Examples:

    show["movie"]
    show["date"]
    show["time"]
    show["screen"]
    show["price"]
    show["seats"]

---

### 27. Global Data

The application data is created outside the functions and is accessed by multiple functions.

Examples:

    movies
    bookings
    shows
    screen1_seats
    screen2_seats

---

### 28. Mutable Data

Lists and dictionaries are mutable, so their values can be changed during program execution.

Example:

    seats[idx] = 'Bk'

This changes a selected seat to a booked seat.

---

# 🏗️ Project Architecture

    MOVIE BOOKING SYSTEM
             |
             v
    movie_booking()
             |
       +-----+-----+
       |           |
       v           v
     ADMIN        USER
       |           |
       v           v
    admin_menu()  user_login()
       |           |
       |       +---+---+---+---+
       |       |   |   |   |   |
       |       v   v   v   v   v
       |     Movies Shows Booking View Exit
       |
       +---- Add Movie
       |
       +---- Remove Movie
       |
       +---- Display Movies
       |
       +---- Add Show
       |
       +---- Remove Show
       |
       +---- Display Shows
       |
       +---- Manage Seats
       |
       +---- View Bookings

---

# 📂 Main Data

## Movies

    movies = ['BAHUBALI', 'RRR']

The `movies` list stores movie names.

## Bookings

    bookings = []

The `bookings` list stores completed ticket booking details.

## Screen Seats

Two screens are available:

    Screen 1
    Screen 2

Each screen currently has 15 seats:

    A1 A2 A3 A4 A5
    B1 B2 B3 B4 B5
    C1 C2 C3 C4 C5

---

# 🎥 Show Data

Each show contains:

    Movie
    Date
    Time
    Screen
    Price
    Seats

Example:

    Movie  : RRR
    Date   : 25-09-2026
    Time   : 06:00 PM
    Screen : Screen 1
    Price  : 200

Each show has its own seat list.

---

# 🔄 Complete System Workflow

    START
      |
      v
    movie_booking()
      |
      +----------------------+
      |                      |
      v                      v
    ADMIN                   USER
      |                      |
      v                      v
    Admin Login            User Menu
      |                      |
      v                +-----+-----+-----+------+
    Admin Menu          |     |     |     |      |
      |                 |     |     |     |      |
      |                 v     v     v     v      v
      |               Movies Shows Booking View  Exit
      |
      +---- Add Movie
      |
      +---- Remove Movie
      |
      +---- Display Movies
      |
      +---- Add Show
      |
      +---- Remove Show
      |
      +---- Display Shows
      |
      +---- Manage Seats
      |
      +---- View Bookings
      |
      +---- Exit

---

# 👨‍💼 Admin Module

The Admin side is used to manage movies and shows, check seat availability, and view bookings.

## Admin Login

Default credentials:

    Username: 123
    Password: 123

### Admin Login Workflow

    Main Menu
        |
        v
      Admin
        |
        v
    Enter Username
        |
        v
    Enter Password
        |
        v
    Validate Credentials
        |
        +------ Valid ------> Admin Menu
        |
        +------ Invalid ----> Main Menu

---

# 🧑‍💼 Admin Menu

    1. Add Movie
    2. Remove Movie
    3. Display Movies
    4. Add Show
    5. Remove Show
    6. Display Shows
    7. Manage Seats
    8. View Bookings
    9. Exit

---

# 🎞️ Add Movie

The Admin can add a new movie.

### Workflow

    Admin Menu
        |
        v
    Add Movie
        |
        v
    Enter Movie Name
        |
        v
    Check Movie Exists
        |
        +------ Yes ------> Movie Already Exists
        |
        +------ No -------> Add Movie
                              |
                              v
                      Add Another Movie?
                              |
                        +-----+-----+
                        |           |
                       Yes          No
                        |           |
                        v           v
                    Add Again   Admin Menu

Duplicate movie names are prevented.

---

# 🗑️ Remove Movie

The Admin can remove a movie.

When a movie is removed, its related shows are also removed.

### Workflow

    Admin Menu
        |
        v
    Remove Movie
        |
        v
    Enter Movie Name
        |
        v
    Check Movie
        |
        +------ Not Found ------> Display Error
        |
        +------ Found ----------> Remove Movie
                                      |
                                      v
                              Find Related Shows
                                      |
                                      v
                              Remove All Shows
                                      |
                                      v
                                 Admin Menu

---

# 📋 Display Movies

The Admin can display all available movies.

### Workflow

    Admin Menu
        |
        v
    Display Movies
        |
        v
    Show All Movies
        |
        v
    Admin Menu

---

# 🎟️ Add Show

The Admin can create a show for a movie.

The Admin enters:

    Movie
    Date
    Time
    Screen
    Price

The system creates a seat list for the selected screen.

### Workflow

    Admin Menu
        |
        v
    Add Show
        |
        v
    Enter Movie
        |
        v
    Check Movie
        |
        v
    Enter Date
        |
        v
    Enter Time
        |
        v
    Enter Screen
        |
        v
    Validate Screen
        |
        v
    Check Screen Availability
        |
        v
    Enter Ticket Price
        |
        v
    Create Seat List
        |
        v
    Create Show
        |
        v
    Add Show
        |
        v
    Admin Menu

---

# ⏰ Show Availability

A screen cannot be assigned to another show at the same:

    Date
    Time
    Screen

Example:

    Movie  : RRR
    Date   : 25-09-2026
    Time   : 09:00 PM
    Screen : Screen 2

If the same screen is already occupied at the same date and time, the new show is rejected.

---

# ❌ Remove Show

The Admin can remove an exact show using:

    Movie
    Date
    Time
    Screen

### Workflow

    Admin Menu
        |
        v
    Remove Show
        |
        v
    Enter Movie
        |
        v
    Enter Date
        |
        v
    Enter Time
        |
        v
    Enter Screen
        |
        v
    Find Exact Show
        |
        +------ Found ------> Remove Show
        |
        +------ Not Found --> Show Error

---

# 💺 Manage Seats

The current `manage_seats()` function is used by the Admin to check the available seats for a particular show.

The Admin selects:

    Movie
    Date
    Time
    Screen

Then the system displays the available seats.

### Workflow

    Admin Menu
        |
        v
    Manage Seats
        |
        v
    Select Movie
        |
        v
    Select Date
        |
        v
    Select Time
        |
        v
    Select Screen
        |
        v
    Find Show
        |
        v
    Display Available Seats

Example:

    Available Seats:

    A1 A2 A3 A4 A5
    B1 B2 B3 B4 B5
    C1 C2 C3 C4 C5

Booked seats are internally marked as:

    Bk

Note: The current implementation checks and displays seat availability. It does not modify the seat layout.

---

# 📋 View Bookings - Admin

The Admin can view all completed bookings.

Each booking contains:

    Movie
    Date
    Time
    Screen
    Seats
    Amount

Example:

    Movie: RRR
    Date: 25-09-2026
    Time: 06:00 PM
    Screen: Screen 1
    Seats: ['A1', 'A2']
    Amount: 400

### Workflow

    Admin Menu
        |
        v
    View Bookings
        |
        v
    Check Bookings
        |
        +------ Empty ------> No Bookings Found
        |
        +------ Available --> Display Booking Details
        |
        v
    Admin Menu

---

# 👤 User Module

The User side allows customers to interact with the booking system.

## User Menu

    1. View Movies
    2. View Showtimes
    3. Book Tickets
    4. View Booking
    5. Exit

---

# 🎬 View Movies - User

The User can view all available movies.

### Workflow

    User Menu
        |
        v
    View Movies
        |
        v
    Display Movies
        |
        v
    Ask Return to Menu

Example:

    BAHUBALI
    RRR

---

# 🕒 View Showtimes - User

The User can view all available shows.

Each show displays:

    Movie
    Date
    Time
    Screen
    Price

Example:

    Movie: RRR
    Date: 25-09-2026
    Time: 06:00 PM
    Screen: Screen 1
    Price: 200

### Workflow

    User Menu
        |
        v
    View Showtimes
        |
        v
    Display All Shows
        |
        v
    User Menu

---

# 🎟️ Book Tickets

Ticket booking is the main feature of the project.

### Workflow

    User Menu
        |
        v
    Book Tickets
        |
        v
    Display Movies
        |
        v
    Enter Movie
        |
        v
    Check Movie
        |
        v
    Display Shows for Movie
        |
        v
    Enter Date
        |
        v
    Enter Time
        |
        v
    Find Selected Show
        |
        v
    Display Available Seats
        |
        v
    Enter Number of Seats
        |
        v
    Validate Number of Seats
        |
        v
    Select Seats
        |
        v
    Mark Seats as Booked
        |
        v
    Calculate Amount
        |
        v
    Create Booking
        |
        v
    Store Booking
        |
        v
    User Menu

---

# 💺 Seat Booking Workflow

The User first selects the number of seats.

Example:

    How many seats do you want to book: 2

Then the User selects:

    A1
    A2

The selected seats are changed internally to:

    Bk

This prevents booked seats from being selected again.

---

# ✅ Seat Validation

The system checks:

    Number of seats must be greater than 0
    Number of seats cannot exceed available seats
    Booked seats cannot be selected

Example:

    Available Seats = 10

    Enter 0
    -> Rejected

    Enter 15
    -> Rejected

    Enter 2
    -> Booking continues

---

# 💰 Amount Calculation

The total ticket amount is calculated using:

    Number of Seats × Ticket Price

Example:

    2 Seats × ₹200
    =
    ₹400

---

# 🧾 Booking Data

After successful booking, the booking contains:

    Movie
    Date
    Time
    Screen
    Selected Seats
    Amount

Example:

    {
        "movie": "RRR",
        "date": "25-09-2026",
        "time": "06:00 PM",
        "screen": "Screen 1",
        "seats": ["A1", "A2"],
        "amount": 400
    }

The booking is then added to:

    bookings

---

# 📖 View Booking - User

The User can view booking details.

Displayed information:

    Movie
    Date
    Time
    Screen
    Seats
    Amount

### Workflow

    User Menu
        |
        v
    View Booking
        |
        v
    Check Booking List
        |
        +------ Empty ------> No Bookings Found
        |
        +------ Available --> Display Booking Details
        |
        v
    User Menu

---

# 🧠 Data Flow

The main relationship between the project data is:

    Movies
       |
       v
    Shows
       |
       v
    Seats
       |
       v
    Booking

More specifically:

    Movie
      |
      +---- Show 1
      |       |
      |       +---- Date
      |       +---- Time
      |       +---- Screen
      |       +---- Price
      |       +---- Seats
      |
      +---- Show 2
              |
              +---- Date
              +---- Time
              +---- Screen
              +---- Price
              +---- Seats

When the User selects a show, the seat list belonging to that show is used for booking.

---

# 🔐 Input Validation

The project contains validation for:

### Admin Login

    Username
    Password

### Movies

    Duplicate movie checking

### Shows

    Screen validation
    Screen/date/time availability

### Seats

    Number of seats must be greater than 0
    Number of seats cannot exceed available seats
    Booked seats cannot be selected

### Menu

    Invalid user choices are handled

---

# 🧩 Functions Used

## Main Function

    movie_booking()

## Admin Functions

    admin_login()
    admin_menu()
    add_movie()
    display_movies()
    remove_movie()
    add_show()
    remove_show()
    display_shows()
    manage_seats()
    view_bookings()

## User Functions

    user_login()
    user_display_movies()
    user_display_shows()
    user_book_tickets()
    user_seat()
    user_view_booking()
    user_shows()
    user_screen()

---

# 📊 Project Module Structure

    MOVIE BOOKING SYSTEM
    │
    ├── Main Module
    │   └── movie_booking()
    │
    ├── Admin Module
    │   ├── admin_login()
    │   ├── admin_menu()
    │   ├── add_movie()
    │   ├── remove_movie()
    │   ├── display_movies()
    │   ├── add_show()
    │   ├── remove_show()
    │   ├── display_shows()
    │   ├── manage_seats()
    │   └── view_bookings()
    │
    ├── User Module
    │   ├── user_login()
    │   ├── user_display_movies()
    │   ├── user_display_shows()
    │   ├── user_book_tickets()
    │   ├── user_seat()
    │   └── user_view_booking()
    │
    └── Data
        ├── movies
        ├── shows
        ├── bookings
        ├── screen1_seats
        └── screen2_seats

---

# 🖥️ Main Application Flow

    =================================
       WELCOME TO MOVIE BOOKING SYSTEM
    =================================

    1. Admin
    2. User
    3. Exit

The user selects the required option.

---

# 👨‍💼 Admin Flow

    Main Menu
        |
        v
    Admin Login
        |
        v
    Admin Menu
        |
        +---- Add Movie
        |
        +---- Remove Movie
        |
        +---- Display Movies
        |
        +---- Add Show
        |
        +---- Remove Show
        |
        +---- Display Shows
        |
        +---- Manage Seats
        |
        +---- View Bookings
        |
        +---- Exit

---

# 👤 User Flow

    Main Menu
        |
        v
    User Menu
        |
        +---- View Movies
        |
        +---- View Showtimes
        |
        +---- Book Tickets
        |        |
        |        +---- Select Movie
        |        +---- Select Show
        |        +---- Select Seats
        |        +---- Calculate Amount
        |        +---- Save Booking
        |
        +---- View Booking
        |
        +---- Exit

---

# ✅ Current Features

    ✔ Admin Login
    ✔ User Menu
    ✔ Add Movie
    ✔ Remove Movie
    ✔ Display Movies
    ✔ Add Show
    ✔ Remove Show
    ✔ Display Shows
    ✔ Screen Selection
    ✔ Screen Availability Check
    ✔ Seat Availability
    ✔ Seat Booking
    ✔ Booked Seat Validation
    ✔ Ticket Price Calculation
    ✔ Booking Storage
    ✔ Admin Booking View
    ✔ User Booking View

---

# 🚀 Future Improvements

The project can later be extended with:

    User Registration
    User Login
    User-Specific Booking History
    Cart System
    Payment System
    Booking Cancellation
    Database Integration
    More Screens
    More Seat Rows
    Advanced Seat Management
    Better Input Validation
    Improved Menu Navigation

---

# ▶️ How to Run

### Step 1

Install Python on your system.

### Step 2

Save the Python file as:

    movie_booking.py

### Step 3

Open the terminal in the project folder.

### Step 4

Run the program:

    python movie_booking.py

### Step 5

Select:

    1. Admin
    2. User
    3. Exit

---

# 👨‍💻 Author

**Chandra Sekhar Sadhu**

B.Tech - Artificial Intelligence and Machine Learning

---

# 📌 Project Summary

The Movie Booking System is a Python-based console application that manages:

    Movies
    Shows
    Screens
    Seats
    Ticket Prices
    Bookings

The Admin manages movies and shows, checks seat availability, and views bookings.

The User can view movies, view showtimes, select seats, book tickets, and view booking information.

### Main Workflow

    Movie
       ↓
    Show
       ↓
    Seat Selection
       ↓
    Ticket Booking
       ↓
    Booking Details