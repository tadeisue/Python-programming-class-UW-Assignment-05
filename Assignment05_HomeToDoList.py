# ------------------------#
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#         When the program starts, load each "row" of data
#         in "ToDoList.txt" into a python Dictionary.
#       Add eah dictionary "row" to a python list "table"
# ChangeLog (Who, When, What):
# Susan Tadei, 5-17-23, Created starter script
# Susan Tadei, Added code to complete assignment 5

#Step 1 - When the program starts, Load from ToDoList.txt into a python Dictionary.
#Step 2 - Display a menu of choices to the user
#Step 3 - Show the current items in the table
#Step 4 - Add a new item to the list/table
# Step4a - Show the current items in the table
#Step 5 - Remove a new item to the list/table
#Step 5a - Allow user to indicate which row to delete
#Step 5a - Show the current items in the table
#Step 5b - Update user on the status
#Step 5b - Ask if they want save that data
#Step 5c - Show the current items in the table
#Step 6 - Save tasks to the ToDoList.txt file
# -- Data --#
# Declare variables and constants
objFileName = "ToDoList.txt" # An object that represents a file
strData = "" # A row of text data from the file
dicRow = {} # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = [] # A dictionary that acts as a 'table' of rows
strChoice = "" # Capture the user option selection

#--Processing--#
objFile = open(objFileName, "r")
for line in objFile:
    strData = line.split(",")
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()
while(True):
    print("""
    Menu of Options
    1) Show current data.
    2) Add a new item.
    3) Remove an existing item)
    4) Save Data to File)
    5) Exit Program
""")
    strChoice = str(input("Which option would you like to perform? [1 to 4]: "))
    if strChoice == '1':
        print("******The current items ToDo are: *****")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("********************************************")
    continue
    elif strChoice == '2' :
        print("ToDo List:")
        strTask = str(input("What is the task? -")).strip()
        strPriority = str(input("What is the priority? [high|low] -")).strip()
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print("Current Data in table:")
        print("*****The current items ToDo are: *****")
   for row in lstTable:
       print(row["Task"] + "(" + row["Priority"] + ")")
       print("*********************************************")
   continue
    elif strChoice == '3':
        strKeyToRemove = input("Which TASK would you like removed? - ")
        blnItemRemoved = False
        intRowNumber = 0
        for row in lstTable:
        if task == strKeyToRemove:
            del lstTable[intRowNumber]
            blnItemRemoved = True
        intRowNumber += 1
    if(blnItemRemoved == True):
        print("The task was removed.")
    else:
        print("I'm sorry, but I could not find that task.")
    print("*****The current items ToDo are: *****")
    for row in lstTable:
        print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue
    elif strChoice == '4':
    print("*****The current items ToDo are: *****")
    for row in lstTable:
        print(row["Task"] + "(" + row["Priority"] + ")")
    print("**********************************************")
        if "y" == str(input("Save this data to file? (y/n) -")).strip().lower():
        objFile = open(objFileName, "w")
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        input("Data saved to file! Press the [Enter] key to return to the menu.")
    else:
        input("New data was NOT saved, but previous data still exists! Press the [Enter] key to return to menu.")
    continue
    elif strChoice == '5':
        break
