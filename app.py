import re
from datetime import datetime

# ==================================================
# DATA REDUNDANCY REMOVAL SYSTEM
# CodeAlpha Cloud Computing Internship Project
# ==================================================

duplicate_count = 0

# Create database file if not exists
try:
    open("database.txt", "x")
except FileExistsError:
    pass

# ==================================================
# MAIN LOOP
# ==================================================

while True:

    print("\n================================================")
    print("      DATA REDUNDANCY REMOVAL SYSTEM")
    print("================================================")

    print("\n1. Add Email")
    print("2. View Database")
    print("3. View Statistics")
    print("4. Search Email")
    print("5. Delete Email")
    print("6. Exit")

    choice = input("\nEnter Your Choice: ").strip()

    # ==================================================
    # ADD EMAIL
    # ==================================================

    if choice == "1":

        # Read database
        with open("database.txt", "r") as file:
            database = file.read().splitlines()

        # User input
        new_email = input("\nEnter Email: ")

        # Clean email
        new_email = new_email.strip().lower().replace(" ", "")

        # ==================================================
        # UNIVERSAL EMAIL VALIDATION
        # ==================================================

        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(email_pattern, new_email):

            print("\n❌ Invalid Email Format")
            continue

        # ==================================================
        # DUPLICATE CHECK
        # ==================================================

        existing_emails = []

        for line in database:

            if " - " in line:

                stored_email = line.split(" - ")[0].lower()
                existing_emails.append(stored_email)

        # Check duplicate
        if new_email in existing_emails:

            print("\n⚠ Duplicate Data Found")
            duplicate_count += 1

        else:

            # Current date and time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Store unique email
            with open("database.txt", "a") as file:
                file.write(f"{new_email} - {current_time}\n")

            print("\n✅ Unique Data Added Successfully")

    # ==================================================
    # VIEW DATABASE
    # ==================================================

    elif choice == "2":

        print("\n================================================")
        print("                STORED DATABASE")
        print("================================================")

        with open("database.txt", "r") as file:
            data = file.readlines()

        if not data:

            print("\nDatabase Empty")

        else:

            for line in data:
                print(line.strip())

    # ==================================================
    # VIEW STATISTICS
    # ==================================================

    elif choice == "3":

        with open("database.txt", "r") as file:
            total_data = len(file.readlines())

        print("\n================================================")
        print("                   STATISTICS")
        print("================================================")

        print(f"\n📧 Total Unique Emails Stored : {total_data}")
        print(f"🚫 Duplicate Entries Prevented : {duplicate_count}")

    # ==================================================
    # SEARCH EMAIL
    # ==================================================

    elif choice == "4":

        search_email = input("\nEnter Email To Search: ")

        search_email = search_email.strip().lower().replace(" ", "")

        found = False

        with open("database.txt", "r") as file:
            data = file.readlines()

        for line in data:

            stored_email = line.split(" - ")[0].lower()

            if search_email == stored_email:

                print("\n✅ Email Found")
                print(line.strip())

                found = True
                break

        if not found:

            print("\n❌ Email Not Found")

    # ==================================================
    # DELETE EMAIL
    # ==================================================

    elif choice == "5":

        delete_email = input("\nEnter Email To Delete: ")

        delete_email = delete_email.strip().lower().replace(" ", "")

        with open("database.txt", "r") as file:
            data = file.readlines()

        updated_data = []
        deleted = False

        for line in data:

            stored_email = line.split(" - ")[0].lower()

            if stored_email != delete_email:

                updated_data.append(line)

            else:

                deleted = True

        with open("database.txt", "w") as file:
            file.writelines(updated_data)

        if deleted:

            print("\n✅ Email Deleted Successfully")

        else:

            print("\n❌ Email Not Found")

    # ==================================================
    # EXIT
    # ==================================================

    elif choice == "6":

        print("\n🚪 Program Stopped")
        break

    # ==================================================
    # INVALID CHOICE
    # ==================================================

    else:

        print("\n❌ Invalid Choice")