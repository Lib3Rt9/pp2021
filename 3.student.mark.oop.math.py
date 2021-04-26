
import numpy as np
import curses

student = []
course = []
mark = []
# gpa = []

print("--------------------------------")
print()

stdscr = curses.initscr()
stdscr.addstr(0, 0, "Current mode: Typing mode",
              curses.A_REVERSE)
stdscr.refresh()

# --------------------------------------------------STUDENT INFORMATION
# STUDENT INFORMATION -------------------------------------------------
# ---------------------------------------------------------------------
class Std_Info():    
    def __init__(self, s_ID, s_Name, s_DoB):
        self.s_ID = s_ID
        self.s_Name = s_Name
        self.s_DoB = s_DoB
        
    # ID
    def get_ID(self):
        return self.s_ID
    def set_s_ID(self, s_ID):
        self.s_ID = s_ID
    
    # Name
    def get_Name(self):
        return self.s_Name
    def set_s_Name(self, s_Name):
        self.s_Name = s_Name

    # DoB
    def get_DoB(self):
        return self.s_DoB
    def set_s_DoB(self, s_DoB):
        self.s_DoB = s_DoB




# ---------------------------------------------------COURSE INFORMATION
# COURSE INFORMATION --------------------------------------------------
# ---------------------------------------------------------------------
class Course_Info():
    def __init__(self, c_ID, c_Name, c_Credits):
        self.c_ID = c_ID
        self.c_Name = c_Name
        self.c_Credits = c_Credits

    # Course ID
    def get_c_ID(self):
        return self.c_ID
    def set_c_ID(self, c_ID):
        self.c_ID = c_ID

    # Course Name
    def get_c_Name(self):
        return self.c_Name
    def set_c_Name(self, c_Name):
        self.c_Name = c_Name

    # Course Credits
    def get_c_Credits(self):
        return self.c_Credits
    def set_c_Credits(self, c_Credits):
        self.c_Credits = c_Credits




# -------------------------------------------------------------ADD MARK
# ADD MARK ------------------------------------------------------------
# ---------------------------------------------------------------------
class mark_Course():
    def __init__(self, s_ID, c_ID, markk):
        self.s_ID = s_ID
        self.c_ID = c_ID
        self.markk = markk

    # s_ID
    def set_s_ID(self, s_ID):
        self.s_ID = s_ID
    def get_s_ID(self):
        return self.s_ID
    
    # c_ID
    def get_c_ID(self):
        return self.c_ID
    def set_c_ID(self, c_ID):
        self.c_ID = c_ID

    # Mark
    def get_mark(self):
        return self.markk
    def set_mark(self, markk):
        self.markk = markk



# ------------------------------------------------------------------GPA
# GPA -----------------------------------------------------------------
# ---------------------------------------------------------------------
def GPA():
    m_Gpa = np.array([mark_Course.get_mark])
    credits = np.array([Course_Info.get_c_Credits])
    
    for s in student:
        for c in course:
            # # cal_gpa = (m_Gpa*Course_Info.c_Credits)/credits
            x = np.dot(m_Gpa, credits)
            sum = np.sum(credits)
            cal_Gpa = x/sum
        print(cal_Gpa)
# (mark*credits)/total credit

def sort_By_GPA():
    
    sort_Student = sorted(student, key = lambda s_Std: s_Std.gpa,  reverse = True)
    # show_S = Std_Info.show_Std()
    for s_Std in sort_Student:
        s_Std.show_S



