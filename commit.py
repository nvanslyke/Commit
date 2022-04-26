import git
from git import Repo
from datetime import datetime
from datetime import date
import os

changing_file = "numCommits.txt"
origing = None

def update():
    
    today = date.today()
    
    today_date = today.strftime("%b-%d-%Y")
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    new_write = ("Day of Last Commit - " + today_date + "\n"
                 "Time of Last Commit - " + current_time)

   # print(new_write)
    
    with open(changing_file, 'w') as file:
        file.write(new_write)
    

def commit():
    global origing
    repo = git.Repo("C:\\Users\\nvans\\Desktop\\Github")
    repo.index.add(changing_file)
    repo.index.commit("Commit from Script")
    origin = repo.remote('origin')
    origing = origin

num = input("how many commits? ")


for i in range(int(num)):
    update()
    commit()
    print("Committ # " + str(i))
    i+=1

origing.push