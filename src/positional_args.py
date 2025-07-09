"""Functions for managing tasks in a todo list application."""
import argparse
import json
import os
from datetime import datetime

from src.config import TAB_LENGTH
from src.helpers import generate_file_path


def list_tasks(args: argparse.Namespace) -> str:
    """List all tasks in the todo list.

    Args:
        args (argparse.Namespace): The command line arguments containing options for
        listing tasks.

    Returns:
        str: A list of all tasks or a message indicating no tasks are found.

    """
    todo_path = generate_file_path()

    if not os.path.exists(todo_path):
        return "No tasks found."

    try:
        with open(todo_path, "r") as f:
            tasks = json.load(f)
    except json.JSONDecodeError:
        return "Error reading tasks. The file may be corrupted."
    except Exception as e:
        return f"An error occurred while reading tasks: {e}"

    task_list = []
    for task in tasks:
        dt = datetime.fromisoformat(task["due_date"]).strftime("%Y-%m-%d %H:%M:%S") if task["due_date"] else "No due date"
        task_info = f"{task['name']:<{TAB_LENGTH}} | {task['priority']:<{TAB_LENGTH}} | {dt:<{TAB_LENGTH}} | {'Yes' if task['completed'] else 'No':<{TAB_LENGTH}} | {task['description'] if task['description'] else 'No description'}"
        task_list.append(task_info)

    if args.limit:
        task_list = task_list[:args.limit]

    return "\n".join(task_list) if task_list else "No tasks found."


def add_task(args: argparse.Namespace) -> str:
    """Add a new task to the todo list.

    Args:
        args (argparse.Namespace): The command line arguments containing task details.

    Returns:
        str: A message indicating success or an error.

    """
    try:
        todo_path = generate_file_path()
        if todo_path == "":
            raise FileNotFoundError("File path is empty.")
    except Exception as e:
        return f"An error found: {e}"

    # Load exisiting tasks or start with an empty list
    if os.path.exists(todo_path):
        with open(todo_path, "r") as f:
            tasks = json.load(f)
    else:
        tasks = []

    new_task = {
        "name": args.name,
        "priority": args.priority,
        "due_date": args.due.isoformat() if args.due else None,
        "completed": args.completed,
        "description": args.description if args.description else None,
    }

    # Add the new task and save to file
    tasks.append(new_task)
    try:
        with open(todo_path, "w") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        return f"An error found: {e}"
    else:
        return "Task added successfully!"


def delete_task(args: argparse.Namespace) -> str:
    """Delete a task from the todo list.

    Args:
        args (argparse.Namespace): The command line arguments containing the task name to delete.

    Returns:
        str: A message indicating success or an error.

    """
    todo_path = generate_file_path()

    if not os.path.exists(todo_path):
        return "No tasks found."

    try:
        with open(todo_path, "r") as f:
            tasks = json.load(f)
    except json.JSONDecodeError:
        return "Error reading tasks. The file may be corrupted."
    except Exception as e:
        return f"An error occurred while reading tasks: {e}"

    # Filter out the task to delete
    new_tasks = [task for task in tasks if task["name"] != args.name]

    if len(new_tasks) == len(tasks):
        return f"No task found with the name '{args.name}'."

    try:
        with open(todo_path, "w") as f:
            json.dump(new_tasks, f, indent=4)
    except Exception as e:
        return f"An error found: {e}"
    else:
        return "Task deleted successfully!"


def complete_task(args: argparse.Namespace) -> str:
    """Mark a task as completed in the todo list.

    Args:
        args (argparse.Namespace): The command line arguments containing the task name to mark as completed.

    Returns:
        str: A message indicating success or an error.

    """
    todo_path = generate_file_path()

    if not os.path.exists(todo_path):
        return "No tasks found."

    try:
        with open(todo_path, "r") as f:
            tasks = json.load(f)
    except json.JSONDecodeError:
        return "Error reading tasks. The file may be corrupted."
    except Exception as e:
        return f"An error occurred while reading tasks: {e}"

    # Find the task and mark it as completed
    for task in tasks:
        if task["name"] == args.name:
            task["completed"] = True
            break
    else:
        return f"No task found with the name '{args.name}'."

    try:
        with open(todo_path, "w") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        return f"An error found: {e}"
    else:
        return "Task marked as completed successfully!"
