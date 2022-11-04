import requests
import json

headers = {
    "Content-Type": "application/json",
    "Connection": "keep-alive",
}

try:
    request = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/employees")
    employeesFromResponse = request.json()["Items"]
    employees = []
    for emp in employeesFromResponse:
        # create your new employee here
        # Call CreateEmployee class?
        # instantiate the new employee into the array to view: employee = Employee(emp) & employees.append(employee)
        print(emp)
except requests.exceptions.HTTPError as err:
    print(err)
