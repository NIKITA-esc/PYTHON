# basic operation in python
str1 = "Python is a case sensitive  language"
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
print(" ".join(str2.split())) # remove extra whitespace from string

# variables
name = "nishu"
sid = 24379
dept = "civil"
print(f"Hey {name} here! \n My SID is {sid} \n My DEPARTMENT is {dept} ")

# bitwise operators
a = 40 # 0b101000
b = 43 # 0b101011
print(a & b) # a and b
print (a | b) # a or b
print(a ^ b) # XOR between two integers
print(a>>2 , b>>2) # right shift of a and  by 2
print(a<<2 , b<<2) # left shift of a and b by 2

# input statement
name = str(input ("Enter your full name here : "))
try:
    rank = int(input ("Enter your rank of JEE MAINS 2024: "))
    if rank < 40000:
        print("you got a seat at PEC!!" )
    else:
        print("Sorry, you can't grab a seat this year. But don't be sad , it is not the end of life. Give yourself one more chance.")
except ValueError:
    print(f"INVALID INPUT!! check {name}, again")







