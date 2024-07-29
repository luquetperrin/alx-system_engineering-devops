#!/usr/bin/python3
"""Fetches information from JSONPlaceholder API and exports to JSON"""

from json import dump
from requests import get
from sys import argv

def fetch_json(url):
    """Fetch JSON data from a URL and handle potential errors."""
    try:
        response = get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return None

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_result = fetch_json(users_url)

    if users_result is None:
        print("Failed to fetch users.")
        exit(1)

    big_dict = {}
    for user in users_result:
        todo_list = []
        user_id = user.get("id")
        username = user.get("username")

        todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        todo_result = fetch_json(todos_url)

        if todo_result is None:
            print(f"Failed to fetch todos for user ID {user_id}.")
            continue

        for todo in todo_result:
            todo_dict = {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            todo_list.append(todo_dict)

        big_dict[user_id] = todo_list

    with open("todo_all_employees.json", 'w') as f:
        dump(big_dict, f, indent=4)
