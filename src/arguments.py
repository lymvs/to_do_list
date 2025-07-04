import argparse

from src.helpers import (
    valid_date,
)


def add_add_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
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
        help="mark the task as completed",
    )
    return parser
