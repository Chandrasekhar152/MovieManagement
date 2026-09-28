movies = ['BAHUBALI', 'RRR']
bookings = []

screen1_seats = [
    "A1", "A2", "A3", "A4", "A5",
    "B1", "B2", "B3", "B4", "B5",
    "C1", "C2", "C3", "C4", "C5"
]

screen2_seats = [
    "A1", "A2", "A3", "A4", "A5",
    "B1", "B2", "B3", "B4", "B5",
    "C1", "C2", "C3", "C4", "C5"
]

shows = [
    {
    "movie": "RRR",
    "date": "25-09-2026",
    "time": "06:00 PM",
    "screen": "Screen 1",
    "price": 200,
    "seats": [
        "A1", "A2", "A3", "A4", "A5",
        "B1", "B2", "B3", "B4", "B5",
        "C1", "C2", "C3", "C4", "C5"
    ]
},

    {
        'movie': "RRR",
        'date': "25-09-2026",
        'time': "09:00 PM",
        'screen': "Screen 2",
        'price': 250,
        "seats": [
        "A1", "A2", "A3", "A4", "A5",
        "B1", "B2", "B3", "B4", "B5",
        "C1", "C2", "C3", "C4", "C5"
    ]
    },

    {
        "movie": "RRR",
        "date": "26-09-2026",
        "time": "08:00 PM",
        "screen": "Screen 1",
        "price": 200,
        "seats": [
        "A1", "A2", "A3", "A4", "A5",
        "B1", "B2", "B3", "B4", "B5",
        "C1", "C2", "C3", "C4", "C5"
    ]
    },

    
    {
        "movie": "BAHUBALI",
        "date": "30-09-2026",
        "time": "07:00 PM",
        "screen": "Screen 2",
        "price": 250,
        "seats": [
        "A1", "A2", "A3", "A4", "A5",
        "B1", "B2", "B3", "B4", "B5",
        "C1", "C2", "C3", "C4", "C5"
    ]
    }
]

add_show_structure ={
    "movie": "BAHUBALI",
        "date": "30-09-2026",
        "time": "07:00 PM",
        "screen": "Screen 2",
        "price": 250
}

def movie_booking():
    print("================================")
    print("WELCOME TO MOVIE BOOKING SYSTEM")
    print("================================")
    print()
    print('1.Admin')
    print('2.User')
    print('3.Exit')
    print()
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Admin login")
        admin_username = input("Enter admin username: ")
        admin_password = input("Enter admin password: ")
        if admin_username == "123" and admin_password == "123":
            admin_login(admin_username, admin_password)
        else:
            print("Invalid username or password. Please try again.")
            movie_booking()
    elif choice == 2:
        print("User login")
        user_login()
    elif choice == 3:
        print("Exiting the program...")
        exit()



def admin_login(admin_username, admin_password):

    if admin_username == "123" and admin_password == "123":
        print("Admin login successful!")
        admin_menu()
    else:
        print("Invalid username or password. Please try again.")
        movie_booking()


def admin_menu():
    print("================================")
    print("ADMIN MENU")
    print("================================")
    print()
    print("1. Add Movie")
    print("2. Remove Movie")
    print("3. Display Movies")
    print("4. Add Show")
    print("5. Remove Show")
    print("6. Display Shows")
    print("7. Manage Seats")
    print("8. View Bookings")
    print("9. Exit")
    print()

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_movie()
    elif choice == 2:
        remove_movie()
    elif choice == 3:
        display_movies()
    elif choice == 4:
        add_show()
    elif choice == 5:
        remove_show()
    elif choice == 6:
        display_shows()
    elif choice == 7:
        manage_seats()
    elif choice == 8:
        view_bookings()
    elif choice == 9:
        print("Exiting admin menu...")
        movie_booking()
    else:
        print("Invalid choice")

def add_movie():
    while True:
        movie_name = input("Enter the name of the movie to add: ").upper()
        if movie_name in movies:
            print(f"{movie_name} is already in the list.")
        else:
            movies.append(movie_name)
            print(f"{movie_name} has been added to the list.")
        admin_choice = input("Do you want to add another movie? (y/n): ")
        if admin_choice.lower() != 'y':
            break
        
    admin_menu()

