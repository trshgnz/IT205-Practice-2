def add_contact(phone_book):
    name = input("Enter contact name: ")
    number = input("Enter phone number: ")
    phone_book[name] = number
    print("Contact added successfully.")

def look_up_contact(phone_book):
    name = input("Enter contact name: ")
    if name in phone_book:
        print(f"{name}'s phone number is {phone_book[name]}.")
    else:
        print("Contact not found.")

def delete_contact(phone_book):
    name = input("Enter contact name: ")
    if name in phone_book:
        del phone_book[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    phone_book = {}
    while True:
        print("\nPhone Book:")
        print("1. Add contact")
        print("2. Look up contact")
        print("3. Delete contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(phone_book)
        elif choice == '2':
            look_up_contact(phone_book)
        elif choice == '3':
            delete_contact(phone_book)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()