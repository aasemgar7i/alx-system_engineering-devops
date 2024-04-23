#!/usr/bin/python3
""" Fetching data into CSV file. """
import csv
import requests
import sys


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

    # Writing data to CSV file
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            task_completed_status = "True" if task["completed"] else "False"
            writer.writerow([user_id, username,
                             task_completed_status, task["title"]])

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
