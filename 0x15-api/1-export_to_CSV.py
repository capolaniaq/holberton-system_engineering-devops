#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    todos_response = requests.get(todos_url)
    user_url = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    user_response = requests.get(user_url)

    task = []
    tasks_status = []
    user_name = user_response.json().get("username")
    name_file = '{}.csv'.format(int(argv[1]))

    for user in todos_response.json():
        task.append(str(int(argv[1])))
        task.append(str(user_name))
        task.append(str(user.get("completed")))
        task.append(str(user.get("title")))
        tasks_status.append(task)
        task = []

    myfile = open(name_file, 'w')
    with myfile:
        writer = csv.writer(myfile)
        writer.writerows(tasks_status)
