# Task Scheduler
# You're building a task scheduler application. Create a Python program that:
# - Lets users input tasks with due dates.
# - Displays a list of tasks due within the next week.
# - Offers the option to mark tasks as completed or remove them from the list.

import datetime as dt
import json
import os
import sys

if sys.platform == 'win32':
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system("clear")


f_name="task_data.json"

def put_data(task=None):
    with open(f_name,'w') as f:
        json.dump(task,f)
    return task


def get_data(task=None):
    with open(f_name) as f:
        task=json.load(f)
    return task

# def get_inputs():
#     t_name=input("enter the task name:")
#     start_date=input("enter the date[yyyy,mon,date]:")
#     due_date=input("enter the date[yyyy,mon,date]:")
#      get_input()

def create_task():
    if not os.path.exists(f_name):
        put_data()
        create_task()
    else:
        t_name=input("enter the task name:")
        start_date=input("enter the start date[yyyy,mon,date]:")
        due_date=input("enter the end date[yyyy,mon,date]:")
        now = dt.datetime.today().date()
        next = dt.datetime.strptime(due_date,"%Y,%m,%d").date()
        r_days=(next - now).days
        tasks=get_data()
 
        if tasks:
            for task in tasks:   
                if task["name"] == t_name:
                #     print("name already exists")
                #     input()
                #     clear()
                #     return display()
                    # or
                    raise ValueError("name already exists")
            t_data={"name":t_name,"start_date":start_date,"due_date":due_date,"remain_days":r_days,"completed":None}
            tasks.append(t_data)
            
            
            put_data(tasks)
            print("Task created")
            input()
            clear()

            
        else:
            task=[]
            t_data={"name":t_name,"start_date":start_date,"due_date":due_date,"remain_days":r_days,"completed":None}
            task.append(t_data)
            
            put_data(task)
            print("Task created")
            
            input()
            clear()
    return display()   

# def next_due():
#     tasks=get_data()
#     if tasks:
     
#         name=input("enter the name of the task:\n")
#         for task in tasks:
#             if task["name"] == name:
#                 print(task)
#                 # print(f"Name of the task is:".ljust(30),f"{task['name']}")
#                 # print(f"Start date of task is:".ljust(30),f"{task['start_date']}")
#                 # print(f"Due date of task is:".ljust(30),f"{task['due_date']}")
#                 # print(f"Remaining days of task is:".ljust(30),f"{task['remain_days']}")
#                 input()
#                 clear()
#     return display()


def complete_task():
    tasks = get_data()
    if tasks:
        print(tasks)
        name=input("Enter the task name:\n")
        for task in tasks:
            # if task["name"] == name:
                if task["remain_days"]<=0:
                    task["completed"] = True
                    put_data(task)
                    print(f"{task['name']} is completed")
                    input()
                    clear()
                else:
                    task["completed"] = False
                    put_data(task)   
                    print(f"{task['name']} is not completed")
                    input()
                    clear()    
                return display()
            
def remove_com_task():
    task=get_data()
    
    if task:
        task=list(filter(lambda i : i["remain_days"]>0,task))
        
        put_data(task)
        t_name=input("enter the task name:")
        p=[f"{t_name} is inprogress" if t["name"] == t_name else f"{t_name} is removed" for t in task]       
        print(p) 
        input()
        clear()
    #     print(f"{t_name} is inprogress")
    #     input()
    #     clear()
    # else:
    #     print(f"{t_name} is removed")
    #     input()
    #     clear()
        return display()


def balance_task():
    task=get_data()
    if task:
        for t in task:
         
            print("remaining task:\n")
            put_data(task)
            print(f"Name of the task is:".ljust(30),f"{t['name']}")
            print(f"Start date of task is:".ljust(30),f"{t['start_date']}")
            print(f"Due date of task is:".ljust(30),f"{t['due_date']}")
            print(f"Remaining days of task is:".ljust(30),f"{t['remain_days']}")
            input()
            
            clear()
    else:
        print("no task")
        input()
        clear()
    return display()

def exit():
    print("Exit the program....")
    input()
    clear()
    

def display():
    clear()
    print("Task scheduler".center(100))
    option=int(input("1.create_task\n2.complete_task\n3.remove_completed_task\n4.balance_task\n5.exit\n"))
   
    fns={
        1:create_task,
        
        2:complete_task,
        3:remove_com_task,
        4:balance_task,
        5:exit
    }
    return fns[option]()
display()

# def display():
#     while True:
#         option=int(input("1.create_task\n2.next_due\n3.com_task\n"))
#         if create_task(1):
#             return create_task
#         if next_due(2):
#             return next_due
#     # elif option == '2':1

#     #     next_weak_task()
#     # elif option == '3':
#     #     com_task()
#     # elif option == '4':
    #     exit()
    # else:
    #     print("invalid input")

display()
    


    