tasks= []
while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2.View Tasks")
    print("3.Delete Task")
    print("4.Exit")

    choice=input("Enter your choice: ")
    if choice=="1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice=="2":
        print("\nYour Tasks: ")
        for i,task in enumerate(tasks,1):
            print(f"{i}. {task}")

    elif choice=="3":
        task_number=int(input("Enter task number to delete: "))
        tasks.pop(task_number-1)
        print("Task deleted!")

    elif choice=="4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
