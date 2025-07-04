"""Helper functions."""
import argparse
import datetime


def valid_date(s: str) -> datetime.datetime:
    """Check if input date is valid, else raise error."""
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d").replace(
            tzinfo=datetime.timezone.utc,
            )
    except ValueError:
        error_msg = f"not a valid date {s!r}"
        raise argparse.ArgumentTypeError(error_msg)
