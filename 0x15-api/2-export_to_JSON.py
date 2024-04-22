#!/usr/bin/python3
""" Fetching data into Json file. """
import requests
import sys
import json


def fetch_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = f"{base_url}/{employee_id}/todos"

    # Fetching employee data
    employee_response = requests.get(f"{base_url}/{employee_id}")
    employee_data = employee_response.json()
    user_id = employee_data["id"]
    username = employee_data["username"]

    # Fetching TODO list
    todo_response = requests.get(todo_url)
    todo_list = todo_response.json()

    # Constructing JSON data
    json_data = {
        str(user_id): [],
    }

    for task in todo_list:
        task_completed_status = "true" if task["completed"] else "false"
        json_data[str(user_id)].append({
            "task": task["title"],
            "completed": task_completed_status,
            "username": username
        })

    # Writing data to JSON file
    filename = f"{user_id}.json"
    with open(filename, "w") as file:
        json.dump(json_data, file)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
