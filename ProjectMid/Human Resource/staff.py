import math
import datetime
import pickle
from Domains.Manager import Manager
from Domains.Staff import Staff
from Domains.Employee import Employee
from Domains.Salary import Salary

def check_Date(DoB):
    #
    # Check:
    #     if _DoB_ is in form DD/MM/YYYY
    #         return _DoB_

    error = True
    while error == True:
        try:
            temp = DoB.split("/" , 2)
            x = datetime.datetime(int(temp[2]), int(temp[1]), int(temp[0]))
            DoB = (datetime.date.strftime(x, "%d/%m/%Y"))
            error = False
        except:
            DoB = input("\tTry again (DD/MM/YYYY) : ")
            error = True
    return DoB


def check_Gender(gender):
    #     
    # Check:
    #     if _gender_ is valid, "Male" or "Female"
    #         return _gender_

    while True:
        if gender == "Male" or gender == "Female":
            break
        else:
            gender = input("\tTry again (Male/Female) : ")
    return gender

def prevent_Duplicate(id, list):
    #
    # Prevent having same ID in the list
    #     return id

    while True:
        if any(obj.id == id for obj in list):
            id = input("ID already existed. Try again : ")
        else:
            break
    return id 


def employee_Count():
    #
    # Count employee
    # input number of employees as e_count
    #
    # If e_count < 11
    #     return an Integer

    e_count = input("Enter the number of employees (smaller than 11) : ")
    while True:
        try: 
            if int(e_count) < 11:
                e_count = int(e_count)
                break
            else:
                e_count = input("Try again (smaller than 11) : ")

        except:
                e_count = input("Integer only (smaller than 11) : ")             
    return e_count


def update_Employee(e_count, office):
    #     
    # Create a new list of e_count people
    #       return e_list

    e_list = []
    for i in range(e_count):
        print("Employee : ", i + 1)

        # ID ----------------------------------------------------------------
        id = input("\tEmployee ID : ")
        id = prevent_Duplicate(id, e_list)

        # Name --------------------------------------------------------------
        name = input("\tEmployee Name : ")

        # Gender ------------------------------------------------------------
        gender = input("\tEmployee Gender (Male/Female): ")
        gender = check_Gender(gender)

        # Date of Birth -----------------------------------------------------
        DoB = input("\tEmployee Date of Birth (DD/MM/YYYY) : ")
        DoB = check_Date(DoB)

        e_list.append(Employee(id, name, gender, DoB, office))
        print()

    e_list = sorted(e_list, key = lambda x: x.id)
    return e_list


def show_Employee(e_list):
    #
    # Show employee list as e_list
    # 

    print()
    print("Employee Information")
    print("ID\t\tName\t\t\t\tGender\t\tDoB\t\tOffice")

    for i in range(len(e_list)):
        e_list[i].display()


def salary(e_list, office):
    #
    # Create a new list of salary base on e_list
    # Payment list (Employee salary) as p_list
    #
    #       return p_list

    show_Employee(e_list)
    print()
    print("Choose employee 'ID' from the list to update salary ")
    print()

    p_list = []
    for i in range(len(e_list)):
        # ID ---------------------------------------------------------------
        id = input("Employee ID : ")
        while True:
            id = prevent_Duplicate(id, p_list)
            if not any(employee.id == id for employee in e_list):
                id = input("\tNo ID found. Try again : ")
            else:
                break
        for j in range(len(e_list)):
            if e_list[j].id == id:
                name = e_list[j].name

        # Working hours -----------------------------------------------------
        working_hour = input("\tWorking Hours (total hour/month) : ")
        while True:
            try: 
                if float(working_hour) < 201.0:
                    working_hour = float(working_hour)
                    break
                else:
                    working_hour = input("Try again (smaller than 201h) : ")
            except:
                    working_hour = input("Number only (smaller than 201h) : ")
        
        # wage --------------------------------------------------------------
        wage = input("\tWage/Hour (smaller than 9999$) : ")
        while True:
            try: 
                if float(wage) < 9999.0:
                    wage = float(wage)
                    break
                else:
                    wage = input("Try again (smaller than 9999$) : ")
            except:
                    wage = input("Number only (smaller than 9999$) : ")
        
        total = wage * working_hour
        total = math.floor(total)
        
        p_list.append(Salary(id, name, office, working_hour, wage, total))
        print()
    
    p_list = sorted(p_list, key = lambda x: x.id)
    return p_list


