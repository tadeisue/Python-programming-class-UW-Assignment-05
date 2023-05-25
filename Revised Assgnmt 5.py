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
    print()
    if strChoice.strip() == '1':
        print("The current items ToDo are: ")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        continue
    elif strChoice.strip() == '2':
     strTask = str(input("What is the task? -")).strip()
     strPriority = str(input("What is the priority? [high|low] -").strip())
     dicRow = {"Task": strTask, "Priority": strPriority}
     lstTable.append(dicRow)
     print("Current Data in table:")
     print("The current items ToDo are: ")
     for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
     continue
    elif strChoice.strip() == '3':
     strKeyToRemove = input("Which TASK would you like removed? - ")
     blnItemRemoved = False
     intRowNumber = 0
     for row in lstTable:
         task,priority = dict(row).values()
         if task == strKeyToRemove:
                del lstTable[intRowNumber]
                blnItemRemoved = True
         intRowNumber += 1
     if(blnItemRemoved == True):
        print("The task was removed.")
     else:
        print("I'm sorry, but I could not find that task.")
        print("The current items ToDo are: ")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        continue
    elif strChoice.strip() == '4':
        print("The current items ToDo are: ")
        for row in lstTable:
             print(row["Task"] + "(" + row["Priority"] + ")")
        if "y" == str(input("Save this data to file? (y/n) -")).strip().lower():
            objFile = open(objFileName, "w")
        for dicRow in lstTable:
                objFileName.write(lstRow["Task"] + "," + lstRow["Priority"] + "\n")
        objFile.close()
        input("Data saved to file! Press the [Enter] key to return to the menu.")
        continue

    elif strChoice == '5':
         break