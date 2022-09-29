#!/usr/bib/env/ python3

import json
from os.path import exists
from datetime import date
import os

caseID = ''

# Select which case ID
def setCaseID():
    global caseID
    caseID = input('Please select a Case ID')

# Add txt file with name of case ID
def addPerson():
    global caseID
    # Edit <Username> for windows
    file_exists = exists(f'C:/Users/<Username>/Desktop/Judo/{caseID}')
    if(file_exists == False):
        p = open(f'C:/Users/<Username>/Desktop/Judo/{caseID}', 'w')
        p.close()
    else:
        print('file exists')
        pass

# Record what date(s) the person has gone to practice
def recordDate():
    global caseID
    p = open(f'C:/Users/<Username>/Desktop/Judo/{caseID}', 'a')
    t = date.today()
    p.write(t.strftime("%m/%d/%Y") + "\n")
    p.close()
    pass

# Record/edit the total hours
def totalHours():
    global caseID
    file = open(f'C:/Users/<Username>/Desktop/Judo/{caseID}', 'a')
    hoursToday = input("Enter hours spent rolling today")
    file.write(f'{hoursToday}' + '\n')
    file.close()
    pass

# delete person's file (y tho?)
def delete():
    global caseID
    if exists(f'C:/Users/<Username>/Desktop/Judo/{caseID}'):
        os.remove(f'C:/Users/<Username>/Desktop/Judo/{caseID}')
        print("File Deleted")
        pass
    else:
        print(f"file with case ID {caseID} does not exist")
    pass

# Read a file
def read():
    global caseID
    file_read = open(f'C:/Users/<Username>/Desktop/Judo/{caseID}', 'r')
    line = file_read.readlines()
    print(caseID)
    for l in line:
        print(l.strip())
    pass

# List all commands
def help():
    list = ["create", "date", "read", "help", "time", "delete", "exit"]
    for item in list:
        print(item)
    pass


if __name__ == '__main__':
    run = True
    help()
    while(run==True):
        command = input("Enter command")
        try:
            if (command == "create"):
                setCaseID()
                addPerson()
            elif (command == "date"):
                setCaseID()
                recordDate()
            elif(command == "read"):
                setCaseID()
                read()
            elif(command == "time"):
                setCaseID()
                totalHours()
            elif(command == "delete"):
                setCaseID()
                delete()
            elif(command == "help"):
                help()
            elif(command == "exit"):
                run = False
            else:
                raise Exception("Command not recognized, please try again")
        except Exception as e:
            print(e)
            pass
