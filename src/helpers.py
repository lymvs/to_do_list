"""Helper functions."""
import argparse
import datetime
import os

from src.config import FILE_NAME


def valid_date(s: str) -> datetime.datetime:
    """Check if input date is valid, else raise error.

    Args:
        s (str): The date string to validate, expected format is YYYY-MM-DD.

    Returns:
        datetime.datetime: The parsed date in UTC timezone if valid.

    """
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d").replace(
            tzinfo=datetime.timezone.utc,
            )
    except ValueError:
        error_msg = f"not a valid date {s!r}"
        raise argparse.ArgumentTypeError(error_msg)


def generate_file_path() -> str:
    """Generate the file path.

    This function constructs the full path to the file where tasks are stored.
    It uses the home directory of the current user and appends the predefined file name.

    Returns:
        str: The full path to the file.

    """
    return os.path.join(os.path.expanduser("~"), FILE_NAME)
