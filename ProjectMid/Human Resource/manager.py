import math
import datetime
import pickle
import staff
from Domains.Manager import Manager
from Domains.Staff import Staff
from Domains.Employee import Employee
from Domains.Salary import Salary


def check_Date(DoB):
    #
    # Check:
    #     if DoB is in form DD/MM/YYYY
    #         return DoB

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

    id = id.strip()
    while True:
        if any(obj.id == id for obj in list):
            id = input("ID already existed. Try again : ")
            id = id.strip()
        else:
            break
    return id       


def staff_Count():
    # 
    # Count staff
    # Input number of staff members
    # input int(s_count) 
    #       return an Integer

    s_count = input("Enter the number of staff : ")
    while True:
        try: 
            s_count = int(s_count)
            break
        except:
            s_count = input("Integer only : ")
    return s_count


def staff_Info(s_count):
    #
    # Create a new list of the staffs
    #     return s_list
    
    # contains:
    #   ID
    #   Name
    #   Gender
    #   DoB
    #   office
    #   Password

    s_list = []
    for i in range(s_count):
        print("Staff : ", i +1)
        id = input("\tStaff ID : ")
        id = prevent_Duplicate(id, s_list)

        name = input("\tStaff Name : ")
         
        # input gender and check if it is valid
        gender = input("\tStaff Gender (Male/Female): ")
        gender = check_Gender(gender)

        # input DoB and check if it is valid
        DoB = input("\tStaff Date of Birth (DD/MM/YYYY) : ")
        DoB = check_Date(DoB)

        # Office = first letter of ID
        office = id[0]
        password = input("\tStaff Code : ")

        s_list.append(Staff(id, name, gender, DoB, office, password))
        print()

    s_list = sorted(s_list, key = lambda x: x.id)
    return s_list


def show_Staff(s_list):
    # 
    # Show s_list

    print()
    print("Staff Information")
    print("ID\t\tName\t\t\t\tGender\t\tDoB\t\tOffice\t\tPassword")
    
    for i in range(len(s_list)):
        s_list[i].display()


def insert_Staff(s_list):
    #
    # Dump s_list into Database using pickle
    
    f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Staffs.pickle", "wb")
    pickle.dump(s_list, f)
    f.close()
    
    for i in range(len(s_list)):
        f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Staff{}.pickle".format(s_list[i].office), "wb")
        pickle.dump(s_list[i], f)
        f.close()


def read_Staff():
    #
    # Read s_list from Databae
    #     return s_list

    f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Staffs.pickle", "rb")
    s_list = pickle.load(f)
    f.close()   
    return s_list


def add_Staff(s_list):
    #
    # Add new staff info
    #     return s_list

    print()
    s_count = input("Add how many people : ")
    while True:
        try: 
            s_count = int(s_count)
            break
        except:
            s_count = input("Integer only : ")

    for i in range(s_count):
        print("Staff : ", i + len(s_list) + 1)

        id = input("\tStaff ID : ")
        id = prevent_Duplicate(id, s_list)

        name = input("\tStaff Name : ")

        gender = input("\tStaff Gender (Male/Female): ")
        gender = check_Gender(gender)

        DoB = input("\tStaff Date of Birth (DD/MM/YYYY) : ")
        DoB = check_Date(DoB)

        office = id[0]

        password = input("\tStaff Code : ")

        s_list.append(Staff(id, name, gender, DoB, office, password))
        print()

    s_list = sorted(s_list, key = lambda x: x.id)
    return s_list


def del_Staff(s_list):
    #
    # Delete a staff info
    #     return s_list

    print()
    show_Staff(s_list)

    id = input("Choose staff 'ID' from the list to delete infomation : ")
    while True:
        if not any(staff.id == id for staff in s_list):
            id = input("\tNo ID found. Try again : ")
        else:
            break

    for i in range(len(s_list)):
        if s_list[i].id == id:
            del(s_list[i])

    s_list = sorted(s_list, key = lambda x: x.id)
    return s_list 


def get_Manager_Info():
    #
    # Get manager info
    #   return manager (object)
    
    id = "Alpha"
    name = input("\tYour Name : ")

    # input gender and check if it is valid
    gender = input("\tYour Gender (Male/Female) : ")
    gender = check_Gender(gender)
    
    # input Dob and check if it is valid
    DoB = input("\tYour Date of Birth (DD/MM/YYYY) : ")
    DoB = check_Date(DoB)
    
    # Show password in case of forgot
    password = input("\tYour password : ")
    
    manager = Manager(id, name, gender, DoB, password)
    return manager


