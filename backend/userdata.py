import csv
from services.userinsert import UserData
from datetime import datetime

userModule = UserData()

myFile = open('addUser.csv', mode='r', encoding='utf-8-sig')
reader = csv.DictReader(myFile)
myList = list()
for dict in reader:
    # myList.append(dict)
    dateString = dict["createdAt"]
    splitStringArray = dateString.split(" UTC")
    datePart = splitStringArray[0]
    datePartCoverted = datetime.strptime(datePart, '%Y-%m-%d %H:%M:%S')

    dict["createdAt"] = datePartCoverted

    myList.append(dict)
    un = dict["username"]
    crAt = dict["createdAt"]
    fn = dict["fullName"]
    pswd = dict["password"]
    userModule.addUserObjects(un, crAt, fn, pswd)

# print(type(myList[0]["createdAt"]))
# print(datePart)
# print(type(datetime.strptime(datePart, '%Y-%m-%d %H:%M:%S')))
# print(myList[2])