def display_movies():
    for movie in movies:
        print(movie)
    admin_menu()
    

def remove_movie():
    while True:
        movie_name = input("Enter the name of the movie to remove: ").upper()

        if movie_name in movies:
            movies.remove(movie_name)

            while True:
                found = False

                for show in shows:
                    if show["movie"] == movie_name:
                        shows.remove(show)
                        found = True
                        break

                if found == False:
                    break

            print(f"{movie_name} and all its shows removed successfully.")

        else:
            print(f"{movie_name} is not in the movie list.")

        choice = input("Do you want to remove another movie? (y/n): ")

        if choice.lower() == 'y':
            continue
        else:
            admin_menu()
            break

def display_shows():
    print("================================")
    print("             ALL SHOWS          ")
    print("================================")
    for show in range(len(shows)):
        print(f"Movie: {shows[show]['movie']}\n Date: {shows[show]['date']}\n Time: {shows[show]['time']}\n Screen: {shows[show]['screen']}\n Price: {shows[show]['price']}")
        print('-----------------------------')
    admin_menu()


def add_show():
    d = {}

    show_add_list = []
    show_details = ['movie', 'date', 'time', 'screen', 'price', 'seats']

    show_movie = input("Enter the movie name: ").upper()

    if show_movie not in movies:
        add_movie_choice = input("Do you want to add the movie? ").upper()

        if add_movie_choice != 'Y':
            admin_menu()
            return

    show_date = input("Enter the date in the format of dd-mm-yyyy: ")

    show_time = input("Add show time: ")

    show_screen = input("Add Screen No: ")



    if show_screen not in ["Screen 1", "Screen 2"]:
        print("Only Screen 1 and Screen 2 are available.")
        admin_menu()
        return

    for show in shows:
        if show["screen"] == show_screen and show["date"] == show_date and show["time"] == show_time:
            print("This screen is already occupied at this date and time.")
            admin_menu()
            return

    show_price = int(input("Enter the ticket price: "))

    if show_screen == "Screen 1":
        show_seats = []
        for seat in screen1_seats:
            show_seats.append(seat)
    else:
        show_seats = []
        for seat in screen2_seats:
            show_seats.append(seat)

    if show_movie not in movies:
        movies.append(show_movie)
    show_add_list.append(show_movie)
    show_add_list.append(show_date)
    show_add_list.append(show_time)
    show_add_list.append(show_screen)
    show_add_list.append(show_price)
    show_add_list.append(show_seats)

    for i in range(len(show_details)):
        if show_details[i] not in d:
            d[show_details[i]] = show_add_list[i]

    shows.append(d)

    print("Show added successfully.")

    if input("Do you want to add another show? ").upper() == 'Y':
        add_show()
    else:
        admin_menu()

def remove_show():
    movie_name = input("Enter movie name: ").upper()
    date = input("Enter date (dd-mm-yyyy): ")
    time = input("Enter show time (hh:mm AM/PM): ")
    screen = input("Enter screen (Screen 1 / Screen 2): ")

    for show in shows:
        if show["movie"] == movie_name and show["date"] == date and show["time"] == time and show["screen"] == screen:
            shows.remove(show)
            print("Show removed successfully.")
            admin_menu()
            return
    else:
        print("Show not found.")
        admin_menu()

def manage_seats(): 
    movie_name = input("Enter movie name: ").upper() 
    date = input("Enter date (dd-mm-yyyy): ") 
    time = input("Enter show time (hh:mm AM/PM): ")
    screen = input("Enter screen (Screen 1 / Screen 2): ")

    for show in shows: 
        if (
            show["movie"] == movie_name
            and show["date"] == date
            and show["time"] == time
            and show["screen"] == screen
        ):

            print("Available Seats:") 
 
            for seat in show["seats"]: 
                if seat != "Bk":
                    print(seat, end=" ") 
 
            print() 
            admin_menu() 
            return 
 
    print("Show not found.") 
    admin_menu()