def insert_Manager(manager):
    #     
    # Dump manager into Database using pickle

    f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Manager.pickle", "wb")
    pickle.dump(manager, f)
    f.close()


def read_Manager():
    #     
    # Read and show manager info from Database

    f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Manager.pickle", "rb")
    manager = pickle.load(f)
    f.close()
    manager.display()


def insert_All_Employee(s_list):
    #
    # Create a new list of all employee base on length of s_list
    #
    # Dump all employee information (all_e) into Database using pickle
    
    all_e = []
    for i in range(len(s_list)):
        try:
            f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Employee{}.pickle".format(s_list[i].office), "rb")
            e_list = pickle.load(f)
            f.close()
            all_e.append(e_list)
        except:
            print("Info missinng. Need update employee info of the {} office".format(s_list[i].office))
    
    f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Employees.pickle", "wb")
    pickle.dump(all_e, f)
    f.close()

def read_All_Employee():
    #
    # Read e_list from Database
    #     return all_e

    f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Employees.pickle", "rb")
    all_e = pickle.load(f)
    f.close()

    for i in range(len(all_e)):
        staff.show_employee(all_e[i])


def insert_All_Employee_Salary(s_list):
    #
    # Create a new list of all employee salary base on length of s_list
    #
    # Dump all employee salary information (all_p) into Database using pickle

    all_p = []
    for i in range(len(s_list)):
        try:
            f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Salary{}.pickle".format(s_list[i].office), "rb")
            p_list = pickle.load(f)
            f.close()
            all_p.append(p_list)
        except:
            print("Info missinng. Need update salary info of the {} office".format(s_list[i].office))
    
    f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Salaries.pickle", "wb")
    pickle.dump(all_p, f)
    f.close()


def read_All_Employee_Salary():
    #
    # read all_e from the database
    #     print all_e

    f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Salaries.pickle", "rb")
    all_p = pickle.load(f)
    f.close()
    for i in range(len(all_p)):
        staff.show_salary(all_p[i])


def staff_Salary(s_list):
    #
    # Create a new list of salary base on s_list
    # Money list (Staff salary) as m_list
    #     
    #       return m_list

    show_Staff(s_list)
    print()
    print("Choose Staff 'ID' from the list to update salary ")
    print()

    m_list = []
    for i in range(len(s_list)):
        # Input Staff id
        #       if id is not match
        #           input id
        #       else
        #           break

        id = input("Staff ID : ")
        while True:
            id = prevent_Duplicate(id, m_list)
            if not any(staff.id == id for staff in s_list):
                id = input("\tNo ID found. Try again : ")
            else:
                break

        for j in range(len(s_list)):
            if s_list[j].id == id:
                name = s_list[j].name

        # # input working_hour of Staff
        # while 
        #     if working_hour < 201.0
        #         return working_hour
        #     else
        #         retry =input(working_hour)

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
        
        # # input wage of staff per hour
        # while 
        #     if wage < 9999.0
        #         return wage
        #     else
        #         retry = input(wage)
            
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
        

        # Total salary = woring_hour * wage
        total = wage * working_hour
        total = math.floor(total)
        
        office = id[0]
        
        m_list.append(Salary(id, name, office, working_hour, wage, total))
        print()

    m_list = sorted(m_list, key = lambda x: x.id)
    return m_list 
 

def show_Staff_Salary(m_list):
    #     
    # Show Staff salary list (m_list)

    print()
    print("Staff Salary")
    print("ID\t\tName\t\t\t\tOffice\t\tWorking Hours\tWage\t\tTotal")
    
    for i in range(len(m_list)):
        m_list[i].display()


def insert_Staff_Salary(m_list):
    #
    # Dump m_list into Databse using pickle

    f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Staff Salary.pickle", "wb")
    pickle.dump(m_list, f)
    f.close()


def read_Staff_Salary():
    #
    # Read m_list
    #     return m_list

    f = open("C:\\Users\\FLOS IGNIS\\OneDrive\\Máy tính\\Human Resource\\Database\\Staff Salary.pickle", "rb")
    m_list = pickle.load(f)
    f.close()   
    return m_list


def add_Staff_Salary(s_list, m_list):
    #
    # Add new staff salary info
    #     return m_list

    print()
    show_Staff_Salary(m_list)

    id = input("Staff ID : ")
    while True:
        id = prevent_Duplicate(id, m_list)
        if not any(staff.id == id for staff in s_list):
            id = input("\tNo ID found. Try again : ")
        else:
            break

    for j in range(len(s_list)):
        if s_list[j].id == id:
            name = s_list[j].name

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
    
    office = id[0]
    
    m_list.append(Salary(id, name, office, working_hour, wage, total))
    print()
    
    m_list = sorted(m_list, key = lambda x: x.id)
    return m_list


