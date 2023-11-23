import re

from pydantic import BaseModel as base

# Number plate validation - tn-38-y-4525, tn 42 yy 4582

def validate(number_plate):
   
    pattern2 = r"(([A-Za-z]{2})-(\d{2})-([A-Za-z]{1,2})-(\d{4})|([A-Za-z]{2})\s(\d{2})\s([A-Za-z]{1,2})\s(\d{4}))"
    
    out2 = re.match(pattern2,number_plate)
    if out2:
        state,district,series,num = out2.groups()
        return (state,district,series,num)
            
# print(validate("tn 38 y 4525"))







