import numpy as np
# import curses

student = []
course = []
mark = []

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
