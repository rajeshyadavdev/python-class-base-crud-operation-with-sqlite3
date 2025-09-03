# python-class-base-crud-operation-with-sqlite3

## 📌 Overview
This project is a simple **CRUD (Create, Read, Update, Delete)** application built with **Python** and **SQLite3** using **Object-Oriented Programming (OOP)** concepts.  
It demonstrates how to interact with an SQLite database through Python classes and methods in a clean and modular way.

---

## ⚡ Features
- Create a new record in the database  
- Read (fetch) existing records  
  - `fetchall`  
  - `fetchone`  
- Update records  
- Delete records  
- Uses **SQLite3** (lightweight, no external database server required)  
- Designed with **OOP principles** for better structure and maintainability  

---

## 🛠️ Tech Stack
- **Python 3.10+**  
- **SQLite3** (built-in Python module)  

---

## 📂 Project Structure
emp/
├── dao/
│ ├── init.py
│ └── database.py
├── model/
│ ├── init.py
│ └── employee.py
├── service/
│ ├── init.py
│ └── employee_services.py
├── service_impl/
│ ├── init.py
│ └── employee_services_impl.py
├── main.py


---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/rajeshyadavdev/python-class-base-crud-operation-with-sqlite3.git
cd emp
2️⃣ Run the app
bash
Copy code
python main.py
🖥️ Usage (Menu-Driven CLI)
When you run main.py, you’ll see:

rust
Copy code
Enter 1->insert-emp,
      2->get-all-emp,
      3->get-sigle-emp,
      4->update-emp,
      5->delete-emp,
      6->exit:
👉 Example Flow:

Add a new employee (name, age, city)

View all employees

Fetch single employee by ID

Update employee details

Delete an employee

Exit the program

