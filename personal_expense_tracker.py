print("PERSONAL EXPENSE TRACKER")
print("Calculate-Analyze-Plan ")



print("1. Enter monthly budget")
print("2. Add expense")
print("3. View expenses")
print("4. Calculate total expenses")
print("5. View number of expenses")
print("6. Delete expense")
print("7. View remaining budget")
print("8. Exit")

expenses=[]
expenses_name=[]

while True:
   
    choice=input("Which option would you like to choose? 1/2/3/4/5/6/7/8:")

    if choice=="1":
        budget=(float(input("Please enter your monthly budget: (Enter 0 return to menu:)")))
        if budget==0:
            continue

    elif choice=="2":
        expense_name=input("Please enter your expense name:")
        expense=float(input("Please enter your expense"))
        expenses.append(expense) 
        expenses_name.append(expense_name)

    elif choice=="3":
        print("Here are your expenses")
        for i in range(len(expenses)):
            print(expenses_name[i],expenses[i])
        
    elif choice=="4":
        print("Here are your total expenses")
        print(sum(expenses))

    elif choice=="5":
        print("You have",len(expenses),"expenses.")  

    elif choice=="6":
        for i in range(len(expenses)):
            print( i+1,expenses_name[i],expenses[i])

        delete=int(input("Which expense would you like to delete? (Enter 0 return to menu:)"))
        if delete==0: 
            continue

        delete=delete-1

        expenses_name.pop(delete)
        expenses.pop(delete)

    elif choice=="7":
          remaining_budget=budget-sum(expenses)
          print(remaining_budget)
       
    elif choice=="8":
        print("Exit GoodBye!")
        break

    else: 
        print("Wrong Choice. Please try again")    