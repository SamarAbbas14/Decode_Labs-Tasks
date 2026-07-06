total_expense=0
print("="*30)   
print("Expense Tracker")
print("="*30,"\n")
print("To close the program type exit ","\n")
while True:
 new_expense=input("Enter the amount of expense ")
 if(new_expense.lower()=="exit"):
  print("\nYour total expense is ",total_expense,"\n")
  break
 try:
    new_expense=int(new_expense)
    if(new_expense<0):
        print("Expense cannot be negative ","\n")
        continue
    total_expense+=(new_expense)

    
 except ValueError as e:
    print("You must give a value as an input ","\n")
    