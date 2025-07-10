"""Main entry point for the To-Do List application."""
from .init_parser import initiate_parser
from .positional_args import (
    add_task,
    complete_task,
    delete_task,
    list_tasks,
)


def main() -> None:
    """Main function to execute the To-Do List application."""
    args = initiate_parser()

    if args.command == "add":
        tasks = add_task(args)
    elif args.command == "list":
        tasks = list_tasks(args)
    elif args.command == "delete":
        tasks = delete_task(args)
    elif args.command == "complete":
        tasks = complete_task(args)

    print(tasks)


if __name__ == "__main__":
    main()
