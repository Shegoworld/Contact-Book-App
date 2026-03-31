
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


# The dictionary to store Name-Number pair is initialized
store = {}


# To view the contacts in the contact book
def viewlist():
    i = 1
    for el in sorted(store):
        print(f"{i}. {el} - {store[el]}")
        i += 1
    '''
    for i, (name, number) in enumerate(store.items(), start=1):
    print(f"{i}. {name} - {number}")
    '''


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


# The Code block to loop the menu
while True:
    choice = accept()

    # The logic for Adding Contact
    if choice == 1:
        print("You have selected Add Contact")
        while True:
            name = input("Enter the name: ")
            name_exist = False
            for x in store:
                if name.lower() == x.lower():
                    name_exist = True
                    print("Name already exist \n ")
                    break
            # Cleaner for checking if name exists
            '''
            if name.lower() in [x.lower() for x in store]:
                print("Name already exists\n")
                continue
            '''
            if not name_exist:
                print(f"{name} added successfully")
                break

        while True:
            mobile = num_check()
            for name, number in store.items():
                if mobile == number:
                    print(f"Number already exists under {name}")
                print()
                continue
            else:
                store[name] = mobile
                print()
                break



    # The logic for viewing contacts
    elif choice == 2:
        print("You have selected View Contacts")
        print("Your contacts are: ")
        if not store:
            print("There is no contact in Contact Book")
        else:
            viewlist()
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
            print("There is no contact to delete")
        else:
            print("Select a number to delete contact")
            viewlist()
            while True:
                delete = input("Enter number to delete contact: ")
                try:
                    is_valid = int(delete)
                    if is_valid in range(1, len(store)+1):
                        del_key = list(sorted(store.keys()))[is_valid - 1]
                        print(f"{del_key} deleted successfully")
                        store.pop(del_key)
                        break
                    else:
                        print("Enter a valid number")

                except ValueError:
                    print("You didn't pick a number")
        print()

    #When the user picks Exit, the loop breaks
    else:
        break


print("Exit Successfully")


