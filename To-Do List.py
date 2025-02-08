from rich import print
import os
import json

class NewTask:
    def __init__(self, task, date, categ_num, categories):
        self.task = task
        self.date = date
        self.categ_num = categ_num
        self.categories = categories

    def new_task(self):
        create_task = {
            "date": self.date, 
            "task": self.task, 
            "categories": self.categories[self.categ_num]
        }    
        with open("task.json", "w") as file:
            json.dump(create_task, file, indent=4)                     

def exit():
    while True:
        userIn = input("\nType [1] to exit: ")
        if userIn == "1":
            clear_screen()
            main()
            break

def create_task():    
    print("\n[bright_cyan]Create new Task[/bright_cyan]")  
    while True:
        task = input("\nWhat is to be done?: ")
        date = input("\nDue date: ")   
        categories = {"1": "Default", "2": "Personal", "3": "Shopping"}
        for index, value in enumerate(categories):            
            print(f"\n{index + 1}. {categories[value]}")
        categ_num = input("\nAdd to list: ")        
        if not (task and date and list):
            clear_screen()
            print("\n[red]Empty input, try again[/red]")      
        print("\n[green]Task creation success![/green]")      
        newtask = NewTask(task, date, categ_num, categories)   
        newtask.new_task()           
        exit()   
        break                                                                        
                                                                                             
def main():
    print("[bright_cyan]To-do List App[/bright_cyan]")
    print("\n1. Task Categories\n2. Create new task\n2. Display all task\n3. Edit Task\n4. Delete Task\n5. Task Completion")
    feat_func = {"2": create_task}
    while True:
        mainIn = input("\nType number to continue: ")    
        if mainIn in feat_func:
            clear_screen()
            feat_func[mainIn]()                      
            break
        print("\n[red]Invalid input, try again[/red]")   
        
def clear_screen():
    os.system('cls' if os.name == 'nt' else "clear")                                

if __name__ == "__main__":
    main()                
           