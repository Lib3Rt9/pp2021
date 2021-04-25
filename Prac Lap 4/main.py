
import numpy 
import curses
from domains import student, course, mark
import input as inp
import output
# MAIN FUNCTION -------------- MAIN FUNCTION -------------- MAIN FUNCTION
# MAIN FUNCTION -------------- MAIN FUNCTION -------------- MAIN FUNCTION
# MAIN FUNCTION -------------- MAIN FUNCTION -------------- MAIN FUNCTION

def option():
    while (True):
        print("Type '?' for list of option")
        choose = input("      => Your option: ")
        if (choose == "?"):
            print("Select an option below: ")
            print("    +> 1. Input information about student and course")
            print("    +> 2. Input mark of student and course")
            print("    +> 3. Show information about student")
            print("    +> 4. Show information about course")
            print("    +> 5. Show mark of students in courses")
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

option()
