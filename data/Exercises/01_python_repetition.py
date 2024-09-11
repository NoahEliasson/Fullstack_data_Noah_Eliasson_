import pandas as pd 

emp_info = []
def add_employee(emp_id, name, dep, salary):
    
    emp_dict = {"emp_id": emp_id, "name": name, "department": dep, "salary": salary}
    emp_info.append(emp_dict)

add_employee(0, "alice", "HR", 31000)
add_employee(1, "Bob", "IT", 41000)
add_employee(2, "Charlie", "HR", 28000)

name = [(d["name"]) for d in emp_info]


#for n in range(3):
#    get_name = emp_info[n]["name"]
#    get_salary = emp_info[n]["salary"]
#    get_dep = emp_info[n]["department"]
#    first_name = f"{get_name}"
#    department = f"{get_dep}"
#    salary = f"{get_salary}"
#    print(f"{first_name} works in department {department} and earns {salary}")

for employee in emp_info:
    print(f"{employee['name']} works in the {employee['department']} department and earns {employee['salary']}")


df = pd.DataFrame(emp_info)
df