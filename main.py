
print("Welcome to your Contact Book, what would you like to do today?")

# Menu List
y = ("Select '1' to Add Contact \nSelect '2' to View Contacts \nSelect '3' to Search Contact "
     "\nSelect '4' to Delete contact \nSelect '5' to Exit")

# To check the selection from Menu is valid
def accept():
    print(y)
    while True:
        request = input("Enter a number: ")
        try:
            valid = int(request)
            if valid in range(1, 6):
                break
            else:
                print("Enter a valid number")
        except ValueError:
            print()
            print("Enter a valid input")
    return valid


# The dictionary to store Name-Number pair is initialized and loaded with the saved contacts
import json

def load_contacts():
    global store
    try:
        with open("contacts.json", "r") as contacts:
            store = json.load(contacts)
    except FileNotFoundError:
        store = {}

 # The logic to save contacts as file
#import json
def save_contacts():
    with open("contacts.json", "w") as contacts:
        json.dump(store, contacts, indent = 4)


# To view the contacts in the contact book
def view_list():
    for i, (list_name, list_number) in enumerate(sorted(store.items()), start=1):
        print(f"{i}. {list_name} - {list_number}")



# To check if a mobile number is valid
def num_check():
    while True:
        phone = input("Enter the mobile number: ")
        if not phone.isdigit():
            print("Mobile can only accept 11 digits number")
        elif phone[0] != "0":
            print("Number must start with 0")
        elif len(phone) != 11:
            print("Number must be exactly 11 digits")
        else:
            return phone

load_contacts()
# The Code block to loop the menu
while True:
    choice = accept()

    # The logic for Adding Contact
    if choice == 1:
        print("You have selected Add Contact")
        while True:
            name = input("Enter the name: ")
           # name_exist = False
            if name.lower() in [x.lower() for x in store]:
                print("Name already exists\n")
                continue

            else:
                break

        while True:
            mobile = num_check()
            if mobile in store.values():
                for existing_name, number in store.items():
                    if number == mobile:
                        print(f"Number already exists under {existing_name} \n")
                        break

            else:
                store[name] = mobile
                print(f"{mobile} stored as {name} \n")
                save_contacts()
                break



    # The logic for viewing contacts
    elif choice == 2:
        print("You have selected View Contacts")
        if not store:
            print("There is no contact in Contact Book")
        else:
            print("Your contacts are: ")
            view_list()
        print()

    # The logic for Searching contact
    elif choice == 3:
        print("You have selected Search Contact")
        if not store:
            print("The Contact Book is empty")
        else:
            search = input("Enter a name to search contact: ")
            found = False
            for x in store:
                if search.lower() in x.lower():
                    found = True
                    print(f"{x} found, the number is {store[x]}")
            if not found:
                print(f"{search} not found in contact book")
        print()

    #The logic to delete contact
    elif choice == 4:
        print("You have selected Delete Contact")
        if not store:
            print("There is no contact to delete \n")
        else:
            print("Select a number to delete contact")
            view_list()
            while True:
                delete = input("\nEnter number to delete contact: ")
                try:
                    is_valid = int(delete)
                    if is_valid in range(1, len(store)+1):
                        while True:
                            sure = input("Are you sure? (y/n): ")
                            if sure.lower() == "y":
                                del_key = list(sorted(store.keys()))[is_valid - 1]
                                print(f"{del_key} deleted successfully \n")
                                store.pop(del_key)
                                save_contacts()
                                break
                            elif sure.lower() == "n":
                                print("Delete operation cancelled successfully \n")
                                break
                            else:
                                print("Enter 'y' or 'n'")
                        break
                    else:
                        print("Enter a valid number")

                except ValueError:
                    print("You didn't pick a number")

    #When the user picks Exit, the loop breaks
    else:
        break


print("Exit Successfully")


