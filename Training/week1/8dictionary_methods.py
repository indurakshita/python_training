# Ways:
# dict(hello="wordl")
# dict({"hello" :"wordl"})
# dict({})




from pprint import pprint

sample = {
    'name': 'albin',
    "profession": "Python developer",
    "age": None,
    "address":{
            "area": "vilankurichi",
            "city": "Cimbatore",
            "state": "Tamilnadu",
            "pincode": 641035
        },
    "hobbies": ["coding", "reading"]
    
}

# Method 1 Clear
# ac = sample.clear()

# Method 2 Copy
# ac = sample.copy()

# Method 3 FromKeys
# ac = sample.fromkeys()

# Method 4 Get
# ac = sample.get()

# Method 5 Items
# ac = sample.items()

# Method 6 Keys
# ac = sample.keys()

# Method 7 Values
# ac = sample.values()

# Method 8 Pop
# ac = sample.pop()

# Method 9 Popitems
# ac = sample.popitems()

# Method 10 Setdefault
# ac = sample.setdefault("name", "unspecified")


# Method 10 Update
sample.update({"company": "OneData Software Solutions"})


pprint(sample)

