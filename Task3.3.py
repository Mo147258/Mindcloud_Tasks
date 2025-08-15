class Phone:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        if name not in self.contacts:
            self.contacts[name] = number
            print(f"Contact '{name}' added successfully.")
        else:
            print(f"Contact '{name}' already exists.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' removed successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def make_call(self, name):
        if name in self.contacts:
            print(f"Calling {name} at {self.contacts[name]}...")
        else:
            print(f"{name} is not in your contacts.")

    def show_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\nContacts List:")
            for name, number in self.contacts.items():
                print(f" - {name}: {number}")
            print()


class Camera:
    def take_pic(self):
        print("The picture was taken successfully.")


class Smartphone(Phone, Camera):
    def __init__(self):
        Phone.__init__(self) 



if __name__ == "__main__":
    phone = Smartphone()

    while True:
        print("\n===== Smartphone Menu =====")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Make Call")
        print("4. Show Contacts")
        print("5. Take Picture")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            name = input("Enter contact name: ").strip()
            number = input("Enter phone number: ").strip()
            phone.add_contact(name, number)
        elif choice == "2":
            name = input("Enter contact name to remove: ").strip()
            phone.remove_contact(name)
        elif choice == "3":
            name = input("Enter contact name to call: ").strip()
            phone.make_call(name)
        elif choice == "4":
            phone.show_contacts()
        elif choice == "5":
            phone.take_pic()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
