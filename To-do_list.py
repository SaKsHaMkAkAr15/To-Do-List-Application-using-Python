import csv 

to_do = []

try:
    with open('to_do.csv', "r") as file:
        reader = csv.reader(file)  
        for row in reader:         
            to_do.append({"Name":row[0], "Status": row[1]})
except FileNotFoundError:
    pass

while True:
    print("\n---To-Do List Menu---")
    print("1. Add something to do")
    print("2. View your tasks")
    print("3. Mark the task as done")
    print("4. Delete the task")
    print("5. Exit the application")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter the Task Name: ")
        status = "Pending"
        to_do.append({"Name":name, "Status":status})
        with open("to_do.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, status])
        print("Task added successfully!")
    
    elif choice == '2':
        print("\nYour Tasks:")
        for i, item in enumerate(to_do):
            print(f"{i+1}. {item['Name']} - {item['Status']}")
    
    elif choice == '3':
        task_num = int(input("Enter task number to mark as done: "))
        index = task_num - 1
        to_do[index]['Status'] = "Done"
        with open("to_do.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for item in to_do:
                writer.writerow([item['Name'], item['Status']])
        print("Task marked as done!")

    elif choice == '4':
        task_num = int(input("Enter task number to delete: "))
        index = task_num - 1
        to_do.pop(index)
        with open("to_do.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for item in to_do:
                writer.writerow([item['Name'], item['Status']])
        print("Task deleted!")

    elif choice == '5':
        print("Exiting....")
        break

    else:
        print("Invalid Choice!")
        