def show_Salary(p_list):
    #       
    # Show p_list

    print()
    print("Salary")
    print("ID\t\tName\t\t\t\tOffice\t\tWorking Hours\tWage\t\tTotal")
    
    for i in range(len(p_list)):
        p_list[i].display()


def insert_Salary(p_list):
    #
    # Dump p_list into Databse using pickle

    f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Salary{}.pickle".format(p_list[0].office), "wb")
    pickle.dump(p_list, f)
    f.close()


def read_Salary(office):
    #
    # Read p_list of the office from Database
    #       return p_list

    f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Salary{}.pickle".format(office), "rb")
    p_list = pickle.load(f)
    f.close()   
    return p_list


def add_Salary(e_list, p_list, office):
    #       
    # Add new salary info of the office
    #       return p_list

    print()
    show_Salary(p_list)

    # ID ----------------------------------------------------------------
    id = input("Employee ID : ")
    while True:
        id = prevent_Duplicate(id, p_list)
        if not any(employee.id == id for employee in e_list):
            id = input("\tNo ID found. Try again : ")
        else:
            break
    for j in range(len(e_list)):
        if e_list[j].id == id:
            name = e_list[j].name

    # Working hours -------------------------------------------------------
    working_hour = input("\tWorking Hours (total hour/month) : ")
    while True:
        try: 
            if float(working_hour) < 201.0:
                working_hour = float(working_hour)
                break
            else:
                working_hour = input("Try again (smaller than 201h) : ")
        except:
                working_hour = input("Number only (smaller than 201h) : ")
    
    # wage ----------------------------------------------------------------
    wage = input("\tWage/Hour (smaller than 9999$) : ")
    while True:
        try: 
            if float(wage) < 9999.0:
                wage = float(wage)
                break
            else:
                wage = input("Try again (smaller than 9999$) : ")
        except:
                wage = input("Number only (smaller than 9999$) : ")
    
    total = wage * working_hour
    total = math.floor(total)
    
    p_list.append(Salary(id, name, office, working_hour, wage, total))
    print()
    
    p_list = sorted(p_list, key = lambda x: x.id)
    return p_list


def del_Salary(p_list):
    #
    # Delete an salary info
    #       return p_list

    print()
    show_Salary(p_list)

    id = input("Choose employee 'ID' from the list to delete infomation : ")
    while True:
        if not any(salary.id == id for salary in p_list):
            id = input("\tNo ID found. Try again : ")
        else:
            break

    for i in range(len(p_list)):
        if p_list[i].id == id:
            del(p_list[i])

    p_list = sorted(p_list, key = lambda x: x.id)
    return p_list
    
def insert_Employee(e_list):
    #
    # Dump e_list into Databse using pickle

    f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Employee{}.pickle".format(e_list[0].office), "wb")
    pickle.dump(e_list, f)
    f.close()


def read_Employee(office):
    #         
    # Read e_list of the office from Database
    #       return e_list

    f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Employee{}.pickle".format(office), "rb")
    e_list = pickle.load(f)
    f.close()   
    return e_list


def add_Employee(e_list, office):
    #
    # Add new employee info of the office
    #       return e_list

    print()
    while True:
        e_count = input("Add how many people : ")
        while True:
            try: 
                e_count = int(e_count)
                break
            except:
                e_count = input("Integer only : ")

        if len(e_list) + e_count > 10:
            print("No more than 10 people in an office")
        else:
            break

    for i in range(e_count):
        print("Employee : ", i + len(e_list) + 1)
        id = input("\tEmployee ID : ")
        id = prevent_Duplicate(id, e_list)

        name = input("\tEmployee Name : ")

        gender = input("\tEmployee Gender (Male/Female): ")
        gender = check_Gender(gender)

        DoB = input("\tEmployee Date of Birth (DD/MM/YYYY) : ")
        DoB = check_Date(DoB)

        e_list.append(Employee(id, name, gender, DoB, office))
        print()

    e_list = sorted(e_list, key = lambda x: x.id)
    return e_list


