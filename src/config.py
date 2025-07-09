"""Configuration for the Bootstodo application."""

POSITIONAL_ARGS = {
    "list": "List all tasks",
    "add": "Add a task",
    "delete": "Delete a task",
    "edit": "Edit a task",
    "complete": "Mark a task as completed",
    }

OPTIONAL_ARGS = {}

FILE_NAME = ".bootstodo"

# Program Configurations
PROGRAM_NAME = "bootstodo"
PROGRAM_DESC = "Manage your tasks with magical efficiency"
PROGRAM_EPILOG = """
"Organization is the first spell every wizard bear learns."
- Boots the Wizardly Task Master

May your tasks be completed with the swiftness of a bear's paw!
        """

# Json format
JSON_FORMAT = {
    "name": "Give a name of description of the task",
    "priority": "[Optional] Define the priority of the task [low, medium, high]",
    "due_date": "[Optional] Specify due date [yyyy-mm-dd]",
    "completed": "[Optional] False by default",
}

TAB_LENGTH = "20"
