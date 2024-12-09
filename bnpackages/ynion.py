def display_menu():
    while True:
        print("\nGreetings! My names is Ma. Bea Mae Ynion")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comment from Delima")
        print("4. Comment from Relente")
        print("5. Comment from Quiambao")
        print("6. Comment from Citron")
        print("7. Exit")
        
        choice = int(input("Enter your choice:"))

        match choice:
            case 1:
                print("\nBasic Info: I am a web developer with a passion for web development.")
            case 2:
                print("\nGoals: To learn more about programming languages and improve my problem-solving skills.")
            case 3:
                print("\nHarry Potter, Lighter and Princess, Stranger Things")
            case 4:
                print("\n2NE1, BLACKPINK, BABYMONSTER, IZNA, BIGBANG, NEWJEANS")
            case 5:
                print("\nSky Blue, Blue, Red, Green")
            case 6:
                print("\nExiting the menu.")
                return