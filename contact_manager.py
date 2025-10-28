import csv

my_contacts = "contacts.csv"
columns = ["Name", "Phone number", "Email"]

print("Contact Manager")
print("1. Add new contact")
print("2. View all contacts")
print("3. Exit")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    print("--- Add New Contact ---")
    name = input("Enter name: ")
    while name.strip() == "":
        print("✗ Error: Name cannot be empty")
        name = input("Enter name: ")

    phone = input("Enter phone number: ")
    while phone == "":
        print("✗ Error: Phone number cannot be empty")
        phone = input("Enter phone number: ")

    email = input("Enter email: ")
    while email == "":
        print("✗ Error: Email cannot be empty")
        email = input("Enter email: ")

    with open(my_contacts, "a", newline="") as file:
        content = csv.DictWriter(file, fieldnames=columns)
        # content.writeheader() - ამას როცა ვამატებ, ყოველ ჯერზე თავიდან ამატებს header-s (Name, Phone Number, Email)
        # გარეთ გატანა და "w" mode-ით ფაილის გახსნა რომ ვცადე, აღარ იმახსოვრებდა ინფუთს და ყოველჯერზე ახალ ფაილს ხსნიდა.
        content.writerow({"Name": name, "Phone number": phone, "Email": email})
    print("✓ Contact added successfully!")

elif choice == 2:
    with open(my_contacts, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row["Name"]}, {row["Phone number"]}, {row["Email"]}")

elif choice == 3:
    print("Thank you for using Contact Manager. Goodbye!")

else:
    print("Invalid choice. Please enter 1, 2, or 3.")
