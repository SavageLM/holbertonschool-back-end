#!/usr/bin/python3
"""Saves all tasks assigned to a user in JSON format"""
import json
import requests
from sys import argv

API_URL = 'https://jsonplaceholder.typicode.com'


def exp_to_JSON():
    """Exports data to a JSON file"""
    USER_ID = argv[1]
    # Getting User data
    user_data = requests.get(f"{API_URL}/users/{USER_ID}").json()

    # Getting Todo Data
    todo_data = requests.get(f"{API_URL}/todos?userId={USER_ID}").json()

    # Prepping Data to be saved
    data = {
        USER_ID: [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_data['username']
            }
            for task in todo_data
        ]
    }
    # Creating file to write to
    with open(f'{USER_ID}.json', 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    exp_to_JSON()
