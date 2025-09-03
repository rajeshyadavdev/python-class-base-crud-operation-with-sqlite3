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
    
  
  
  
  
  
    
    
  
    
    