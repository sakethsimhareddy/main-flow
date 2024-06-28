import mysql.connector
from tkinter import *
from tkinter import messagebox

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="CompanyDB"
    )

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
            EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
            FirstName VARCHAR(255) NOT NULL,
            LastName VARCHAR(255) NOT NULL,
            BirthDate DATE,
            Position VARCHAR(255)
        )
    ''')
    conn.close()
    messagebox.showinfo("Info", "Table 'Employees' created successfully")

def insert_data():
    conn = connect_db()
    cursor = conn.cursor()
    sql = "INSERT INTO Employees (FirstName, LastName, BirthDate, Position) VALUES (%s, %s, %s, %s)"
    val = (entry_first_name.get(), entry_last_name.get(), entry_birth_date.get(), entry_position.get())
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    messagebox.showinfo("Info", "Data inserted successfully")

def update_data():
    conn = connect_db()
    cursor = conn.cursor()
    sql = "UPDATE Employees SET Position = %s WHERE FirstName = %s AND LastName = %s"
    val = (entry_position.get(), entry_first_name.get(), entry_last_name.get())
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    messagebox.showinfo("Info", "Data updated successfully")

def delete_data():
    conn = connect_db()
    cursor = conn.cursor()
    sql = "DELETE FROM Employees WHERE FirstName = %s AND LastName = %s"
    val = (entry_first_name.get(), entry_last_name.get())
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    messagebox.showinfo("Info", "Data deleted successfully")

def query_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employees")
    rows = cursor.fetchall()
    conn.close()
    
    text_box.delete(1.0, END)
    
    for row in rows:
        text_box.insert(END, f"{row}\n")

root = Tk()
root.title("Database Management System")

Label(root, text="First Name").grid(row=0, column=0)
Label(root, text="Last Name").grid(row=1, column=0)
Label(root, text="Birth Date (YYYY-MM-DD)").grid(row=2, column=0)
Label(root, text="Position").grid(row=3, column=0)

entry_first_name = Entry(root)
entry_first_name.grid(row=0, column=1)
entry_last_name = Entry(root)
entry_last_name.grid(row=1, column=1)
entry_birth_date = Entry(root)
entry_birth_date.grid(row=2, column=1)
entry_position = Entry(root)
entry_position.grid(row=3, column=1)

Button(root, text="Create Table", command=create_table).grid(row=4, column=0, pady=10)
Button(root, text="Insert Data", command=insert_data).grid(row=4, column=1, pady=10)
Button(root, text="Update Data", command=update_data).grid(row=5, column=0, pady=10)
Button(root, text="Delete Data", command=delete_data).grid(row=5, column=1, pady=10)
Button(root, text="Query Data", command=query_data).grid(row=6, column=0, pady=10)

text_box = Text(root, width=50, height=10)
text_box.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
