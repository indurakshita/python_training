import re

def val_password(password):
    
    pattern = r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%&*_+])(?!.*\s).{8,10}$"

    if re.match(pattern, password):
        return "Password is valid"
    else:
        return "Password not valid"


password = "@a3Adty_hh"
# print(val_password(password))



