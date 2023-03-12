import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="demopythondb"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Define functions for each CRUD operation
#EmpId,	EmpName,	Gender,	Birthday,	Country,Company	,	Department,Chucvu,	Salary
def create_employee(EmpId, EmpName, Gender, Birthday, Country, Company, Department, Chucvu, Salary):
  sql = "INSERT INTO employee (EmpId, EmpName, Gender, Birthday, Country, Company, Department, Chucvu, Salary) VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s)"
  val = (EmpId, EmpName, Gender, Birthday, Country, Company, Department, Chucvu, Salary)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "bản ghi được thêm mới.")

def read_employees():
  mycursor.execute("SELECT * FROM employee")
  myresult = mycursor.fetchall()
  for row in myresult:
      print(row)
      
def soft_emp_by_salary():
  mycursor.execute("SELECT * FROM employee order by Salary desc")
  myresult = mycursor.fetchall()
  # myresult = sorted(myresult, key=lambda x: x.Salary, reverse=True)
  for row in myresult:
      print(row)
      
def update_employee(EmpName, Gender, Birthday, Country, Company, Department, Chucvu, Salary, EmpId):
  sql = f"UPDATE employee SET EmpName = %s, Gender = %s, Birthday = %s, Country = %s, Company = %s, Department = %s, Chucvu = %s, Salary = %s WHERE EmpId = %s"
  val = (EmpName, Gender, Birthday, Country, Company, Department, Chucvu, Salary, EmpId)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "bản ghi được cập nhật.")

def view_detail(EmpId):
  sql = f"SELECT * FROM employee WHERE EmpId = %s"
  val = (EmpId,)
  mycursor.execute(sql, val)
  myresult = mycursor.fetchone()
  print(myresult)
    
def delete_employee(id):
  sql = "DELETE FROM employee WHERE EmpId = %s"
  val = (id,)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "bản ghi đã xoá.")

# Define a function for the search operation

def search_employee(value):
  sql = f"SELECT * FROM employee WHERE EmpName LIKE %s"
  val = ("%" + value + "%",)
  mycursor.execute(sql, val)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

# Define a menu to interact with the user

while True:
  print("Choose an operation:")
  print("1. Thêm mới nhân viên")
  print("2. Hiển thị thông tin các nhân viên")
  print("3. Sắp xếp và hiển thị thông tin các nhân viên giảm dần theo lương")
  print("4. Cập nhật thông tin nhân viên")
  print("5. Xem thông tin chi tiết của nhân viên theo mã")
  print("6. Tìm kiếm thông tin nhân viên theo tên")
  print("7. Xoá nhân viên")
  print("8. Thoát")
  
  choice = input("Vui lòng nhập lựa chọn của bạn: ")

  if choice == "1":
    EmpId = input("Nhập mã nhân viên: ")
    EmpName = input("Nhập tên nhân viên: ")
    Gender = input("Nhập giới tính của nhân viên (Nam/Nữ): ")
    Birthday = input("Nhập ngày sinh (yyyy-mm-dd): ")
    Country = input("Nhập quê quán: ")
    Company = input("Nhập tên công ty: ")
    Department = input("Nhập tên phòng ban: ")
    Chucvu = input("Nhập chức vụ: ")
    Salary = input("Nhập lương: ")
    create_employee(EmpId, EmpName, Gender, Birthday, Country, Company, Department, Chucvu, Salary)

  elif choice == "2":
    read_employees()

  elif choice == "3":
    soft_emp_by_salary()
    
  elif choice == "4":
    EmpId = input("Nhập mã nhân viên cần cập nhật: ")
    EmpName = input("Nhập tên nhân viên mới: ")
    Gender = input("Nhập giới tính của nhân viên (Nam/Nữ): ")
    Birthday = input("Nhập ngày sinh (yyyy-mm-dd): ")
    Country = input("Nhập quê quán: ")
    Company = input("Nhập tên công ty: ")
    Department = input("Nhập tên phòng ban: ")
    Chucvu = input("Nhập chức vụ: ")
    Salary = input("Nhập lương: ")
    update_employee(EmpName, Gender, Birthday, Country, Company, Department, Chucvu, Salary, EmpId)
    
  elif choice == "5":
    EmpId = input("Nhập mã nhân viên muốn xem chi tiết: ")
    view_detail(EmpId)

  elif choice == "6":
    Key = input("Nhập tên nhân viên muốn tìm kiếm: ")
    search_employee(Key)
  elif choice == "7":
    EmpId = input("Nhập mã nhân viên muốn xoá: ")
    delete_employee(EmpId)
    
  elif choice == "8":
    print("Cảm ơn bạn đã sử dụng...")
    break

  else:
    print("Lựa chọn không hợp lệ")