#!/usr/bin/python3
""" list of Dict"""
import requests
import json


def fetch_all_employees_todo():
    base_url = "https://jsonplaceholder.typicode.com/users"

    # Fetching all employees
    employees_response = requests.get(base_url)
    employees_data = employees_response.json()

    # Constructing JSON data
    json_data = {}

    for employee in employees_data:
        user_id = employee["id"]
        username = employee["username"]

        # Fetching TODO list for each employee
        todo_url = f"{base_url}/{user_id}/todos"
        todo_response = requests.get(todo_url)
        todo_list = todo_response.json()

        # Constructing JSON data for the current employee
        employee_tasks = []
        for task in todo_list:
            task_completed_status = "true" if task["completed"] else "false"
            employee_tasks.append({
                "username": username,
                "task": task["title"],
                "completed": task_completed_status
            })

        json_data[str(user_id)] = employee_tasks

    # Writing data to JSON file
    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(json_data, file)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    fetch_all_employees_todo()
