employee_details=[{"emp_id": 1, "name": "John", "age": 30, "department": "IT", "salary": 50000},
                   {"emp_id": 2, "name": "JaneJane", "age": 25, "department": "HR", "salary": 40000},
                     {"emp_id": 3, "name": "MikeMikeMike", "age": 35, "department": "Finance", "salary": 60000}]

for employee in employee_details:
    if len(employee["name"])>6 and employee["salary"]>50000:
        print(employee["name"] + " is eligible for promotion")


    