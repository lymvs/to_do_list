import argparse

from src.constants import ARGS_DICT


def main():
    # read user's command
    parser = argparse.ArgumentParser()

    # List argument
    for key, value in ARGS_DICT.items():
        parser.add_argument(key, help=value)

    args = parser.parse_args()
    # if command is invalid, ask user to give a valid one and print available options
    # execute command
    # print back to user a response


if __name__ == "__main__":
    main()