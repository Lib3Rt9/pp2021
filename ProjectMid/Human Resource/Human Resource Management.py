import math
import datetime
import pickle
import manager
import staff
from Domains.Manager import Manager
from Domains.Staff import Staff
from Domains.Employee import Employee
from Domains.Salary import Salary

def check_User_Account():
    f1 =open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Staffs.pickle", "rb") 
    temp = pickle.load(f1)
    f1.close()

    f2 =open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Manager.pickle", "rb") 
    temp.append(pickle.load(f2))
    f2.close()

    # check_User_Account() : Check if username and password correct, return a string
	#       if string = "A"
    #           run manager.main()
	#       else 
    #           run staff.main()
    username = input("Your username (Your ID) : ")
    while True:
        if not any (obj.id == username for obj in temp):
            print("Username not found !")
            username = input("Your Username (Your ID) : ")
        else:
            break
    for i in range(len(temp)):
        if temp[i].id == username:
            check = temp[i].password 

    password = input("Your password : ")
    while True:
        if password != check:
            print("Wrong password !")
            password = input("Your Password : ")
        else:
            break
    if username[0] == "A":
        return "A"
    else:
        return username[0] 

office = check_User_Account()
if office == "A":
    manager.main()
else:
    staff.main(office)