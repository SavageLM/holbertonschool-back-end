#!/usr/bin/python3
"""Gets User information from the specified API"""
import requests
import sys


def print_employee_tasks(emp_id):
    """Prints a given Employee's to do list"""
    source = "https://jsonplaceholder.typicode.com"
    user_url = f"{source}/users/{emp_id}"
    todo_url = f"{source}/todos"
    emp_data = requests.get(user_url).json()
    todo_list = requests.get(todo_url, params={"userId": emp_id}).json()

    emp_name = emp_data.get("name")
    done_tasks = []
    for task in todo_list:
        if task["completed"]:
            done_tasks.append(task["title"])
    all_len = len(todo_list)
    done_len = len(done_tasks)

    print(f"Employee {emp_name} is done with tasks({done_len}/{all_len}):")
    for title in done_tasks:
        print(f"\t {title}")


if __name__ == "__main__":
    print_employee_tasks(int(sys.argv[1]))
