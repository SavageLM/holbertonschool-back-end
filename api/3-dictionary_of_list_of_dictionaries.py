#!/usr/bin/python3
"""Saves all tasks assigned to all users in JSON format"""
import json
import requests
from sys import argv

API_URL = 'https://jsonplaceholder.typicode.com'


def all_to_JSON():
    """Exports data to a JSON file"""

    # Getting Todo Data
    todo_data = requests.get(f"{API_URL}/todos").json()

    # Prepping Data to be saved
    data = {}
    for task in todo_data:
        # Getting User ID
        user_id = task['userId']
        # Pulling User Data
        user_data = requests.get(f"{API_URL}/users/{user_id}").json()
        # Checking if user is already in Data dict
        if user_id not in data:
            data[user_id] = []
        # Adding todo data to UserID list
        data[user_id].append({
            "username": user_data['username'],
            "task": task['title'],
            "completed": task['completed']
        })
    # Creating file to write to
    with open("todo_all_employees.json", 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    all_to_JSON()
