from service_impl.employee_services_impl import EmployeeServiceImpl

service_impl = EmployeeServiceImpl()

def main():
  
  while True:
    input_data = int(input(
      """
        Enter 1->insert-emp, 2->get-all-emp, 3->get-sigle-emp, 4->update-emp,5->delete-emp, 6->exits:
      """
    ))
    match input_data:
      case 1:
        name = input("Enter Employee Name:")
        age = int(input("Enter Employee Age:"))
        city = input("Enter Employee City:")
        service_impl.create_employee(name=name,age=age,city=city)
        print("Employee Inserted into database.")
      case 2:
        emp_list = service_impl.get_all_employee()
        print(emp_list)
      case 3:
        id = int(input("Enter Employee ID:"))
        emp = service_impl.get_employee_detail(id=id)
        print(emp)
      case 4:
        id = int(input("Enter Employee ID:"))
        name = input("Enter Employee Name:")
        age = int(input("Enter Employee Age:"))
        city = input("Enter Employee City:")
        emp=service_impl.update_employee(id=id,name=name,age=age,city=city)
        print(f"Employee updated with  id:{id}.")
      case 5:
        id = int(input("Enter Employee ID:"))
        service_impl.delete_employee(id=id)
        print(f"Employee Deleted with ID:{id}")
      case 6:
        break
      case _:
        print("Invalide Input Please Try Again..")        
  
if __name__ == "__main__":
  main()  


