import domains
import output
from domains import student, course, mark, Std_Info, Course_Info, mark_Course

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
        student.append({"Student #" + str(i + 1) + ": Id: " + Std_Info.s_ID + "; Name: " + Std_Info.s_Name + "; DoB: " + Std_Info.s_DoB})
        

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
