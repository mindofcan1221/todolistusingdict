# a simple to do list program
#this uses a single file to register the tasks and their status
#it uses a dictionary data structure to do that
from datetime import date
import ast
tasks = {}
current_date = date.today()
#filename1 = 'tasks.txt'
#filename2='status.txt'
filename = 'todolist.txt'
print("#### A simple to do list program.###")
print("####1.to enter the list of your tasks.###")
print("####2.to enter the status of each task.###")
mychoice = "Enter your choice"
choice = int(input(mychoice+">"))

#list your daily tasks
if choice ==1:
    count = 0
    myfile = open(filename,'w')
    print("\n Enter your tasks.")
    print("Enter 'exit' to stop")
    while True:
        yourtask = input(f"Enter your task {len(tasks)+1 }:")
        if yourtask.lower()=='exit':
            print("You can come next and fill their status")
            break
        else:
                tasks[yourtask] = 'unspecified'

    #write the date and tasks on task.txt file
    myfile.write("Date:"+str(current_date))
    myfile.write("\n"+str(tasks)) 
    print("Tasks have been saved to", filename)  

#list the status of your tasks     
elif choice ==2:
    myfile = open(filename,'r')
    list_str = myfile.readlines()
    taskdic= eval(list_str[1])
    taskdickeys=list(taskdic.keys())
    
    count = 0
    print("\n Enter status of your tasks as complete/incomplete.")
    print("Enter 'exit' to stop")
    while True:
        yourstatus = input("Status of task "+taskdickeys[count]+":")
        if yourstatus.lower()=='exit':
            break
        else:
            taskdic[taskdickeys[count]] = yourstatus
            count+=1
            if count == len(taskdic): break
    
    '''while count<len(taskdic):
        tasks.append("unspecified")
        count+=1''' 

    myfile=open(filename,'a')
    myfile.write("\n"+str(taskdic))
    print("The status of your work are now updated")
#if other values are entered   
else:
    print("Enter the right choice")
