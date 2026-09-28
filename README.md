# 🎬 Movie Booking System

A simple **Movie Booking System** developed using **Python**.

This is a console-based application with two main sides:

- **Admin**
- **User**

The Admin manages movies, shows, and bookings and can check seat availability.

The User can view movies, view showtimes, book tickets, select seats, and view booking details.

---

# 📌 Project Objective

The main objective of this project is to create a simple movie ticket booking system using Python.

The system manages:

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

Used to store movie names, dates, times, prices, choices, seat counts, and other values.

### 2. Lists

Used to store movies, bookings, seats, and shows.

Example:

~~~python
movies = ['BAHUBALI', 'RRR']
bookings = []
~~~

### 3. Dictionaries

Used to store show and booking details using key-value pairs.

Example:

~~~python
show = {
    "movie": "RRR",
    "date": "25-09-2026",
    "time": "06:00 PM",
    "screen": "Screen 1",
    "price": 200,
    "seats": [...]
}
~~~

### 4. Functions

The project is divided into multiple functions for better organization.

Examples:

~~~python
movie_booking()
admin_login()
admin_menu()
add_movie()
remove_movie()
add_show()
remove_show()
manage_seats()
user_login()
user_seat()
user_book_tickets()
~~~

### 5. Function Parameters and Arguments

Used to pass information between functions.

Example:

~~~python
def admin_login(admin_username, admin_password):
~~~

### 6. Return Statement

Used to stop a function and return control to the calling function.

Example:

~~~python
return
~~~

### 7. Conditional Statements

The project uses:

- `if`
- `elif`
- `else`

Example:

~~~python
if movie_name in movies:
    print("Movie already exists.")
else:
    movies.append(movie_name)
~~~

### 8. For Loop

Used to iterate through lists.

Example:

~~~python
for movie in movies:
    print(movie)
~~~

### 9. While Loop

Used when a process needs to continue until a condition becomes false.

Example:

~~~python
while count > 0:
    ...
~~~

### 10. Nested Loops

Used when one loop works inside another loop.

Example:

~~~python
while True:
    for show in shows:
        ...
~~~

### 11. User Input

`input()` is used to get data from the Admin and User.

Example:

~~~python
movie_name = input("Enter movie name: ")
~~~

### 12. Type Casting

`int()` is used to convert input into an integer.

Example:

~~~python
choice = int(input("Enter your choice: "))
~~~

### 13. String Methods

The project uses:

- `.upper()`
- `.lower()`

Example:

~~~python
movie_name = input("Enter movie name: ").upper()
~~~

### 14. List Methods

The project uses methods such as:

- `append()`
- `remove()`
- `index()`

### 15. Membership Operator

The `in` operator is used to check whether a value exists in a list.

Example:

~~~python
if movie_name in movies:
~~~

### 16. Comparison Operators

The project uses:

- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`

### 17. Logical Operators

The project uses:

- `and`

Example:

~~~python
if (
    show["movie"] == movie_name
    and show["date"] == date
    and show["time"] == time
):
~~~

### 18. `len()`

Used to find the number of items.

Example:

~~~python
len(selected_seats)
~~~

### 19. `break`

Used to stop a loop.

### 20. `continue`

Used to move to the next iteration of a loop.

### 21. Recursion

Some menu functions call themselves again to continue the workflow.

Examples:

~~~python
admin_menu()
user_login()
user_book_tickets()
~~~

### 22. F-Strings

Used to display dynamic values.

Example:

~~~python
print(f"{movie_name} has been added to the list.")
~~~

### 23. Dictionary Access

Dictionary values are accessed using keys.

Example:

~~~python
show["movie"]
show["price"]
show["seats"]
~~~

### 24. Nested Data Structures

The project uses dictionaries inside lists.

Example:

~~~python
shows = [
    {
        "movie": "RRR",
        "date": "25-09-2026",
        "time": "06:00 PM"
    }
]
~~~

---

# 🏗️ Project Architecture

~~~text
                         MOVIE BOOKING SYSTEM
                                  |
                                  v
                         movie_booking()
                                  |
                     +------------+------------+
                     |                         |
                     v                         v
                   ADMIN                      USER
                     |                         |
                     v                         v
               admin_login()              user_login()
                     |                         |
                     v              +----------+----------+----------+----------+
               admin_menu()         |          |          |          |          |
                     |              v          v          v          v          v
          +----------+----------+ Movies     Shows     Booking     View       Exit
          |          |          |
          v          v          v
       Add Movie  Remove     Display
                  Movie      Movies

                     Admin Show Management
                              |
                +-------------+-------------+
                |             |             |
                v             v             v
             Add Show    Remove Show   Display Shows
                                             |
                                             v
                                        Manage Seats
                                             |
                                             v
                                        View Bookings
~~~

---

# 📂 Main Data

The project stores data using Python lists and dictionaries.

## Movies

~~~python
movies = ['BAHUBALI', 'RRR']
~~~

The `movies` list stores movie names.

## Bookings

~~~python
bookings = []
~~~

The `bookings` list stores completed ticket booking details.

## Screen Seats

Two screens are available:

~~~text
Screen 1
Screen 2
~~~

Each screen currently contains 15 seats:

~~~text
A1 A2 A3 A4 A5
B1 B2 B3 B4 B5
C1 C2 C3 C4 C5
~~~

---

# 🎥 Show Data

Each show contains:

~~~text
Movie
Date
Time
Screen
Price
Seats
~~~

Example:

~~~text
Movie  : RRR
Date   : 25-09-2026
Time   : 06:00 PM
Screen : Screen 1
Price  : 200
~~~

Each show has its own seat list.

---

# 🔄 Complete System Workflow

~~~text
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
~~~

---

# 👨‍💼 Admin Module

The Admin side is used to manage the movie booking system.

## Admin Login

Default credentials:

~~~text
Username: 123
Password: 123
~~~

### Admin Login Workflow

~~~text
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
~~~

---

# 🧑‍💼 Admin Menu

~~~text
1. Add Movie
2. Remove Movie
3. Display Movies
4. Add Show
5. Remove Show
6. Display Shows
7. Manage Seats
8. View Bookings
9. Exit
~~~

---

# 🎞️ Add Movie

The Admin can add a new movie.

### Workflow

~~~text
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
~~~

Duplicate movie names are prevented.

---

# 🗑️ Remove Movie

The Admin can remove a movie.

When a movie is removed, all shows belonging to that movie are also removed.

### Workflow

~~~text
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
~~~

---

# 📋 Display Movies

The Admin can display all available movies.

### Workflow

~~~text
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
~~~

---

# 🎟️ Add Show

The Admin can create a show for a movie.

The Admin enters:

~~~text
Movie
Date
Time
Screen
Price
~~~

The system creates a seat list for that show.

### Workflow

~~~text
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
Add Show to shows
    |
    v
Admin Menu
~~~

---

# ⏰ Show Availability

A screen cannot be occupied by another show at the same:

~~~text
Date
Time
Screen
~~~

Example:

~~~text
Movie  : RRR
Date   : 25-09-2026
Time   : 09:00 PM
Screen : Screen 2
~~~

If the same screen is already occupied at the same date and time, the new show is rejected.

---

# ❌ Remove Show

The Admin can remove an exact show using:

~~~text
Movie
Date
Time
Screen
~~~

### Workflow

~~~text
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
~~~

---

# 💺 Manage Seats

The Admin can check the seat status of a particular show.

The Admin selects:

~~~text
Movie
Date
Time
Screen
~~~

Then the system displays the available seats for that show.

### Workflow

~~~text
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
~~~

Example:

~~~text
Available Seats:

A1 A2 A3 A4 A5
B1 B2 B3 B4 B5
C1 C2 C3 C4 C5
~~~

Booked seats are internally marked as:

~~~text
Bk
~~~

---

# 📋 View Bookings - Admin

The Admin can view all completed bookings.

Each booking contains:

~~~text
Movie
Date
Time
Screen
Seats
Amount
~~~

Example:

~~~text
Movie: RRR
Date: 25-09-2026
Time: 06:00 PM
Screen: Screen 1
Seats: ['A1', 'A2']
Amount: 400
~~~

### Workflow

~~~text
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
~~~

---

# 👤 User Module

The User side allows customers to interact with the booking system.

## User Menu

~~~text
1. View Movies
2. View Showtimes
3. Book Tickets
4. View Booking
5. Exit
~~~

---

# 🎬 View Movies - User

The User can view all available movies.

### Workflow

~~~text
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
~~~

Example:

~~~text
BAHUBALI
RRR
~~~

---

# 🕒 View Showtimes - User

The User can view all available shows.

Each show displays:

~~~text
Movie
Date
Time
Screen
Price
~~~

Example:

~~~text
Movie: RRR
Date: 25-09-2026
Time: 06:00 PM
Screen: Screen 1
Price: 200
~~~

### Workflow

~~~text
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
~~~

---

# 🎟️ Book Tickets

Ticket booking is the main feature of the project.

### Workflow

~~~text
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
Mark Selected Seats as Booked
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
~~~

---

# 💺 Seat Booking Workflow

The User first selects the number of seats.

Example:

~~~text
How many seats do you want to book: 2
~~~

Then the User selects:

~~~text
A1
A2
~~~

The selected seats are changed internally to:

~~~text
Bk
~~~

This prevents the same seats from being selected again.

---

# ✅ Seat Validation

The system checks:

~~~text
Seat number must be greater than 0
Seat number cannot be greater than available seats
Booked seats cannot be selected
~~~

Example:

~~~text
Available Seats = 10

Enter 0
-> Rejected

Enter 15
-> Rejected

Enter 2
-> Booking continues
~~~

---

# 💰 Amount Calculation

The total ticket amount is calculated using:

~~~text
Number of Seats × Ticket Price
~~~

Example:

~~~text
2 Seats × ₹200
=
₹400
~~~

---

# 🧾 Booking Data

After successful booking, the booking contains:

~~~text
Movie
Date
Time
Screen
Selected Seats
Amount
~~~

Example:

~~~python
{
    "movie": "RRR",
    "date": "25-09-2026",
    "time": "06:00 PM",
    "screen": "Screen 1",
    "seats": ["A1", "A2"],
    "amount": 400
}
~~~

The booking is then added to:

~~~python
bookings
~~~

---

# 📖 View Booking - User

The User can view booking details.

Displayed information:

~~~text
Movie
Date
Time
Screen
Seats
Amount
~~~

### Workflow

~~~text
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
~~~

---

# 🧠 Data Flow

The main relationship between the project data is:

~~~text
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
~~~

More specifically:

~~~text
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
~~~

When the User selects a show, the seat list belonging to that show is used for booking.

---

# 🔐 Input Validation

The project contains validation for:

### Admin Login

~~~text
Username
Password
~~~

### Movies

~~~text
Duplicate movie checking
~~~

### Shows

~~~text
Screen validation
Screen/date/time availability
~~~

### Seats

~~~text
Number of seats must be greater than 0
Number of seats cannot exceed available seats
Booked seats cannot be selected
~~~

### Menu

~~~text
Invalid choices are handled in the user menu
~~~

---

# 🧩 Functions Used

## Main Function

~~~text
movie_booking()
~~~

## Admin Functions

~~~text
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
~~~

## User Functions

~~~text
user_login()
user_display_movies()
user_display_shows()
user_book_tickets()
user_seat()
user_view_booking()
user_shows()
user_screen()
~~~

---

# 📊 Project Module Structure

~~~text
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
~~~

---

# 🖥️ Main Application Flow

~~~text
=================================
   WELCOME TO MOVIE BOOKING SYSTEM
=================================

1. Admin
2. User
3. Exit
~~~

The user selects the required option.

---

# 👨‍💼 Admin Flow

~~~text
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
~~~

---

# 👤 User Flow

~~~text
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
~~~

---

# ✅ Current Features

~~~text
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
~~~

---

# 🚀 Future Improvements

The project can later be extended with:

~~~text
User Registration
User Login
User-Specific Booking History
Cart System
Payment System
Booking Cancellation
Database Integration
More Screens
More Seat Rows
Better Input Validation
Improved Menu Navigation
~~~

---

# ▶️ How to Run

### Step 1

Install Python on your system.

### Step 2

Save the Python file as:

~~~text
movie_booking.py
~~~

### Step 3

Open the terminal in the project folder.

### Step 4

Run the program:

~~~bash
python movie_booking.py
~~~

### Step 5

Select:

~~~text
1. Admin
2. User
3. Exit
~~~

---

# 👨‍💻 Author

**Chandra Sekhar Sadhu**

B.Tech - Artificial Intelligence and Machine Learning

---

# 📌 Project Summary

The Movie Booking System is a Python-based console application that manages:

~~~text
Movies
Shows
Screens
Seats
Ticket Prices
Bookings
~~~

The Admin manages movies, shows, and bookings and can check seat availability.

The User can view movies, view showtimes, select seats, book tickets, and view booking information.

### Main Workflow

~~~text
Movie
   ↓
Show
   ↓
Seat Selection
   ↓
Ticket Booking
   ↓
Booking Details
~~~