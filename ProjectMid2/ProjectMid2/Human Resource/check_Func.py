# Checking functions ------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
def check_gender(gender):
    if gender == "Male" or gender == "Female":
        judgment = True                         # If gender is input correctly, return True
    else:
        judgment = False                        # Else return False
    return judgment                             

def prevent_duplicate(id, list):                
    id = id.strip()
    if any(obj.id == id for obj in list):
        judgment = False                        # If ID already existed, return False
    else:
        judgment = True                         # Else return True
    return judgment 

def prevent_duplicate2(office, list):           # For Staff only
    if any(obj.office == office for obj in list):
        judgment = False                        # If office already existed, return False
    else:
        judgment = True                         # Else return True
    return judgment