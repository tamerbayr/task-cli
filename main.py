import datetime

progress_types = {0: "todo", 1: "in-progress", 2: "done"}
progress_convert = {"todo": 0, "in-progress": 1, "done": 2, "1": 1, "2": 2, "0": 0, "ToDo": 0}


class Node:
    def __init__(self, priority=0, progress=0, data=None, createTime=None, updateTime=None):
        self.priority = priority
        self.progress = progress
        self.data = data
        self.next = None
        if createTime is None:
            self.createTime = datetime.datetime.now()
            self.updateTime = self.createTime
        else:
            self.createTime = createTime
            self.updateTime = updateTime


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def get_head(self):
        return self.head

    def add(self, node):
        # check if progress input is valid
        node.progress = int(node.progress)
        if node.progress not in progress_types:
            raise ValueError(
                f"Invalid progress value: {node.progress}. Valid values are {list(progress_types.keys())}")

        # add to the linked list
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

        self.count += 1

    # update a specific attribute of a node
    def update_field(self, index, field, value):
        if not self.head:
            print("This list is empty!")
            return

        if index < 0 or index >= self.count:
            print("Index out of range!")
            return

        current = self.head
        for i in range(index):
            current = current.next

        if hasattr(current, field):
            setattr(current, field, value)
            current.updateTime = datetime.datetime.now()

    # to decide which attribute to change
    def update(self, index, field, value):
        self.update_field(index-1, field, value)

    def delete(self, index):
        if not self.head:
            print("This list is empty!")
            return

        if index < 0 or index > self.count:
            print("Index out of range!")
            return

        if index == 1:
            self.head = self.head.next

        else:
            current = self.head
            for i in range(index - 2):
                current = current.next

            print(f"Task at index {index} deleted.")
            current.next = current.next.next

        self.count -= 1

    @staticmethod
    def display_properties(current):
        return f"Priority: {current.priority}, Progress: {progress_types[current.progress]}, Data: {current.data}, Created at: {current.createTime}, Last update: {current.updateTime}"

    # lists all tasks if progress arg is not specified, lists tasks with only stated progress otherwise
    def display(self, progress=None):
        current = self.head
        count = 1
        if progress is None:
            while current:
                print(f"{count}- {self.display_properties(current)}")
                current = current.next
                count += 1
        else:
            if progress in progress_types.items():
                progress = progress_types.items()
            while current:
                if current.progress == progress:
                    print(f"{count}- {self.display_properties(current)}")
                current = current.next
                count += 1


class Commands:
    def __init__(self):
        self.ll = ll

    def execute(self, command):
        parts = command.split()

        if not parts:
            print("No command entered!")
            return

        command_input = parts[0].lower()
        try:
            if command_input == "add":
                # add <priority> <progress> <data>
                if len(parts) < 2:
                    print("You must enter at least a description for the task!")
                    return

                # set default values
                priority = 0
                progress = 0
                data = None

                if len(parts) == 2:
                    data = parts[1]
                elif len(parts) == 3:
                    priority = int(parts[1])
                    data = parts[2]
                elif len(parts) == 4:
                    priority = int(parts[1])
                    progress = int(progress_convert[parts[2]])
                    data = parts[3]
                else:
                    print("Unexpected amount of arguments! Format: add <priority> <progress> <data>")
                    return

                node = Node(priority=priority, progress=progress, data=data)
                self.ll.add(node)
                print(f"Task added: Priority {node.priority}, Progress {progress_types[node.progress]}, Data '{node.data}'")

            elif command_input == "display":
                # display [progress]
                if len(parts) == 2:
                    progress = int(parts[1])
                    self.ll.display(progress)
                else:
                    self.ll.display()

            elif command_input == "delete":
                # delete <index>
                if len(parts) < 2:
                    print("Usage: delete <index>")
                    return

                index = int(parts[1])
                self.ll.delete(index)

            elif command_input == "update":
                # update <index> <field> <value>
                if len(parts) < 4:
                    print("Usage: update <index> <field> <value>")
                    return

                index = int(parts[1])
                field = parts[2]
                value = parts[3]
                if field == "progress":
                    value = progress_convert[value]
                self.ll.update(index, field, value)

                print(f"Task at index {index} updated: {field} = {parts[3]}")

            elif command_input == "exit":
                print("Saving... Please wait.")
                with open("tasklist.json", "w") as file:
                    head = ll.get_head()
                    while head:
                        file.write(f"{head.priority},{head.progress},{head.data},{head.createTime},{head.updateTime}\n")
                        head = head.next

                print("Exiting task-cli. Goodbye!")
                exit()

            else:
                print(f"Unknown command: {command_input}")

        except ValueError as e:
            print(f"Invalid value: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


ll = LinkedList()
tasks = Commands()
try:
    with open("tasklist.json", "r") as f:
        first_char = f.read(1)
        if first_char:
            f.seek(0)
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    ll.add(Node(int(parts[0]), parts[1], parts[2], parts[3], parts[4]))
except FileNotFoundError:
    print("tasklist file is not found. Do not panic if this is your first launch.")


while True:
    cmd = input("task-cli: ")
    tasks.execute(cmd)

""" test
#progress: 0 means 'todo', 1 means 'in-progress' and 2 means 'completed'
ll.add(Node(priority=1, progress=0, data="Task 1"))
ll.add(Node(priority=2, progress=1, data="Task 2"))
ll.add(Node(priority=1, progress=2, data="Task 3"))

print("tasks:")
ll.display()

print("\nin progress:")
ll.display(1)

print("\npriority-sorted list:")
ll.sorted_display()
# """
