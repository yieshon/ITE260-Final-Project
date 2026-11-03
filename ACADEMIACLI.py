from datetime import datetime

student_accounts = []

teachers = {
    "1": {"name": "Alein Dhave Villadores"},
    "2": {"name": "Gwayne Rithzel Colaste"}
}

students = {"BSIT":[]}

sections = [
    "COC-FC1-BSIT1-01",
    "COC-FC1-BSIT1-02",
    "COC-FC1-BSIT1-03",
    "COC-FC1-BSIT1-04"
]

def valid_student_id(student_id):
    if len(student_id) !=14:
        return False
    if student_id[2] != "-" or student_id[7] != "-":
        return False
    
    numbers = student_id[:2] +  student_id[3:7] + student_id[8:]
    return numbers.isdigit()

def exit_option(prompt):
    value = input(prompt).strip()
    if value == "0":
        return None
    return value

def student_submenu():
    while True:
        print("\n====== STUDENT ======")
        print("\n[1] Create account")
        print("[2] Login")
        print("[0] Exit")
        print("\n=====================")

        choice = input("Choice: ").strip()

        if choice == "1":
            create_student_account()
        elif choice == "2":
            student_login()
        elif choice == "0":
            print("\nReturning to the main menu...")
            return
        else:
            print("Invalid choice. 1, 2, and 0 only.")

def add_student_id(prompt="\nEnter Student ID (ex. 02-2425-006647): "):
    while True:
        student_id = exit_option(prompt)

        if student_id is None:
            return None
        
        if valid_student_id(student_id):
            return student_id
        
        print("Invalid Student ID!")
        print("Required format: 02-2425-123456")

def create_student_account():
    print("====== CREATE STUDENT ACCOUNT ======")

    student_id = add_student_id()

    if student_id is None:
        print("Account creation cancelled.")
        return

    for account in student_accounts:
        if account["id"] == student_id:
            print("Student already exists.")
            return

    while True:
        username = exit_option("Create Username: ")
        
        if username is None:
            print("Account creation cancelled.")
            return
        
        if not username or not username.isalnum():
            print("Username must only contain letters or numbers only.")
            continue

        username_exists = False

        for account in student_accounts:
            if account["username"] == username:
                username_exists = True
                break

        if username_exists:
            print("Username already exists.")
        else: 
            break

    while True:
        password = exit_option("Create password: ")

        if password is None:
            print("Account creation was cancelled.")
            return

        if password:
            break

        print("Password cannot be empty.")

    student_accounts.append({
        "id": student_id,
        "username": username,
        "password": password
    })

    print("\nAccount created successfully.")

def student_login():
    if not student_accounts:
        print("No student account exists. Please create an account first.")
        return

    while True:
        print("\n ====== STUDENT LOGIN ======")
        
        student_id = add_student_id()

        if student_id is None:
            print("Login cancelled.")
            return
        
        username = exit_option("Username: ")

        if username is None:
            print("Login cancelled.")
            return

        password = exit_option("Password: ")

        if password is None:
            print("Login cancelled.")
            return

        for account in student_accounts:
            if (account["id"] == student_id
                and account["username"] == username
                and account["password"] == password):
                print("\nLogin successful!")
                student_menu(student_id)
                return

        print("Incorrect Student ID, username, or password. Try again.")        

def student_menu(student_id):
    while True:
        print("\n====== STUDENT MENU ======")
        print("\n[1] Add Information")
        print("[2] View Information")
        print("[3] Update Information") 
        print("[0] Log out")
        print("\n==========================")

        choice = input("Choice: ").strip()

        if choice == "1":
            add_student_information(student_id)
        elif choice == "2":
            view_student_information(student_id)
        elif choice == "3":
            update_student_information(student_id)
        elif choice == "0":
            print("\nReturning to the submenu...")
            return
        else:
            print("Invalid choice. 1, 2, 3, and 0 only.")

def find_student_information(student_id):
    for student in students["BSIT"]:
        if student["id"] == student_id:
            return student

    return None
            
