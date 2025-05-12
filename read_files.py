employee_file = open("employees.txt", "r")

print("Readable: " + str(employee_file.readable()))
for employee in employee_file.readlines():
    print(employee)
employee_file.close()