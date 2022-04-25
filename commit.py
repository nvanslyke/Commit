import git
from git import Repo
from datetime import datetime
from datetime import date

changing_file = "numCommits.txt"

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
    
    repo = git.Repo("C:\\Users\\nvans\\Desktop\\Github")
    repo.index.add(changing_file)
    repo.index.commit("Commit from Script")
    origin = repo.remote('origin')
    origin.push()

commit()