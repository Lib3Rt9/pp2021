# import curses
from domains import student, course, mark, Std_Info, Course_Info, mark_Course
import numpy as np


# ------------------------------------------------------------------GPA
# GPA -----------------------------------------------------------------
# ---------------------------------------------------------------------
def GPA():
    m_Gpa = np.array([mark])
    credits = np.array([course])
    
    for s in student:
        for c in course:
            cal_gpa = (m_Gpa*Course_Info.c_Credits)/credits

        print(cal_gpa)
# (mark*credits)/total credit

def sort_By_GPA():
    
    sort_Student = sorted(student, key = lambda s_Std: s_Std.gpa,  reverse = True)
    # show_S = Std_Info.show_Std()
    for s_Std in sort_Student:
        s_Std.show_S


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


# 