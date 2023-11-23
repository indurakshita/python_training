def romanToInt(s):
    rom_int ={
         "I": 1,
         "V": 5,
         "X": 10,
         "L": 50,
         "C": 100,
         "D": 500,
         "M": 1000        
     }

    total = 0
    prev_value = 0  

    for rs in s:
        if rom_int.get(rs) is not None:
            cur_value= rom_int[rs]
            if cur_value >prev_value:
                total+=cur_value-2*prev_value
            else:
                total+=cur_value
            prev_value = cur_value
    return total
  
result = romanToInt("LVIII")
# print(result)

"--------------------------------------------------------------------------------------------------"
# remove element which user give
# def func(n, lis):
#     f=[]
#     for i in lis:
#         if i in n: 
#            del i
#         else:
            
#             yield i

# n = [3]
# lis = [1, 2, 3, 4, 3, 4, 5, 6]
# r = func(n, lis)
# # print(list(r))

# "-----------------------------------------------------------------------------------------------"
# # Find the Index of the First Occurrence in a String
# haystack = "sadbutsad"
# needle = "sad"

# index = haystack.find(needle)

# # print(index)
# "-----------------------------------------------"
# import re

# s = "sadbutsad"
# pattern = re.compile(r'sad')
# r= [i.start() for i in pattern.finditer(s)]
# # print(r)

# '-------------------------------------------------'

# s = "sadbutsad"
# pattern = "sad"

# matches = re.finditer(pattern, s)
# spans = [match.span() for match in matches]

# print(spans)

"----------------------------------------------------------------------------------------------"
# Search Insert Position

# def pos(n,t):
#     for i,num in enumerate(n):
#         if num in t:
#             return f"position of {num} is:{i}"
#         else:
#             n.append(t)
#     return n  
# nums=[1,3,5,6] 
# target = [2]

# r =pos(nums,t=target)
# print(r)

"--------------------------------------------------------------------------------------------------------------------"
# Length of Last Word
 
s="Learn algorithms at geeksforgeeks"
r=s.split()
length=len(r)
# print(r[length-1])
"----------------------------------------------------------------------------------------------------"
# Plus One
def func(n):
    # r= n[len(n)-1]
    # n[len(n)-1]=r+1
    # print(n)
    n[-1]+=1
    print(n)
# func([1,2,3,4])
"-------------------------------------------------------------------------------------------"
# add binary number
r=lambda a,b: bin(int(a,2)+int(b,2))
print(r(a="1010",b="1011")[2:])

"-------------------------------------------------------------------------"
# Contains Duplicate

# def func(n):
#     d=[]

#     for i in n:
#         if i in d:
#             return True
               
#         else:
#             d.append(i)
#     return False
          
# r=func([1,2,3,4])
# print(r)
'--------------------------------------------------------------------------'
# cache value using decorator

def deco(f):
    cache={}
    def wrap(*args,**kwargs):
        
        if args in cache:
            print("cache value")
            return cache[args]
        else:
            final=f(*args,**kwargs)
                
            cache[args]=final
            print(cache)
            print("final value")
            return final
    return wrap

@deco
def add(a,b):
    return a+b

print(add(5,4))   
print(add(5,4)) 
print(add(3,4))
print(add(3,4))
