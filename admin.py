movies = ['PARADISE', 'BAHUBALI', 'RRR', 'KGF']


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
    movie_name = input("Enter the name of the movie to add: ")
    print(f"Movie '{movie_name}' added successfully!")
    admin_menu()

def display_movies():
    print("Displaying all movies:")
    for movie in movies:
        print(movie)
    admin_menu()





movie_booking()
