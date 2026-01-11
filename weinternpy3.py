import sqlite3

# open connection to sqlite database
# if database file is not present, it will be created automatically
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# creating employee table if it does not already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    salary REAL
)
""")
conn.commit()


def add_employee():
    # taking employee details from user
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))

    # inserting data safely using parameterized query
    cursor.execute(
        "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
        (name, department, salary)
    )
    conn.commit()
    print("Employee added successfully.\n")


def view_employees():
    # fetching all employee records
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    if not employees:
        print("No employee records found.\n")
    else:
        print("\nEmployee List:")
        for emp in employees:
            print(emp)
        print()


def update_employee():
    # updating salary of an employee using id
    emp_id = int(input("Enter employee ID to update salary: "))
    new_salary = float(input("Enter new salary: "))

    cursor.execute(
        "UPDATE employees SET salary = ? WHERE id = ?",
        (new_salary, emp_id)
    )
    conn.commit()
    print("Employee salary updated.\n")


def delete_employee():
    # deleting an employee record using id
    emp_id = int(input("Enter employee ID to delete: "))

    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (emp_id,)
    )
    conn.commit()
    print("Employee record deleted.\n")


# main menu loop
while True:
    print("----- Employee Database Menu -----")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee Salary")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        print("Program closed.")
        break
    else:
        print("Invalid choice. Please try again.\n")

# closing database connection
conn.close()