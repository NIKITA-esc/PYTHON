str1 = "Python is a case sensitive  language"
# basic operations of python
print(len(str1))
print(str1[9:])  # string slicing
print(str1.replace("a case sensitive","object oriennted"))

substring = "\"a\""
try:
    index = str1.index(substring)
    print(f"the index of {substring} is : {index} ")
except ValueError:
    print(f"{substring} not found")

substring1 = "a"
try:
    index = str1.index(substring1)
    print(f"the index of {substring} is: {index}")
except ValueError:
    print(f"{substring} not found")

print(str1.replace(" ","")) # remove whitespace
str2 = "    Python is a good   language to start your programming career     "
print(str2.strip()) # remove leading and trailing whitespace
print(" ".join(str2.split())) # remove extra space from string








