"""Configuration for the todocli application."""

FILE_NAME = "todocli.json"
HEADERS = ["Name", "Priority", "Due Date", "Completed", "Description"]

# Program Configurations
PROGRAM_NAME = "todocli"
PROGRAM_DESC = "A Simple Command Line Todo List Manager"
PROGRAM_EPILOG = """
Examples:
  todocli list
  todocli add "Buy groceries" --priority high --due 2023-10-31
  todocli delete "Buy groceries"
  todocli complete "Buy groceries"
"""
