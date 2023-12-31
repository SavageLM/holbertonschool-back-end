#!/usr/bin/python3
"""Saves all tasks assigned to a user in CSV format"""
import csv
import requests
from sys import argv


def exp_to_CSV():
    """Exports data to a CVS file"""
    user_id = argv[1]
    source = 'https://jsonplaceholder.typicode.com/'
    todo_url = f"{source}users/{user_id}/todos"

    # Getting User data
    user_req = requests.get(source + f'users/{user_id}')
    user_data = user_req.json()
    # Getting Todo Data
    todo_req = requests.get(todo_url)
    todo_data = todo_req.json()
    # Creating file to write to
    with open(f'{user_id}.csv', 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        # Looping through todo Data to write each task
        for tasks in todo_data:
            username = user_data.get('username')
            task_status = tasks.get('completed')
            title = tasks.get('title')

            record = [user_id, username, task_status, title]
            writer.writerow(record)


if __name__ == '__main__':
    exp_to_CSV()