def del_Staff_Salary(m_list):
    #
    # Delete an staff salary info
    #     return m_list

    print()
    show_Staff_Salary(m_list)

    id = input("Choose employee 'ID' from the list to delete infomation : ")
    while True:
        if not any(salary.id == id for salary in m_list):
            id = input("\tNo ID found. Try again : ")
        else:
            break

    for i in range(len(m_list)):
        if m_list[i].id == id:
            del(m_list[i])

    m_list = sorted(m_list, key = lambda x: x.id)
    return m_list


def main():
    try:
        print("Getting Staff info.......", end = "")
        s_list = read_Staff()
        print("Done")
    except:
        print("No Staff info. Please update Staff info !")
    try:
        print("Getting Staff Salary info.......", end = "")
        m_list = read_Staff_Salary()
        print("Done")
    except:
        print("No Staff Salary info. Please update Staff Salary info !")
    while True:
        print("'A' : Update Staff info", end = "\t\t")
        print("'B' : Show Staff info")
        print("'C' : Update Staff salary ", end = "\t")
        print("'D' : Show Staff salary")
        print("'E' : Show all Employee info", end = "\t")
        print("'F' : Show all Employee salary")
        print("'X' : Update your information", end = "\t")
        print("'Y' : Show your information")
        print("'Z' : Exit")
        answer = input("Choose your action : ")
        if answer == "A":
            print("\n\n")
            print("Updating staff info.......")
            print()
            while True:
                print("'1' : Create new staff info")
                print("'2' : Add new staff info")
                print("'3' : Del staff info")
                print("'4' : Cancel")
                answer = input("Choose your action : ")
                if answer == "1":
                    print()
                    s_count = staff_Count()
                    print()
                    s_list = staff_Info(s_count)
                    insert_Staff(s_list)
                    print()
                elif answer == "2":
                    try:
                        s_list = add_Staff(s_list)
                        insert_Staff(s_list)
                        print()
                    except:
                        print("No staff info. Please update staff info first")
                        print()
                elif answer == "3":
                    try:
                        s_list = del_Staff(s_list)
                        insert_Staff(s_list)
                        print()
                    except:
                        print("No staff info. Please update staff info first")
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
                show_Staff(s_list)
            except:
                print("Need updating.......")
            print()
        elif answer == "C":
            print("\n\n")
            print("Updating staff salary info.......")
            try:
                print()
                while True:
                    print("'1' : Create new staff salary info")
                    print("'2' : Add staff salary info")
                    print("'3' : Del staff salary info")
                    print("'4' : Cancel")
                    answer = input("Choose your action : ")
                    if answer == "1":
                        print()
                        m_list = staff_Salary(s_list)
                        insert_Staff_Salary(m_list)
                        print()
                    elif answer == "2":
                        try:
                            m_list = add_Staff_Salary(s_list, m_list)
                            insert_Staff_Salary(m_list)
                            print()
                        except:
                            print("No staff salary info. Please update staff salary info first")
                            print()
                    elif answer == "3":
                        try:
                            m_list = del_Staff_Salary(m_list)
                            insert_Staff_Salary(m_list)
                            print()
                        except:
                            print("No staff salary info. Please update staff salary info first")
                            print()
                    elif answer == "4":
                        print()
                        break
                    else:
                        print()
                        print("Action not recognized")
                        print()
            except:
                print("No staff info. Please update staff info first")
        elif answer == "D":
            try:
                show_Staff_Salary(m_list)
            except:
                print("Need updating.......")
            print()
        elif answer == "E":
            print()
            insert_All_Employee(s_list)
            read_All_Employee()
            print()
        elif answer == "F":
            print()
            insert_All_Employee_Salary(s_list)
            read_All_Employee_Salary()
            print()
        elif answer == "X":
            print("\n\n")
            print("Updating your info.......")
            print()
            while True:
                print("'1' : Update your info")
                print("'2' : Cancel")
                answer = input("Choose your action : ")
                if answer == "1":
                    print()
                    manager = get_Manager_Info()
                    insert_Manager(manager)
                    print()
                elif answer == "2":
                    break
                else:
                    print()
                    print("Action not recognized")
                    print()
        elif answer == "Y":
            read_Manager()
            print()
        elif answer == "Z":
            print("Bravo Six, we're going dark !.... ")
            break
        else:
            print()
            print("Action not recognized")
            print()
            continue

