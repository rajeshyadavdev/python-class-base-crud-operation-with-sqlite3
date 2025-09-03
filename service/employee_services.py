from abc import ABC,abstractmethod

class EmployeeServices(ABC):
  
  @abstractmethod
  def create_employee(self,name,age,city):
    ...
    
  @abstractmethod
  def get_all_employee(self):
    ...  
    
  @abstractmethod
  def get_employee_detail(self,emp_id):
    ...   
    
  @abstractmethod
  def update_employee(self,emp_id,name=None,age=None,city=None):
    ...   
    
  @abstractmethod 
  def delete_employee(self,emp_id):
    ...  