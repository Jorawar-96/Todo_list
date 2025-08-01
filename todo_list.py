import json


def load_task():
    try:
        with open("todo_container.json","r") as file:
            return json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        return []   
def save_task(tasks):
    with open("todo_container.json","w") as file:
        json.dump(tasks,file,indent=4)

def add_task(task_id,tasks):
    num_of_task = int(input("Enter the number of task : "))
    for i in range(num_of_task):
        task_data = input("Enter the task : ")
        task = {"id":task_id,"task_data":task_data,"done":False}
        tasks.append(task)
        save_task(tasks)
        print("Task Added Successfully\n")
        task_id+=1

def update_task(tasks):
    existing_data_id = int(input("Enter the task number that you want to update : "))
    found = False
    for task in tasks:
        if task["id"]==existing_data_id:
            if task["done"]:
                print("You cannot update this task because it is already done.\n")
                return
            else:
                new_data = input("Enter the new task : ").strip()
                if new_data =="":
                    print("task cannot be empty")
                    return
                task["task_data"] = new_data
                found = True
                save_task(tasks)
                print("Task Updated Successfully\n")

def show_task(tasks):
    print("To Do List : ")
    for index,task in enumerate(tasks):
        status = "✔️ " if task["done"] else "⚠️   Not Done"
        print()
        print(f"{index+1}. {task['task_data']} - {status}")
    print()

def delete_task(tasks):
    show_task(tasks)
    delete_task_id = int(input("Enter the task number for delete : "))-1
    if 0<=delete_task_id<len(tasks):
        if not tasks[delete_task_id]["done"]:
            print("You cannot delete this task becasue it is not done yet.\n")
        else:
            removed = tasks.pop(delete_task_id)

            for index2,task in enumerate(tasks):
                task.pop("id")

            # reset index after deleteion of task
            for index1,task in enumerate(tasks):
                task["id"] = index1+1
        
            save_task(tasks)
            print("Deleted successfully...\n")

def mark_task(tasks):
    task_index = int(input("Enter the task number of task : ")) -1
    if 0<=task_index<len(tasks):
        if tasks[task_index]["done"]:
            print("It is already done..!\n")
        else:
            tasks[task_index]["done"] = True
            save_task(tasks)
            print("Marked successfully .....!\n")
    else:
        print("Number does not exist")

def todo_list():
    tasks = load_task()
    task_id =max([task["id"] for task in tasks], default=0)+1
    while True:
        print("-------------To Do List ------------\n")
        print("1. Add tasks")
        print("2. Update tasks")
        print("3. Show tasks")
        print("4. Delete task")
        print("5. Mark task as done")
        print("6. Exit\n")

        choice = int(input("Enter the choice : "))
        print()
        
        if choice==1:
            add_task(task_id,tasks)

        elif choice ==2:
            update_task(tasks)

        elif choice==3:
            show_task(tasks)

        elif choice==4:
            delete_task(tasks)

        elif choice==5:
            mark_task(tasks)

        elif choice==6:
            print("\nExisting to do list \nGood Bye....!")
            break

        else:
            print("\nInvalid choice ----- \nPlease enter the choice betweeen 1 to 5 \n")
        

todo_list()
