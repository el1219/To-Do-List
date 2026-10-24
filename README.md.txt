# To-Do List

A simple command-line to-do list built in Python. Tasks are saved to a file, so they're still there the next time you open the program.

## Features
- `add`: add a new task
- `list`: show all tasks, with `[ ]` for pending and `[x]` for done
- `done`: mark a task as done
- `delete`: remove all tasks with a given title
- Automatically saves and loads tasks from `todos.json`
- Starts cleanly even when the data file doesn't exist yet


## What I learned
I built this with a `Task` class and a `TodoList` class that holds a list of tasks. I used JSON to save and load both the title and the done status, and `try / except` to handle a missing data file.