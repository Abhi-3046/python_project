todo_list = []
try:
  with open("tasks.txt", "r") as file:
    for line in file:
      todo_list.append(line.strip())
  print("Previous tasks loaded!")

except FileNotFoundError:
  print("No previous file found, starting fresh.")
  
  
while True:
  choice = input("Enter the option(1. Add, 2. View, 3. Remove, 4. save , 5.Exit): ")
  
  if choice.lower() == "5":
    print("see you soon🫡")
    break
  
  elif choice == "1" :
    add_task= input("Enter the task you needed: ")
    todo_list.append(add_task)
    print(f"Task added:{add_task}")
    
  elif choice == "2":
    print("\n--- current task---")
    
    if not todo_list :
      print("Empty! Nothing to do yet.😗")
    
    else:
        for i ,task in enumerate(todo_list, start=1):
          print(f"{i}.{task}")
  
  elif choice== "3":
    if not todo_list:
      print("Empty! Nothing to do yet. 😗")
    
    else:
      try:
        remove_task = int(input("Enter task number to remove: "))
      except ValueError:
        print("Please enter a valid number.")
        continue
      
      if 1 <= remove_task <= len(todo_list):
        removed = todo_list.pop(remove_task -1)
        print(f"Successfully deleted: {removed}")
      
      else:
        print("Invalid task number.")
  
    
  elif choice == "4":
        with open("tasks.txt", "w") as file:
          for task in todo_list:
            file.write(task + "\n")
        print("Tasks saved to tasks.txt! 💾")
    

  else:
    print("Invalid choice, pick 1–5.")
