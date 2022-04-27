import git
from git import Repo
from datetime import datetime
from datetime import date
import os
import time

changing_file = "numCommits.txt"


def update():
    
    today = date.today()
    
    today_date = today.strftime("%b-%d-%Y")
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")[:-3]
    
    new_write = ("Day of Last Commit - " + today_date + "\n"
                 "Time of Last Commit - " + current_time)

   # print(new_write)
    
    with open(changing_file, 'w') as file:
        file.write(new_write)
    

def commit():
    
    repo = git.Repo("C:\\Users\\nvans\\Desktop\\Github")
    repo.index.add(changing_file)
    repo.index.commit("Commit from Script")
    #origin = repo.remote('origin')
    #origin.push()


num = int(input("Number of Commits: "))

#start = time.time()
for i in range(num):
    update()
    commit()
    print("Committ # " + str(i))
    i+=1

os.system('git push')
#end = time.time()
#print(end - start)