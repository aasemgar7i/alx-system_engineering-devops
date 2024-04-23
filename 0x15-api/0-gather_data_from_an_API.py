#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


def fetch_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = f"{base_url}/{employee_id}/todos"

    # Fetching employee data
    employee_response = requests.get(f"{base_url}/{employee_id}")
    employee_data = employee_response.json()
    emp_n = employee_data["name"]

    # Fetching TODO list
    todo_response = requests.get(todo_url)
    todo_list = todo_response.json()

    # Calculating progress
    tot_t = len(todo_list)
    comp_t = sum(1 for task in todo_list if task["completed"])

    # Displaying progress
    print(f"Employee {emp_n} is done with tasks({comp_t}/{tot_t}):")
#    print(f"\t{emp_n}: {comp_t}/{tot_t}")

    # Displaying completed tasks
    for task in todo_list:
        if task["completed"]:
            print(f"\t\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
