#!/usr/bin/python3
"""
This script uses a REST API to gather the TODO
list progress of an employee
"""


import requests
import sys

def get_employee_progress(employee_id):
    """
    Fetches and displays the progress of an employee's Todo List from an API.
     Args:
         employee_id (int): The employee id
    """

    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = {}/users/{}.format(base_url, employee_id)
    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status() #Check for bad status codes
        employee_name = user_response.json().get("name")
    except requests.exceptions.RequestException as e:
        print("Error fetching user data: {}".format(e), file=sys.stder)
        return
    total_tasks = len(todos_data)
    done_task_titles = [
        task.get("title")
        for task in todos_data
        if task.get("completed") is True
    ]
    done_tasks = len(done_task_titles)
    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks))
    for title in done_task_titles:
        print("\t {}".format(title)
    __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gtather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
sys.exit(1)

