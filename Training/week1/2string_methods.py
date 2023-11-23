

sample = " One-data {position} software solutions {name}"


# # method 1 Capitalize
# c = sample.capitalize()
# print(c)

# # method 2 Casefold convert special caharacter to lowercase
# c = sample.casefold()
# print(c)

# # method 3 center 
# c = sample.center(20, "_")
# print(c)

# # # method 4 count
# c = sample.casefold().count("o")
# print(c)

# # method 5 encode
# c = sample.encode("utf-8")
# print(c)

# # method 6 endswith
# c = sample.endswith("ions")
# print(c)

# # method 7 startswith
c = sample.startswith("One")
print(c)

# # method 8 exapandtabs
# c = sample.expandtabs()
# print(c)

# # method 9 find
# c = sample.find("data")
# print(c)

# # method 10 find
# c = sample.format(name="Albin", position="python developer")
# print(c)

# # method 11 format_map
# c = sample.format_map({"name": "Albin", "position":"python developer"})
# print(c)

# # method 12 index
# c = sample.index("data", 2, 10)
# print(c)

# # method 13 isIdentifier
# d = "name2"
# print(d.isidentifier())

# # method 14 join
# c = "\t".join(sample.split())
# print(c)

# # method 15 ljust
# c = sample.ljust(50, "_")
# print(c)

# # method 16 rjust
# c = sample.rjust(50, "_")
# print(c)

# # method 17 maketrans
# c = str.maketrans("so", "tm")
# print(c)
# print(sample.translate(c))

# # method 18 replace
# c = sample.replace(" {position}", "").replace(" {name}", "")
# print(c)

# # method 19 rfind
# c = sample.rfind("z")
# print(c)

# # method 22 rindex
# c = sample.rindex("o")
# print(c)

# # method 21 partitions
# c = sample.partition("na")
# print(c)

# # method 22 rpartitions
# c = sample.rpartition("na")
# print(c)

# # method 23 split
# c = sample.rsplit("so")
# print(c)

# # method 24 split
# c = sample.split("so")
# print(c)

# # method 25 strip
# print(sample)
# c = sample.strip()
# print(c)


# # method 26 split
# print(sample)
# c = sample.splitlines()
# print(c)


# # method 27 swapcases
# print(sample)
# c = sample.swapcase()
# print(c)

# # method 28 swapcases
# c = sample.swapcase()
# print(c)

# method 29 title
# c = sample.title()
# print(c)

# # method 29 zfill
# c = sample.zfill(120)
# print(c)