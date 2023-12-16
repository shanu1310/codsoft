class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

def add_contact(contact_list):
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    new_contact = Contact(name, phone_number, email, address)
    contact_list.append(new_contact)
    print("Contact added successfully!")

def view_contact_list(contact_list):
    print("Contact List:")
    for index, contact in enumerate(contact_list, start=1):
        print(f"{index}. {contact.name} - {contact.phone_number}")

def search_contact(contact_list, keyword):
    results = []
    for contact in contact_list:
        if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
            results.append(contact)
    return results

def update_contact(contact):
    contact.name = input("Enter new name: ")
    contact.phone_number = input("Enter new phone number: ")
    contact.email = input("Enter new email: ")
    contact.address = input("Enter new address: ")
    print("Contact updated successfully!")

def delete_contact(contact_list, contact):
    contact_list.remove(contact)
    print("Contact deleted successfully!")

def main():
    contact_list = []

    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact(contact_list)
        elif choice == '2':
            view_contact_list(contact_list)
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            results = search_contact(contact_list, keyword)
            if results:
                print("Search Results:")
                for index, result in enumerate(results, start=1):
                    print(f"{index}. {result.name} - {result.phone_number}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            view_contact_list(contact_list)
            index = int(input("Enter the index of the contact to update: ")) - 1
            if 0 <= index < len(contact_list):
                update_contact(contact_list[index])
            else:
                print("Invalid index.")
        elif choice == '5':
            view_contact_list(contact_list)
            index = int(input("Enter the index of the contact to delete: ")) - 1
            if 0 <= index < len(contact_list):
                delete_contact(contact_list, contact_list[index])
            else:
                print("Invalid index.")
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
