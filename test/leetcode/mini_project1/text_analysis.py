# Text Analysis Tool
# You're tasked with building a text analysis tool in Python. The tool should:
# - Take a string of your choice.

# Find and display the top 5 most common words in the text.
# - Identify and count the number of sentences in the text.

import json
import os
import sys

if sys.platform == "win32":
    clear = lambda: os.system("cls")
    clear()
else:
    clear = lambda: os.system("clear")


filename = "t_analysis.txt"
text="John is the son of John second.Second son of John second is William second."


def w_data(text=None):
    with open(filename,'w') as t:
        json.dump(text,t)
    return text
w_data(text)


def get_data(t=None):
    try:
        with open(filename,'r') as f:
            t=json.load(f)
            return t
    except FileNotFoundError:
            print("File not found")

# check=[".",",","!","?"]
# - Calculate and print the total word count in the file.
def w_count(option):
     
    t=get_data()
    tot_word=0
    if t:
        # t=t.replace[('lambda x:x for c in check'," ")]
        # t_sep=t.lower().split()
        # print(t_sep)
        t_sep=t.lower().replace(",",' ').replace(".",' ').replace("!"," ").replace("?"," ").split()
        
        tot_word=len(t_sep)
        print(f"Sentence is:{t}\n")
        print(f"Total word of the sentence is:{tot_word}")
        input()
        clear()
    else:
        print("still not get input values")
        s_new=input("enter the some sentence:\n")
        text=s_new
        return w_data(text)
        clear()
    return display()

# Find and display the top 5 most common words in the text.

def com_word(option):
    t=get_data()
    
    w_count={}
    if t:
        t_sep=t.lower().replace(",",' ').replace(".",' ').replace("!"," ").replace("?"," ").split()
        for i in t_sep:
            w_count[i]=w_count.get(i,0)+1
            comm_w=sorted(w_count.items(),key=lambda x: x[1],reverse=True)
            comm_w=dict((x,y) for x,y in comm_w if y>=2)
        print(f"This is the highest common words:\n")
        
        for i,j in comm_w.items():
            print(f"Common word of {i} is:".ljust(10),f"{j}")
        input()
        clear()   
        return display()
    

# - Identify and count the number of sentences in the text.

def c_sentence(option):
    t=get_data()
    if t:
        print(t)
        no_sen=len(t.split('.'))
        print("Number of Sentence is:",no_sen)
        input()
        clear()
    return display()

#Exit the program:

def exit(option):
    print("Exit the program...")
    input()
    clear()
    

def display():
    clear()
    print("text Analysis Tool".center(100))
    option=int(input("1.word counts\n2.common words\n3.count sentence\n4.exit\n"))
    clear()
    if  w_count(1):
        return w_count
    elif com_word(2):
        return com_word
    elif c_sentence(3):
        return c_sentence()
    elif exit(4):
        return exit()
    else:
        print("input not valid")
display()





