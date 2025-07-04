# to_do_list
Add task functionality:
- store to a json file having the following structure:
    - task: {
        "id": 1, # auto-generated
        "name": "some name", # From user input
        "priority": "medium", # default or user defined
        "due_date": "2025-08-15", # optional, from user
        "created_at": "2025-06-20", # auto-generated
        "completed": False, # default of user defined
    } 