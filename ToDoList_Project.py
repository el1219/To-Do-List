
import json

class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done


    def describe(self):
        if self.done == False:
            return f"[ ] {self.title.capitalize()}"

        else:
            return f"[x] {self.title.capitalize()}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def list_all(self):
        for x in self.tasks:
            print(x.describe())     

    def mark_done(self, title):
        for x in self.tasks:
            if title == x.title:
                x.done = True
                return f"{title} marked as done"
        return f"{title} does not exist"

    def delete(self, title):
        before = len(self.tasks)
        self.tasks = [x for x in self.tasks if title != x.title]
        removed = before - len(self.tasks)
        if removed == 0:
            return f"{title} does not exist in the list"
        return f"{removed} task(s) named {title} deleted"

    def save(self, filename):
        lst = []
        for x in self.tasks:
            lst.append({"title": x.title, "done" : x.done})
        with open(filename, "w") as f:
            json.dump(lst, f)

    def load(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
        for d in data:
            self.add(Task(d["title"], d["done"]))

todo = TodoList()

try:
    todo.load("todos.json")

except FileNotFoundError:
    pass

while True:
    cmd = input("add / list / done/ delete/ quit: ").lower()
    if cmd == "add":
        title = input("Title: ").lower()
        todo.add(Task(title))

    elif cmd == "list":
        todo.list_all()

    elif cmd == "done":
        d = input("Pick one to mark done: ").lower()
        print(todo.mark_done(d))

    elif cmd == "delete":
        d = input("Pick to delete: ").lower()
        print(todo.delete(d))

    elif cmd == "quit":
        todo.save("todos.json")
        break
    
    else:
        print("Invalid input")