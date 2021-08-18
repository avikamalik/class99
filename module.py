import os
import shutil
#print (os.system('date'))
#os.mkdir("/Users/prashantmalik/Desktop/boom/")
#print(os.getcwd())

#print(os.path.exists('/Users/prashantmalik/Desktop/python/'))
#print(os.path.splitext("/Users/prashantmalik/Desktop/Phython/swipe.txt")[1])
#print(os.listdir())


source=input("enter the name of the folder you want to import ☞  ")
destination=input("where do you want the folder to go ☞  ")

source=source+"/"
destination=destination+"/"
files=os.listdir(source)
for i in files:
    shutil.move((source+i),destination)



