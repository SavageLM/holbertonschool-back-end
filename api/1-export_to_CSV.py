#!/usr/bin/python3
"""Saves all tasks assigned to a user in CSV format"""
import csv
import requests
from sys import argv


def exp_to_CSV():
    """Exports data to a CVS file"""
    source = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]

    user_req = requests.get(source + f'users/{user_id}')
    user_data = user_req.jdon()

    todo_req = requests.get(source + 'todos', params={'userID': user_id})
    todo_data = todo_req.json()

    with open(f'{user_id}.csv', 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for tasks in todo_data:
            username = user_data.get('username')
            task_status = tasks.get('completed')
            title = tasks.get('title')

            record = [user_id, username, task_status, title]
            writer.writerow(record)


if __name__ == '__main__':
    exp_to_CSV()
