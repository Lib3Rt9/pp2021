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
    m = input(" => Enter the mark: ")
    mark.append({"Student ID": s_ID, "Course ID": c_ID, "Mark": m})
    print()
# 
# 
# 
# PW5
def write_to_txt():
        with open("student.txt", "a+") as f1:
            f1.write("Student ID:" + Std_Info.s_ID)
            f1.write("Student Name:" + Std_Info.s_Name)
            f1.write("Student DoB: " + Std_Info.s_DoB)
            f1.close()

        with open("course.txt", "a+") as f2:
            f2.write("Name :" + Course_Info.get_c_ID)
            for i in Course_Info.c_ID:
                f2.write("  Course:" + str(Course_Info.get_c_ID))
            f2.close()

        with open("mark.txt", "a+") as f3:
            f3.write("Name :" + mark_Course.get_mark)
            for j in i.courses:
                f3.write(f"  Mark: " + str(mark))
            f3.close()

# Something wrong with this function...
# Need recheck
# 
#  


# Compress
def compress(nameFile):
        list_files = ["student.txt", "course.txt", "mark.txt"]
        
        compression = zip.ZIP_DEFLATED
        z = zip.ZipFile(nameFile, mode="w")
        
        for file in list_files:
            z.write(file, file, compress_type = compression)
        z.close()

# COmpress still have somthing wrong
# Updating...