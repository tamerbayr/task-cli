# task-cli
A simple task list runs on Python terminal.

A beginner project I made using guidelines on https://roadmap.sh/projects/task-tracker

# How to use
!IMPORTANT - always use "exit" command to exit or all of your changes will be lost.

run main.py or task-cli.exe standalone executable. Use commands to make changes on your task list. The program will keep all of your data in tasklist.json file, which will be created in the same directory after you exit the program for the first time.

Each task has following attributes:
1- priority: accepts any integer. default is 0
2- progress: progress of your task. Accepts only the following: 0=ToDo, 1=in-progress, 2=done. default is 0. You can use the numbers or keywords while using the program.
3- data: description of your task. Accepts anything.
4- create time: creation time of your task. Assigned automatically.
5- uptade tine: last uptade time of your task. Assigned automatically.

# commands
<b>add</b> `priority` `progress` `data` - adds a new task. at least data must be specified. Assumes 1st argument is priority if only 2 arguments are given. <br>
<b>delete</b> `index` <br>
<b>display</b> - displays your tasklist <br>
<b>display</b> `priority` - displays tasks that has the specified progress <br>
<b>update</b> `index` `field (priority/progress/data)` `new_value` <br>
<b>exit</b> - save and exit. always use this when you're done. <br>

