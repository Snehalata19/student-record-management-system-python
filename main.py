import csv
def show_menu():
    print("\n--- Student Record Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
while True:
    show_menu()
    def add_student():
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")

        with open("students.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([roll, name, marks])

        print("Student added successfully!")

    choice = input("Enter your choice (1-5): ")
    def view_student():
        try:
            with open("students.csv","r") as file:
                reader=csv.reader(file)
                print("\n Students record")
                for row in reader:
                    print(f"Roll:{row[0]},Name:{row[1]},Marks:{row[2]}")
        except FileNotFoundError:
            print("Records not found")
    def search_student():
        roll_no =input("Enter the roll no:")
        found=False
        try:
            with open("students.csv","r")as file:
                reader=csv.reader(file)
                for row in reader:
                    if row and row[0]==roll_no:
                        print("\n Student Found!!")
                        print(f"Roll:{row[0]},Name:{row[1]},Marks:{row[2]}")
                        found=True
                        break
            if not found:
                        print("Student not found")
        except FileNotFoundError:
            print("No file exists")
    def delete_student():
        roll_delete=input("Enter the roll no to be deleted:")
        rows=[]
        deleted=False
        try:
            with open("students.csv","r")as file:
                reader=csv.reader(file)
                for row in reader:
                    if row and row[0]!=roll_delete:
                        rows.append(row)
                    else:
                        deleted=True
            if deleted:
                with open("students.csv","w",newline="")as file:
                    writer=csv.writer(file)
                    writer.writerows(rows)
                print("Student deleted successfully.")
            else:
                print("Student not found.")
        except FileNotFoundError:
            print("No records found.")

            

    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
