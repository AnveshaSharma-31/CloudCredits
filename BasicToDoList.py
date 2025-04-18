tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    print("\nYour Tasks:")
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")

print("*" * 10, "To-Do List", "*" * 10)

while True:
    print("\n1. Add Task\n2. Show Tasks\n3. Exit")
    choice = int(input("Enter Your Choice (1-3): "))

    if choice == 1:
        task = input("Enter your task: ")
        add_task(task)
        print("Task Added Successfully!")
    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            show_tasks()
    elif choice == 3:
        print("Thank You!!")
        break
    else:
        print("Invalid Choice!!! Please Enter Correct Option.")