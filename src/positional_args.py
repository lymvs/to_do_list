import json
import os
import sys
import argparse

from src.config import FILE_NAME


def generate_file_path() -> str:
    """Generate the file path.

    This function constructs the full path to the file where tasks are stored.
    It uses the home directory of the current user and appends the predefined file name.

    Returns:
        str: The full path to the file.

    """
    return os.path.join(os.path.expanduser("~"), FILE_NAME)


def list_tasks() -> str:
    todo_path = generate_file_path()

    try:
        with open(todo_path, "r") as f:
            tasks = f.read()
            if tasks == "":
                return "No tasks found!"
            return tasks
    except FileNotFoundError:
        try:
            with open(todo_path, "w") as f:
                return list_tasks()
        except Exception as e:
            return f"An error found: {e}"


def add_task(args: argparse.Namespace) -> None:
    """Add a new task to the todo list.

    Args:
        args (argparse.Namespace): The command line arguments containing task details.

    Returns:
        None

    """
    try:
        todo_path = generate_file_path()
        if todo_path == "":
            raise FileNotFoundError("File path is empty.")
    except Exception as e:
        return f"An error found: {e}"

    new_task = {
        "name": args.name,
        "priority": args.priority,
        "due_date": args.due.isoformat() if args.due else None,
        "completed": args.completed,
    }

    try:
        with open(todo_path, "a") as f:
            json.dump(new_task, f, indent=4)
    except Exception as e:
        return f"An error found: {e}"
