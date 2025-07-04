import argparse

from src.parser import initiate_parser
from src.positional_args import (
    add_task,
)


def main():
    args = initiate_parser()

    if args.command == "add":
        tasks = add_task(args)



if __name__ == "__main__":
    main()
