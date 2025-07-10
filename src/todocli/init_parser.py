"""Initiate a parser for the Bootstodo application."""
import argparse

from .arguments import (
    add_args,
    complete_args,
    delete_args,
    # edit_args,
    list_args,
)
from .config import (
    PROGRAM_DESC,
    PROGRAM_EPILOG,
    PROGRAM_NAME,
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
    parser_add = add_args(parser_add)

    parser_list = subparsers.add_parser("list", help="List all tasks")
    parser_list = list_args(parser_list)

    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete = delete_args(parser_delete)

    parser_complete = subparsers.add_parser("complete", help="Mark a task as completed")
    parser_complete = complete_args(parser_complete)

    return parser.parse_args()
