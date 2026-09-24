movies = ['BAHUBALI', 'RRR']
shows = [
    {
        "movie": "RRR",
        "date": "25-09-2026",
        "time": "06:00 PM",
        "screen": "Screen 1",
        "price": 200
    },

    {
        'movie': "RRR",
        'date': "25-09-2026",
        'time': "09:00 PM",
        'screen': "Screen 2",
        'price': 250
    },

    {
        "movie": "RRR",
        "date": "26-09-2026",
        "time": "08:00 PM",
        "screen": "Screen 1",
        "price": 200
    },

    
    {
        "movie": "BAHUBALI",
        "date": "30-09-2026",
        "time": "07:00 PM",
        "screen": "Screen 2",
        "price": 250
    }
]

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
    print("4. Exit")
    print()

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_movie()
    elif choice == 2:
        remove_movie()
    elif choice == 3:
        display_movies()
    elif choice == 4:
        print("Exiting admin menu...")
        movie_booking()
    else:
        print("Invalid choice")

def add_movie():
    while True:
        movie_name = input("Enter the name of the movie to add: ")
        if movie_name in movies:
            print(f"{movie_name} is already in the list.")
        else:
            movies.append(movie_name)
            print(f"{movie_name} has been added to the list.")
        admin_choice = input("Do you want to add another movie? (y/n): ")
        if admin_choice.lower() != 'y':
            break

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


movie_booking()







def remove_movie():
    while True:
        movie_name = input("Enter the name of the movie to remove: ").upper()
        time = input("Enter show time: ")
        for show in shows:
            if show['movie']==movie_name and show['time']==time:
                shows.remove(show)
                print("Show removed successfully.")
            else:
                print("Invalid")
        admin_menu()

        admin_choice = input("Do you want to remove another movie? (y/n): ")
        if admin_choice.lower() != 'n':
            admin_menu()
            break
        else:
            remove_movie()