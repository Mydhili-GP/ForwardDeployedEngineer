employee_deatils=[{"employee_id": 101, "employee_name": "JohnMac", "employee_salary": 50000}, 
                  {"employee_id": 102, "employee_name": "Jane", "employee_salary": 60000},
                  {"employee_id": 103, "employee_name": "DoeSwiss", "employee_salary": 55000},
                  {"employee_id": 104, "employee_name": "SmithNot found", "employee_salary":  70000}]
for employee in employee_deatils:
   if employee["employee_salary"] < 250000 and len(employee["employee_name"]) > 6:
       print(employee["employee_name"])