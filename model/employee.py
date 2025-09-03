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
  
  