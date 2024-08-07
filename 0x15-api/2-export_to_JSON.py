#!/usr/bin/python3
"""
Uses the JSON placeholder API to query data about an employee's TODO list
progress and exports the data in JSON format.
"""

from requests import get
from sys import argv
import json

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        exit(1)

    try:
        employee_id = int(argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        exit(1)

    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = f"{main_url}/users/{employee_id}/todos"
    name_url = f"{main_url}/users/{employee_id}"

    try:
        todo_result = get(todo_url).json()
        name_result = get(name_url).json()
    except Exception as e:
        print(f"Error fetching data: {e}")
        exit(1)

    if not todo_result or not name_result:
        print("Invalid employee ID or no data available.")
        exit(1)

    username = name_result.get("username")

    tasks = []
    for todo in todo_result:
        tasks.append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        })

    data = {str(employee_id): tasks}

    # Create the JSON file and write the data
    filename = f"{employee_id}.json"
    with open(filename, 'w') as file:
        json.dump(data, file)

    print(f"Data exported to {filename}")
