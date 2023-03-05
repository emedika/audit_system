import os
import datetime as dt

"""Checking the correct user input"""
while True:
    name = input("Please enter your name: ")
    surname = input("Please enter your surname: ")
    personalID = input("Please enter your personal ID: ")

    if name == "" or surname == "" or not personalID:
        print("Please enter your name, surname and personal ID. These fields cannot be empty.")
    else:
        personalID = int(personalID)
        break

def createFile(personal_id):
    """Create a file with personal ID"""
    fileName = name + "_" + surname + ".txt"
    filePath = path + "/" + fileName
    with open(filePath, "w") as file:
        file.write(str(personal_id))

"""Create a folder with today's date. Check if the folder already exists"""
currentDate = dt.date.today()
parent_dir = "/home/sgtuser/sgt/audit_system/"
directory = str(currentDate)
path = os.path.join(parent_dir, directory)

if os.path.exists(path) == False:
    os.mkdir(path)

if len(os.listdir(path)) == 0:
    print("The folder is empty. Creating a new file")
    createFile(personalID)
else:
    duplicateID = False
    for textFile in os.listdir(path):
        if textFile.endswith(".txt"):
            with open(path + "/" + textFile, "r") as file:
                fileID = int(file.read())
                if fileID == personalID:
                    print("Personal ID already exists.")
                    duplicateID = True
                    break
    if duplicateID == False:
        createFile(personalID)

"""Output information"""
if(len(os.listdir(path)) == 0):
    print("The folder is empty. Nothing to output")
else:
    for textFile in os.listdir(path):
        if textFile.endswith(".txt"):
            print("\n")
            print(f'Name: {textFile.split("_")[0]} \nSurname: {textFile.split("_")[1].replace(".txt", "")}')
            with open(path + "/" + textFile, "r") as file:
                fileID = str(file.read())
                print(f'Personal ID: {fileID}')
