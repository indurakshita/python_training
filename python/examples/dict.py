#dictonary

user={
	"name":"ram",
	"age":"25",
	"is married":True
	}

print(user)
print(type(user))
print(user["name"])
print(user.get('age'))
print(user.keys())
print(user.values())
print(user.items())

for x in user:
    print(x) # only print keys
    print(user[x]) #print keys and values
    print(x," ",user[x])

for x in user.values():
    print(x)
for x in user.items():
    print(x)
for x,y in user.items():
    print(x,y)
if "age" in user:
    print("present")
else:
    print("not present")
if "gender" in user:
    print("present")
else:
    print("not present")
   
#changing the values
user.update({"gender":'male'})
print(user)
user["age"]=35 #change age 25 into 35
print(user)
user.pop("age")
print(user)
user.clear()
print(user)

#nested dictionary
user={
    "u1":{
        "name":"ram",
        "age":"25",
        "is married":True
    },
    "u2":{
        "name":"raj",
        "age":"35",
        "is married":False
    }
}
print(user)
