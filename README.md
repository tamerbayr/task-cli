# task-cli
A simple task list that runs on the Python terminal.

This is a beginner project I created using the guidelines from [roadmap.sh's Task Tracker Project](https://roadmap.sh/projects/task-tracker).

## How to use
**IMPORTANT:** Always use the `exit` command to exit; otherwise, all of your changes will be lost.

Run `main.py` or the standalone executable `task-cli.exe`. Use the provided commands to manage your task list. The program saves all data to `tasklist.json`, which will be created in the same directory after you exit the program for the first time.

Each task has the following attributes:
1. **Priority**: Accepts any integer. Default is `0`.
2. **Progress**: Indicates the progress of your task. Accepts only the following values:
   - `0`: ToDo
   - `1`: In Progress
   - `2`: Done  
   Default is `0`. You can use either numbers or keywords (e.g., "todo", "in-progress", "done") when interacting with the program.
3. **Data**: Description of your task. Accepts any string.
4. **Creation Time**: Automatically assigned when a task is created.
5. **Update Time**: Automatically assigned when a task is updated.

## Commands
- **add** `priority` `progress` `data`  
  Adds a new task. At least the `data` field must be specified. If only two arguments are given, the program assumes the first argument is `priority`.
  
- **delete** `index`  
  Deletes the task at the specified index.

- **display**  
  Displays your entire task list.
  
- **display** `priority`  
  Displays tasks with the specified `priority`.

- **update** `index` `field (priority/progress/data)` `new_value`  
  Updates a specific field of a task with a new value.

- **exit**  
  Saves and exits the program. Always use this when you're done to ensure your changes are saved.

https://github.com/tamerbayr/task-cli/tree/release
