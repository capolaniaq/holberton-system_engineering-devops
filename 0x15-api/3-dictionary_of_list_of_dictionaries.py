#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
and generate the file.json"""

import json
import requests

if __name__ == "__main__":

    file_data = {}
    for i in range(1, 11):
        t_url = 'https://jsonplaceholder.typicode.com/todos?userId=' + str(i)
        todos_response = requests.get(t_url)
        user_url = 'https://jsonplaceholder.typicode.com/users/' + str(i)
        user_response = requests.get(user_url)

        task = {}
        tasks_status = []
        user_name = user_response.json().get("username")

        for user in todos_response.json():
            task["username"] = user_name
            task["task"] = user.get("title")
            task["completed"] = user.get("completed")
            tasks_status.append(task)
            task = {}
        file_data[str(i)] = tasks_status

    with open('todo_all_employees.json', 'w') as file:
        json.dump(file_data, file)