def del_Employee(e_list):
    #
    # Delete an employee info
    #       return e_list

    print()
    show_Employee(e_list)
    
    id = input("Choose employee 'ID' from the list to delete infomation : ")
    while True:
        if not any(employee.id == id for employee in e_list):
            id = input("\tNo ID found. Try again : ")
        else:
            break
    
    for i in range(len(e_list)):
        if e_list[i].id == id:
            del(e_list[i])
    
    e_list = sorted(e_list, key = lambda x: x.id)
    return e_list 


def your_Info(office):
    #
    # Show informations of the staff who manage the office

    f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Staff{}.pickle".format(office), "rb")
    staff = pickle.load(f)
    f.close()  
    staff.display2()     


def main(office):
    #
    # running when input Username and Password of a staff

    print("OFFICE : {}".format(office))
    try:
        print("Getting Employee info.......", end = "")
        e_list = read_Employee(office)
        print("Done")
    except:
        print("No Employee info. Please update Employee info !")
    try:
        print("Getting Salary info.......", end = "")
        p_list = read_Salary(office)
        print("Done")
    except:
        print("No Salary info. Please update Salary info !")
    print()
    while True:
        print("'A' : Update employee info", end = "\t\t")
        print("'B' : Show employee info")
        print("'C' : Update salary", end = "\t\t\t")
        print("'D' : Show salary")
        print("'X' : Show your information")
        print("'Z' : Exit")
        answer = input("Choose your action : ")
        if answer == "A":
            print("\n\n")
            print("Updating employee info.......")
            print()
            while True:
                print("'1' : Create new employee info")
                print("'2' : Add new employee info")
                print("'3' : Del employee info")
                print("'4' : Cancel")
                answer = input("Choose your action : ")
                if answer == "1":
                    print()
                    e_count = employee_Count()
                    print()
                    e_list = update_Employee(e_count, office)
                    insert_Employee(e_list)
                    print()
                elif answer == "2":
                    try:
                        e_list = add_Employee(e_list, office)
                        insert_Employee(e_list)
                        print()
                    except:
                        print("No employee info. Please update employee info first")
                        print()
                elif answer == "3":
                    try:
                        e_list = (e_list)
                        insert_Employee(e_list)
                        print()
                    except:
                        print("No employee info. Please update employee info first")
                        print()
                elif answer == "4":
                    print()
                    break
                else:
                    print()
                    print("Action not recognized")
                    print()
        elif answer == "B":
            try:
                show_Employee(e_list)
            except:
                print("Need updating.......")
            print()
        elif answer == "C":
            print("\n\n")
            print("Updating salary info.......")
            try:
                print()
                while True:
                    print("'1' : Create new salary info")
                    print("'2' : Add salary info")
                    print("'3' : Del salary info")
                    print("'4' : Cancel")
                    answer = input("Choose your action : ")
                    if answer == "1":
                        print()
                        p_list = salary(e_list, office)
                        (p_list)
                        print()
                    elif answer == "2":
                        try:
                            p_list = add_Salary(e_list, p_list, office)
                            (p_list)
                            print()
                        except:
                            print("No salary info. Please update salary info first")
                            print()
                    elif answer == "3":
                        try:
                            p_list = del_Salary(p_list)
                            (p_list)
                            print()
                        except:
                            print("No salary info. Please update salary info first")
                            print()
                    elif answer == "4":
                        print()
                        break
                    else:
                        print()
                        print("Action not recognized")
                        print()
            except:
                print("No employee info. Please update employee info first")
        elif answer == "D":
            try:
                show_Salary(p_list)
            except:
                print("Need updating.......")
            print()
        elif answer == "X":
            your_Info(office)
            print()
        elif answer == "Z":
            print("Bravo Six, we're going dark !.... ")
            break
        else:
            print()
            print("Action not recognized")
            print()
            continue


    
   