def add_student_information(student_id):
    print("\n====== ADD STUDENT INFORMATION ======")

    if find_student_information(student_id) is not None:
        print("You have already added your information.")
        return

    while True:
        last_name = exit_option("Enter Last Name: ")

        if last_name is None:
            print("Adding information cancelled. No changes were saved.")
            return

        if last_name and last_name.replace(" ", "").isalpha():
            last_name = last_name.upper()
            break

        print("Last name must only contain letters only.")

    while True:
        first_name = exit_option("Enter First Name: ")

        if first_name is None:
            print("Adding information cancelled. No changes were saved.")
            return

        if first_name and first_name.replace(" ", "").isalpha():
            first_name = first_name.upper()
            break

        print("First name must only contain letters only.")

    while True:
        middle_name = exit_option("Enter Middle Name: ")

        if middle_name is None:
            print("Adding information cancelled. No changes were saved.")
            return

        if middle_name and middle_name.replace(" ", "").isalpha():
            middle_name = middle_name.upper()
            break

        print("Middle name must only contain letters only.")

    if middle_name:
        name = f"{last_name}, {first_name}, {middle_name}"
    else:
        name = f"{last_name}, {first_name}"

    while True:
        birthdate = exit_option("Enter Birthdate(MM/DD/YYYY): ")
        
        if birthdate is None:
            print("Adding information cancelled. No changes were saved.")
            return
        
        try:
            datetime.strptime(birthdate, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid birthdate. Use MM/DD/YYYY (example: 09/15/2007).")

    while True:
        print("\n====== COURSE ======")
        print("\n[1] BSIT")

        choice = exit_option("Choice: ")

        if choice is None:
            print("Adding information was cancelled. No changes were saved.")
            return

        if choice == "1":
            course = "BSIT"
            break

        print("Invalid choice. 1 only.")

    while True:
        print("\n====== YEAR LEVEL ======")
        print("\n[1] 1st Year")

        choice = exit_option("Choice: ")

        if choice is None:
            print("Adding information cancelled. No changes were saved.")
            return

        if choice == "1":
            year = "1st Year"
            break

        print("Invalid choice. 1 only.")

    while True:
        print("====== SECTION ======")

        for number, section_name in enumerate(sections, start=1):
            print("[" + str(number) + "] " + section_name)
        
        choice = exit_option("Choice: ")

        if choice is None:
            print("Adding information cancelled. No changes were saved.")
            return

        if choice.isdigit() and 1 <= int(choice) <= len(sections):
            section = sections[int(choice) - 1]
            break

        print("Invalid choice. Enter a number.")

    students[course].append({
        "id": student_id,
        "name": name,
        "birthdate": birthdate,
        "course": course,
        "year": year,
        "section": section,
    })

    print("\nInformation added successfully!")


def view_student_information(student_or_id):
    if isinstance(student_or_id, dict):
        student = student_or_id
    else:
        student = find_student_information(student_or_id)

    if student is None:
        print("\nNo added information yet.")
        return

    print("====== STUDENT INFORMATION ======")
    print("-----------------------------")
    print("Student ID :", student["id"])
    print("Name       :", student["name"])
    print("Birthdate  :", student["birthdate"])
    print("Course     :", student["course"])
    print("Year Level :", student["year"])
    print("Section    :", student["section"])
    print("-----------------------------")

def update_student_information(student_id):
    print("\n====== UPDATE INFORMATION ======")

    student = find_student_information(student_id)

    if student is None:
        print("No information added yet.")
        return

        print("\nCurrent Name:", student["name"])
    
    while True:
        last_name = exit_option("Enter New Last Name: ")

        if last_name is None:
            print("Update cancelled. No changes were saved.")
            return
        
        if last_name and last_name.replace (" ", "").isalpha():
            last_name = last_name.upper()
            break
    
        print("Last name must contain letters only.")

    while True:
        first_name = exit_option("Enter New First Name: ")

        if first_name is None:
            print("Update cancelled. No changes were saved.")
            return
        
        if first_name and first_name.replace (" ", "").isalpha():
            first_name = first_name.upper()
            break
    
        print("First name must contain letters only.")

    while True:
        middle_name = exit_option("Enter New Middle Name: ")

        if middle_name is None:
            print("Update cancelled. No changes were saved.")
            return
        
        if middle_name and middle_name.replace (" ", "").isalpha():
            middle_name = middle_name.upper()
            break
    
        print("Middle name must contain letters only.")

    student["name"] = f"{last_name}, {first_name}, {middle_name}"
    print("\nInformation updated successfully!")    

def teacher_submenu():
    while True:
        print("\n====== SELECT TEACHER ======")
        print("\n[1] Alein Dhave Villadores")
        print("[2] Gwayne Rithzel Colaste")
        print("[0] Exit")
        print("\n============================")

        choice = input("Choice: ").strip()
        if choice in teachers:
            teacher = teachers[choice]
            print("\n====== WELCOME " + teacher["name"].upper() + "! ======")
            teacher_menu()

        elif choice == "0":
            print("\nReturning to the main menu...")
            return

        else:
            print("Invalid choice. 1, 2, and 0 only.")

def teacher_menu():
    while True:
        print("\n====== TEACHER MENU ======")
        print("\n[1] View all Student")
        print("[2] Search Student")
        print("[3] Delete student")
        print("[0] Exit")
        print("\n==========================")

        choice = input("Choice: ").strip()

        if choice == "1":
            view_all_student_information()
        elif choice == "2":
            search_student_information()
        elif choice == "3":
            delete_student_information()
        elif choice == "0":
            print("\nReturning to the submenu...")
            return
        else:
            print("Invalid choice. 1, 2, 3, and 0 only.")

def view_all_student_information():
    print("\n====== VIEW ALL STUDENT INFORMATION ======")
    print("\n====== SELECT SECTION ======")

    for number, section_name in enumerate(sections, start=1):
        print("[" + str(number) + "]" + section_name)

    print("[0] Exit")

    while True:
        choice = input("Choice: ").strip()

        if choice == "0":
            print("\nReturning to teacher menu...")
            return

        if choice.isdigit() and 1<= int(choice) <= len(sections):
            selected_section = sections[int(choice) - 1]
            break

        print("Invalid choice. Enter a valid number.")

    section_students = [
        student for student in students["BSIT"]
        if student["section"] == selected_section
    ]

    print("\n" + "=" * 80)
    print("SECTION:", selected_section)
    print("\n" + "=" *80)

    if not section_students:
        print("\nNo student records found in this section.")
        return

    print(
        "STUDENT ID".ljust(17),
        "NAME".ljust(25),
        "BIRTHDATE".ljust(14),
        "COURSE".ljust(8),
        "YEAR LEVEL"
    )

    print("-" * 80)

    for student in section_students:
        print(
            student["id"].ljust(17),
            student["name"][:24].ljust(25),
            student["birthdate"].ljust(14),
            student["course"].ljust(8),
            student["year"]
        )

    print("-" * 80)

def search_student_information():
    print("\n====== SEARCH STUDENT ======")

    student_id = add_student_id("Enter Student ID: ")
    if student_id is None:
        print("Search cancelled.")
        return

    student = find_student_information(student_id)

    if student is None:
        print("\nStudent not found.")
        return

    print("\n====== STUDENT FOUND ======")
    view_student_information(student)

def delete_student_information():
    print("\n====== DELETE STUDENT INFORMATION ======")

    student_id = add_student_id("Enter Student ID: ")
    if student_id is None:
        print("Delete operation cancelled.")
        return

    student = find_student_information(student_id)

    if student is None:
        print("\nStudent not found.")
        return

    view_student_information(student)

    confirm = input("Are you sure you want to delete this student's information? (Y/N): ").strip().upper()

    if confirm == "Y":
        students[student["course"]].remove(student)
        print("\nStudent deleted successfully!")
    else:
        print("\nDeletion cancelled.")

while True:
        print("\n========================================")
        print("ACADEMIACLI - STUDENT INFORMATION SYSTEM")
        print("========================================")
        print("Are you a student or a teacher?")
        print("[1] Student")
        print("[2] Teacher")
        print("[0] Exit")
        print("\n======================================")
        
        choice = input("Choice: ").strip()
        if choice == "1":
            student_submenu()
        elif choice == "2":
            teacher_submenu()
        elif choice == "0":
            print("\nThank you for using the system!")
            break

        else:
            print("Invalid choice. Enter 1, 2, and 0 only.")