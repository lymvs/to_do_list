"""Adding and parsing command line arguments for the todocli application."""
import argparse

from .helpers import (
    valid_date,
)


def add_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """Add arguments to the parser for the add command."""
    parser.add_argument(
        "name",
        type=str,
        help="name of the new task",
    )
    parser.add_argument(
        "-p",
        "--priority",
        choices=["low", "medium", "high"],
        default="medium",
        type=str,
        help="priority of the task",
    )
    parser.add_argument(
        "-d",
        "--due",
        type=valid_date,
        help="due date of the task in YYYY-MM-DD format",
    )
    parser.add_argument(
        "-c",
        "--completed",
        action="store_true",
        default=False,
        help="mark the task as completed",
    )
    parser.add_argument(
        "-desc",
        "--description",
        type=str,
        help="description of the task",
    )
    return parser


def list_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """Add arguments to the parser for the list command."""
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="list all tasks, including completed ones",
    )
    parser.add_argument(
        "-l",
        "--limit",
        type=int,
        default=10,
        help="limit the number of tasks displayed",
    )
    return parser


def delete_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """Add arguments to the parser for the delete command."""
    parser.add_argument(
        "name",
        type=str,
        help="name of the task to delete",
    )
    return parser


def complete_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """Add arguments to the parser for the complete command."""
    parser.add_argument(
        "name",
        type=str,
        help="name of the task to mark as completed",
    )
    return parser
