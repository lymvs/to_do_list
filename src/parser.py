import argparse

from src.config import (
    PROGRAM_DESC,
    PROGRAM_EPILOG,
    PROGRAM_NAME,
)
from src.helpers import (
    valid_date,
)
from src.arguments import (
    add_add_args,
)


def initiate_parser() -> argparse.Namespace:
    """Initiate a parser using program's configurations.

    Returns:
        argparse.Namespace: parsed command-line args as attributes

    """
    parser = argparse.ArgumentParser(
        prog=PROGRAM_NAME,
        description=PROGRAM_DESC,
        epilog=PROGRAM_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Implement positional arguments
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add = add_add_args(parser_add)

    parser_edit = subparsers.add_parser("edit", help="Edit a task")


    parser_list = subparsers.add_parser("list", help="List all tasks")
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_complete = subparsers.add_parser("complete", help="Mark a task as completed")

    return parser.parse_args()