def view_bookings():
    if len(bookings) ==0:
        print("No bookings found.")
    else:
        for booking in bookings:
            print("Movie:",booking["movie"])
            print("Date:",booking["date"])
            print("Time:",booking["time"])
            print("Screen:",booking["screen"])
            print("Seats:", booking["seats"])
            print("Amount:",booking["amount"])
            print("-----------------------------")
    admin_menu()

def user_display_movies():
    for movie in movies:
        print(movie)
    if input("Do you want to see the menu (Y/N): ").upper()=='Y':
        user_login()
    else:
        return "Exiting admin menu..."


def user_display_shows():
    print("================================")
    print("             ALL SHOWS          ")
    print("================================")

    for show in range(len(shows)):
        print(f"Movie: {shows[show]['movie']}")
        print(f"Date: {shows[show]['date']}")
        print(f"Time: {shows[show]['time']}")
        print(f"Screen: {shows[show]['screen']}")
        print(f"Price: {shows[show]['price']}")
        print("-----------------------------")

    user_login()

def user_login():
    print("================================")
    print("USER MENU")
    print("================================")
    print()
    print("1. View Movies")
    print("2. View Showtimes")
    print("3. Book Tickets")
    print("4. View Booking")
    print("5. Exit")

    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        user_display_movies()
    elif user_choice == 2:
        user_display_shows()
    elif user_choice == 3:
        user_book_tickets()
    elif user_choice == 4:
        user_view_booking()
    elif user_choice == 5:
        movie_booking()
    else:
        print("Invalid choice")
        user_login()


def user_view_booking():
    if len(bookings) == 0:
        print("No bookings found.")
    else:
        for booking in bookings:
            print("Movie:", booking["movie"])
            print("Date:", booking["date"])
            print("Time:", booking["time"])
            print("Screen:", booking["screen"])
            print("Seats:", booking["seats"])
            print("Amount:", booking["amount"])
            print("-----------------------------")

    user_login()

def user_shows(show):
    return show["seats"]

def user_screen(show):
    if show["screen"] =="Screen 1":
        return "Screen 1"
    else:
        return "Screen 2"


def user_seat(show):
    seats = user_shows(show)
    selected_seats = []

    price = show["price"]

    print("Available Seats:")

    for seat in seats:
        if seat!='Bk':
            print(seat, end=" ")
    
    print()

    available_seats = 0

    for seat in seats:
        if seat != "Bk":
            available_seats += 1
    
    seat_no = int(input("How many seats do you want to book: "))

    if seat_no <= 0:
        print("Please enter at least 1 seat.")
        user_login()
        return

    if seat_no > available_seats:
        print(f"Only {available_seats} seats are available.")
        user_login()
        return

    count = seat_no

    while count>0:
        seat = input("Enter seat: ").upper()

        if seat in seats and seat!='Bk':
            idx = seats.index(seat)
            selected_seats.append(seat)
            seats[idx] = 'Bk'
            count-=1
        else:
            print("Seat is not available. Please enter another seat.")

            
    print("Selected Seats:", selected_seats)

    amount = len(selected_seats) * price

    print(f"The Amount you need to pay {amount} for {len(selected_seats)} seats")


    booking = {
    "movie": show["movie"],
    "date": show["date"],
    "time": show["time"],
    "screen": show["screen"],
    "seats": selected_seats,
    "amount": len(selected_seats) * price
    }

    bookings.append(booking)
    user_login()

def user_book_tickets():
    print("Available Movies:")
    user_display_movies()

    user_movie = input("Enter movie name: ").upper()

    if user_movie in movies:

        for show in shows:
            if show["movie"] == user_movie:
                print(
                    "Date:", show["date"],
                    "| Time:", show["time"],
                    "| Screen:", show["screen"]
                )
                

        user_date = input("Enter date: ")
        user_time = input("Enter time: ")

        for show in shows:
            if (
                show["movie"] == user_movie
                and show["date"] == user_date
                and show["time"] == user_time
            ):
                print("Selected Show:", show)
                user_seat(show)
                return

        print("Show not found.")

    else:
        print("Movie not found.")

        if input("Do you want to rebook tickets? ").upper() == 'Y':
            user_book_tickets()
        else:
            return


movie_booking() 