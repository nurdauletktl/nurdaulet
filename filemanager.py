import os
import os.path


def Getinfo():
    print("0-exit/quit")
    print("1-to manage a file")
    print("2-to manage a dir")

def TeamManager():
    print("0- return to MainMenu")
    print("1- create new file")
    print("2- delete a file")
    print("3- rename file")
    print("4- add content")
    print("5- rewrite file")
    cmd = int(input())
    if cmd==0:
        return 0
    elif cmd==1:
        name=input("New file name: ")+".txt"
        Open=open(name,"tw")
        Open.close()
        print("file was created")
        TeamManager()
    elif cmd==2:
        name=input("delete which file: ")+".txt"
        try:
            os.remove(name)
        except FileNotFoundError:
             print("File doesn't found") 
        else :
             print("file was delete")
    elif cmd==3:
        name=input("old file name: ")+".txt"
        Nname=input("new file name: ")+".txt"
        os.rename(name,Nname)
        print("file name was change")
    elif cmd==4:
        name=input("open file")+".txt"
        Open=open(name,"at")
        content=input()          
        Open.write(content)
        Open.close()
    elif cmd==5:
        name=input("rewrite file")+".txt"
        Open=open(name,"wt")
        content=input()
        Open.write(content)
        Open.close()
def CurrentManager():
    print("0- return to menu")
    print("1- create new dir")
    print("2- rename dir")
    print("3- to determine your location")
    print("4- list content")
    print("5- number of file and dir")
    print("6- change your location")
    cmd = int(input("Cmd: "))
    if cmd==0:
        return 0
    elif cmd==1 :
        name= input("new dir's name: ")
        os.mkdir(name)
        print("dir created ")
    elif cmd==2:
        name=input("old dir name: ")+".txt"
        Nname=input("new dir name: ")+".txt"
        os.rename(name,Nname)
        print("dir name was change")  
    elif cmd==3:
       print("your dir is "+str(os.getcwd()))
    elif cmd==4:
        print(os.listdir())
    elif cmd==5:
        fileordir=input("1-file or 2-dir")
        if fileordir=="2":
            num=0
            for f in os.listdir():
                Dir=os.path.join(f)
                if os.path.isdir(Dir):
                    num=num+1
            print("number of dir is: ",num)
        elif fileordir=="1" :
            num=0
            for f in os.listdir():
                 File=os.path.join(f)
                 if os.path.isdir(File):
                   num=num+1
            print("number of dir is: ",num)   
    elif cmd == 6:
        print("Enter path to dir, for exmp:C:\... or D:\...")
        path=input("DIR: ")
        try:
            os.chdir(path)
        except ValueError:
            print("*It's Dir does not exist")
        except FileNotFoundError:
            print("*It's Dir does not exist")
        else :print("*You changed dir")
        
run=True
while run:
    Getinfo()
    cmd=int(input())
    if cmd==0:
        print("program will out")
        run=False 
    elif cmd==1:
        print("you in file manager")
        TeamManager()
    elif cmd==2:
        print("you in current location")
        CurrentManager()