# -------------------------------------------------------INPUT FUNCTION
# INPUT FUNCTION ------------------------------------------------------
# ---------------------------------------------------------------------
def add_Info():
    # Input Student information ##############################
    # Contain:
    #     - ID
    #     - Name
    #     - Date of Birth
    s_Num = int(input("How many students?\n  -> There are: "))
    for i in range(s_Num):
        Std_Info.s_ID = input("      - Student " + str(i + 1) + " ID: ")
        Std_Info.s_Name = input("      - Student " + str(i + 1) + " Name: ")
        Std_Info.s_DoB = input("      - Student " + str(i + 1) + " DoB: ")
        student.append({"Student #" + str
        (i + 1) + ": Id: " + Std_Info.s_ID + "; Name: " + Std_Info.s_Name + "; DoB: " + Std_Info.s_DoB})
        

        # student.append({"Student " + str(i + 1) + "})
        print()
        print("-----------------------------------------------------------------")

    # Input Course information ###############################
    # Contain:
    #      - ID
    #      - Name
    c_Num = int(input("How many courses?\n  -> There are: "))
    for i in range(c_Num):
        print("    * Enter information about course " + str(i + 1) + ": ")
        Course_Info.c_ID = input("      - Course " + str(i + 1) +" ID: ")
        Course_Info.c_Name = input("      - Course " + str(i + 1) +" Name: ")
        Course_Info.c_Credits = int(input("      - Course " + str(i + 1) + " Credits: "))
        course.append({"Course #" + str(i + 1) + ": Id: " + Course_Info.c_ID + "; Name: " + Course_Info.c_Name + "; Credits: " + str(Course_Info.c_Credits)})
        # print("Course #" + str(i + 1))
        # print("ID: " + Course_Info.c_ID)
        # print("Name: " + Course_Info.c_Name)
        # print("Credits: " + Course_Info.c_Credits)
        print()
        print("-----------------------------------------------------------------")



# ------------------------------------------------------------SHOW INFO
# SHOW INFO -----------------------------------------------------------
# ---------------------------------------------------------------------
def show_Student():
    print("Student list: ")
    print(student)
        

def show_Course():
    print("Course list: ")
    print(course)

def show_Mark():
    print("Mark list: ")
    print(mark)


# ----------------------------------------------------------------------------
# ADD MARK -------------------------------------------------------------------
# ----------------------------------------------------------------------------
def marking():
    print("-------------------------------")
    print()

    # Input for choosing:
    #      - Student:      ###########################
    show_Student()
    print(" => Select student by ID:")
    s_ID = input("    +> Option: ")
    print("--------------------------------------------------------")

    #      - Course:       ###########################
    show_Course()
    print(" => Select course by ID:")
    c_ID = input("    +> Option: ")
    print("--------------------------------------------------------")

    # Mark #######################################
    print()
    m = float(input(" => Enter the mark: "))
    mark.append({"Student ID": s_ID, "Course ID": c_ID, "Mark": m})
    print()



# MAIN FUNCTION -------------- MAIN FUNCTION -------------- MAIN FUNCTION
# MAIN FUNCTION -------------- MAIN FUNCTION -------------- MAIN FUNCTION
# MAIN FUNCTION -------------- MAIN FUNCTION -------------- MAIN FUNCTION

def option():
    while (True):
        print()
        print("Type '?' for list of option")
        choose = input("      => Your option: ")
        print()
        if (choose == "?"):
            print("Select an option below: ")
            print("    +> 1. Input information about student and course")
            print("    +> 2. Input mark of student and course")
            print("    +> 3. Show information about student")
            print("    +> 4. Show information about course")
            print("    +> 5. Show mark of students in courses")
            print("    +> 6. Show GPA of students")
            print("    +> 7. Show students after being sorted by GPA")
            print("""
         If you find that this program is to bad, just follow the step below.
         Have fun!!
         :)""")
            print("    +> 0. Type '0' ('zero') to quit")

        if (choose == "1"):
            add_Info()
        if (choose == "2"):
            marking()
        if (choose == "3"):
            show_Student()
        if (choose == "4"):
            show_Course()
        if (choose == "5"):
            show_Mark()
        if (choose == "6"):
            GPA()
        if (choose == "7"):
            print("You")
        if (choose == "0"):
            break
    print("""  :)
        Thanks for using this.
        See you later.
        Have fun!
        :)""")

# Information()
# # show_Student()
# # show_Course()
# mark_Course()
# show_Marks()
option()
# Std_Info.show_Std(self)
