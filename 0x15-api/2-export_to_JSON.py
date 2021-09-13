#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
and generate the file.json"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    todos_response = requests.get(todos_url)
    user_url = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    user_response = requests.get(user_url)

    file_data = {}
    task = {}
    tasks_status = []
    user_name = user_response.json().get("username")
    name_file = '{}.json'.format(int(argv[1]))

    for user in todos_response.json():
        task["task"] = user.get("title")
        task["completed"] = user.get("completed")
        task["username"] = user_name
        tasks_status.append(task)
        task = {}

    file_data[str(int(argv[1]))] = tasks_status
    with open(name_file, 'w') as file:
        json.dump(file_data, file)
