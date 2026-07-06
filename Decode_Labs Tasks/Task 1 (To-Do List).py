my_tasks=[]
while True:
  print("\n","="*15,"TO-DO LIST","="*15,"\n")
  print("Press 1 to add task")
  print("Press 2 to delete task")
  print("Press 3 to view tasks")
  print("Press 4 to exit")

  choice=int(input("Enter your choice: "))
  if(choice==1):
    task=input("Enter your task: ")
    my_tasks.append(task)
  elif(choice==2):
        found=False
        task_to_remove=input("Enter the task you want to remove: ")
        for task in my_tasks:
            if task.lower()==task_to_remove.lower():
                my_tasks.remove(task)
                print("Task Removed... ")
                found=True
                break
            else:
                    print("Task not found ")
  elif(choice==3):
        if(len(my_tasks)==0):
            print("You have no tasks: ")
        else:
                print("Your tasks are: ")
                for i,task in enumerate(my_tasks,start=1):
                    print(i,task)
  elif(choice==4):
               print("Exiting Program.... ")
               break
  else:
   print("Invalid choice!!!")



