
def task():
    task = []
    print("---It is your task for Today---")

    total_task = int(input("Emter the no. of task you want to create: "))
    for i in range(1 , total_task+1):
        task_name = input(f"Enter the task {i} = ")
        task.append(task_name)

    print(f"Your today's task are \n{task}")

    while True:
        print("\nChoose an Operation: ")
        print("1 - Add task")
        print("2 - Update task")
        print("3 - Delete task")
        print("4 - View task ")
        print("5 - Today task is over")

        try:
            operation = int(input("Enter your choice between (1-5): "))

        except ValueError:
            print("Please enter a valid number")
            continue

        if operation == 1:
            add = input("Enter the task you want to add: ")
            task.append(add)
            print(f"Your {add} task has been added")

        elif operation == 2:
            update_val = input("Enter the task you want to update")
            if update_val in task:
                up = input("Enter the task = ")
                ind = task.index(update_val)
                task[ind] = up

                print(f"Task updated{up}")

        elif operation == 3:
            del_val = input("Enter the task you want to delete: ")
            if del_val in task:
                ind = task.index(del_val)
                del task[ind]

                print(f"Task deleted{del_val}")

        elif operation == 4:
            print(f"The total task{task}")

        elif operation == 5:
            print("Today task is over")

task()
