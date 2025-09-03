# python-class-base-crud-operation-with-sqlite3

# Python CRUD Application with SQLite3 (OOP Based)

## 📌 Overview
This project is a simple **CRUD (Create, Read, Update, Delete)** application built with **Python** and **SQLite3** using **Object-Oriented Programming (OOP)** concepts.  
It demonstrates how to interact with an SQLite database through Python classes and methods in a clean and modular way.

---

## ⚡ Features
- Create a new record in the database  
- Read (fetch) existing records  
    1.fetchall
	2.fetchone
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

emp
|--dao-|--__init__.py
|      |
|      |--database.py
|
|--model-|--__init__.py
|      	 |
|      	 |--employee.py
|
|--service-|--__init__.py
|      	   |
|          |--employee_services.py
|
|--server_impl-|--__init__.py
|              |
|              |--employee_services_impl.py
|
|--main.py


-----------------------
#database.py
-----------------------
import sqlite3
from model.employee import Employee

class EmployeeDatabase():
  def __init__(self):
    self.con = sqlite3.connect(database="employee.db")
    self.cursor = self.con.cursor()
    self.cursor.execute(
    """
      CREATE TABLE IF NOT EXISTS employee(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      age INTEGER,
      city TEXT)
    """
    ) 
     
  def create(self,name,age,city):
    query = 'INSERT INTO employee (name,age,city) VALUES (?,?,?)'
    self.cursor.execute(query,(name,age,city))
    self.con.commit()  
    
  def get_all(self):
    query = f"SELECT * FROM employee"
    self.cursor.execute(query)  
    return self.cursor.fetchall()
    
  def get_detail(self,id):
    query = f"SELECT * FROM employee WHERE id= {id}"
    self.cursor.execute(query)
    return self.cursor.fetchone() 
    
  
  def update(self,id,name=None,age=None,city=None):
    query = f"UPDATE employee SET name='{name}',age={age},city='{city}' WHERE id= {id}"
    self.cursor.execute(query)
    self.con.commit()
    
  def delete(self,id):
    query = f"DELETE FROM employee WHERE id={id}"
    self.cursor.execute(query)
    self.con.commit()
    
  
  ---------------
  employee.py
  ---------------
  class Employee():
  
  def __init__(self,id:int,name:str,age:int,city:str) -> None:
    self.__id:int = id
    self.__name:str = name
    self.__age:int = age
    self.__city:str = city
  
  # Getter methode
  def get_id(self)->int:
    return self.__id
  def get_name(self)->str:
    return self.__name
  def get_age(self)->int:
    return self.__age
  def get_city(self)->str:
    return self.__city
  
  # Setter method
  def set_id(self,id:int)->None:
    self.__id = id 
  def set_name(self,name:str)->None:
    self.__name = name 
  def set_age(self,age:int)->None:
    self.__age = age
  def set_city(self,city)->None:
    self.__city = city
    
  def __repr__(self):
    return f"Employee:(id:{self.__id},name:{self.__name},age:{self.__age},city:{self.__city})"  
  
  def to_dict(self)->dict:
    return(
      {
        "id":self.__id,
        "name":self.__name,
        "age":self.__age,
        "city":self.__city
      }
    )
    
if __name__  == "__main__":    
  emp = Employee(12,"Rahul",33,"Omaniya")  
  print(emp)  
  
  
  ----------------
  employee_services.py
  ----------------
  
  
  
  
    
    
  
    
    