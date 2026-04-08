from auth import login
from backup import backup_data

def main():
    print("=== USB Backup Tool ===")

    if not login():
        return

    print("1. Backup Documents")
    print("2. Backup Desktop")

    choice = input("Choose option: ")

    # Change paths depending on your PC
    if choice == "1":
        source = "C:/Users/YourName/Documents"
    elif choice == "2":
        source = "C:/Users/YourName/Desktop"
    else:
        print("Invalid choice!")
        return

    destination = "./backup_data"

    backup_data(source, destination)

if __name__ == "__main__":
    main()