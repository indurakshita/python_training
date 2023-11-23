import re

'''here one dot represent match atleast character or more if u want 2 char 
u should put 2 dots but u extend string 2 or more '''

# x = 'x' 
# y ='abc'
# if re.match('..',y):  
#     print('yes')
# else:
#     print("no")


# String start with a simple pattern
'''Read a string with a substring of length 3 and Ist leter start with a and end s'''
# x = "aios"
# if re.match("a.s",x):   
#     print("yes")
# else:
#     print("no")

# x = "aisops"
# if re.match("a.s",x):   
#     print("yes")
# else:
#     print("no")

# x = "aio"
# if re.match("a.s",x):   
#     print("yes")
# else:
#     print("no")

# x = "bais"
# if re.match("a.s",x):   
#     print("yes")
# else:
#     print("no")
'-----------------------------------------------------------------------------------------------------------------'
# differenc b/w star(*) and(+) 
'''if using (.*) means zero or more character may comes or not
but if uusing (.+) means should contain atleast one character'''

'String with Specific Substring'
#  dot(.)* for beginning 0 or  more character accept
# x = "aosg"
# if re.match(".+a.s","aosg"):
# # if re.match(".*a.s",x):   
#     print("yes")
# else:
#     print("no")

'$ - symbol for end of the string'
# y = "baos"
# x = "aosg"

# if re.match(".*a.s$",x):   
#     print("yes")
# else:
#     print("no")

'Strings with Proper substring'
# Read a string that has a proper substring abc
# x = 'ffgabcz'
# y ='abc'
# if re.match(".abc+.",x):
# # if re.match(".*abc+.",x):   
#     print("yes")
# else:
#     print("no")

'$ part of the string'
# x = 'fb$c'
# # if re.match(".+\$$",x):
# if re.match(".+\$",x):
#     print("yes")
# else:
#     print("no")

# ------------------------------------------------------------------------------------------------------------
'examples for match'

# "valide Email address"
# email = "indu.1@gmail.ink"
# # out = [True if re.match(".+@.+\.in",email) else False]
# # print(out)

# out = True if re.match("[A-Za-z0-9._]*@[a-zA-Z]+\.[a-z]{2,3}$",email) else False
# print(out)

'Rule of Register number'
# r_num = '19CCET2011'
# out = [True if re.match("[0-9]{2}[A-Z]{4}[0-9]{4}$",r_num) else False]
# print(out)

# 'check mobil number'
# mob_no = "+91h 88455-03689"
# clean_no =re.sub(r"[^\s\+\d\-]",'',mob_no)
# print(clean_no)
# pattern1 = r"\+[1-9]{1,2}\s?(([1-9]\d{9}$)|([1-9]\d{4}-\d{5}$))"

# out = True if re.match(pattern1, clean_no) else False
# print(out)


# 'minimum and maximum'
# out = [True if re.match("[a-z]{1,3}[0-9]{2,4}$","abc123") else False]

 
# check valide number
# num = '++123'
# out = [True if re.match('[+-]?[0-9]+',num) else False]
# print(out)

# check constant
# x= 'baaed'
# out = [True if re.match("[a-z]*[^aeiou]+[a-z]",x) else False]
# print(out)

# check accept decimal numbers
# x = input()
# out = [True if re.match("[+-]?[0-9]{2}\.[0-9]{3}$",x)else False]
# print(out)
# '---------------------------------------------------------------------------------------------------------'
'find method'

# s = "123@rd123abcd123#rdin"
# out = re.finditer('123',s)
# for i in out:

#     # print(f"Start index {i.start()} - end index {i.end()}")
#     print(f"It's given start and end position = {i.span()}")
# out = re.findall('123',s)
# print(out)

'search method'
# out = re.match(r"123",s) #here output match
# out = re.match(r"rd",s) #match take the Ist position, here output None
# print(out)

# out = re.search(r"rd",s) #search anywhere in the given string,here give output
# print(out)


# 'group method'
# x = '27.50'
# s = "apple,orange"
# out1 = re.match(r"(\d+)\.(\d+)",x)
# out2 = re.match(r"(.+),(.+)",s)
# print(out1.groups())
# print(out2.groups())

# 'meta characters'

# s= "The rain in spain"
# out = re.findall("[a-n]",s)
# print(out)

# n = "The rain 100 in spain"
# out = re.findall("\d",n)
# print(out)

# s = "hello world"
# o = re.findall("h...o",s)
# r = re.findall("^He",s)
# print(o)
# print(r)

s ="The rain in spain Falls mainly in the plain"
# o = re.findall("aix*",s)
# r = re.findall("aix+",s)
# print(f"{o} \n{r}")
# o = re.findall("al{2}",s)  
# print(o)




# Number plate validation - tn-38-y-4525, tn 42 yy 4582

# (tn, 32, yy, 4587)



# print(validate("tn 42 yy 4582"))


username_pattern = r"\w+"
string = "5"

out = re.match(username_pattern, string)

print( "matches", out)

