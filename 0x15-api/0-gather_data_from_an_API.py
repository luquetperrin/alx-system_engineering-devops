#!/usr/bin/python3
"""
Uses the JSON placeholder API to query data about an employee's TODO list progress.
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
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

    todo_num = len(todo_result)
    todo_complete = len(
        [todo for todo in todo_result if todo.get("completed")]
    )
    name = name_result.get("name")

    print(f"Employee {name} is done with tasks({todo_complete}/{todo_num}):")
    for todo in todo_result:
        if todo.get("completed"):
            print(f"\t {todo.get('title')}")

