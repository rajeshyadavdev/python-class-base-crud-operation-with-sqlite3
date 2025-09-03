print("****service_impl****")

from service.employee_services import EmployeeServices
from dao.database import EmployeeDatabase


class EmployeeServiceImpl(EmployeeServices):
  
  def __init__(self):
    self.db = EmployeeDatabase()
    
  def create_employee(self,name,age,city):
    return self.db.create(name=name,age=age,city=city)
  
  def get_all_employee(self):
    return self.db.get_all()
  
  def get_employee_detail(self,id):
    return self.db.get_detail(id=id)
    
  def update_employee(self,id,name,age,city):
    return self.db.update(id=id,name=name,age=age,city=city)
    
  def delete_employee(self,id):
    return self.db.delete(id=id)
      