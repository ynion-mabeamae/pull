from bnpackages import ynion

def display_main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Ynion")
        print("2. Delima")
        print("3. Relente")
        print("4. Quiambao")
        print("5. Citron")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                ynion.display_menu()
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                print("\nExiting the main menu.")
                break

display_main_menu()