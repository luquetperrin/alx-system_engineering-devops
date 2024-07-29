import json

# Sample data for demonstration purposes
tasks = {
    "1": [
        {"username": "Bret", "task": "delectus aut autem", "completed": False},
        {"username": "Bret", "task": "quis ut nam facilis et officia qui", "completed": False},
        # Add more tasks as needed
    ],
    "2": [
        {"username": "Antonette", "task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": False},
        # Add more tasks as needed
    ]
    # Add more users and their tasks as needed
}

# File name for the JSON file
file_name = "todo_all_employees.json"

# Write the data to the JSON file
with open(file_name, 'w') as file:
    json.dump(tasks, file, indent=4)

print(f"Data has been written to {file_name}")
