# todocli

A command-line To-Do List application written in Python.

## Features

- Add tasks
- List tasks
- Complete tasks
- Delete tasks

## Installation

First, clone the repository and install the package:

```sh
git clone https://github.com/lymvs/to_do_list.git
cd to_do_list
```

It is recommended to use a virtual environment:

```sh
python -m venv .venv
source .venv/bin/activate
```

Then install the package:

```sh
pip install .
```

## Usage

After installation, use the `todocli` command:

```sh
todocli --help
todocli add "Buy groceries"
todocli list
todocli complete "Buy groceries"
todocli delete "Buy groceries"
```

## Requirements

- Python 3.8+
- [tabulate](https://pypi.org/project/tabulate/)

## Development

To install dependencies for development:

```sh
pip install -r requirements.txt
```

## To-Do

Adding more feature. Ideas:
- Edit tasks
- Create projects
- Warn about overdue tasks
- Prioritize tasks
- Export tasks (e.g. to csv or json)
- Keep statistics
- Mark tasks as important

## License

This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for details.